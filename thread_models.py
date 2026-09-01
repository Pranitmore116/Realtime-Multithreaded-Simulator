import threading
import time
import random


# -------------------------------------------------------------
# Base Thread Model Class
# -------------------------------------------------------------
class BaseThreadModel:
    def __init__(self, num_threads, logger, visualizer_callback):
        self.num = num_threads
        self.log = logger
        self.update = visualizer_callback

    def set_state(self, tid, state):
        self.update(tid, state)
        self.log(f"Thread {tid}: {state}")


# -------------------------------------------------------------
# Many-to-One (User-level threads on single kernel thread)
# -------------------------------------------------------------
class ManyToOne(BaseThreadModel):
    def run(self):
        self.log("\n=== Many-to-One Model Running ===")
        time.sleep(0.7)

        # READY state (slower)
        for tid in range(self.num):
            self.set_state(tid, "READY")
            time.sleep(0.4)

        # Only ONE kernel thread executes at a time
        for tid in range(self.num):
            self.set_state(tid, "RUNNING")
            time.sleep(random.uniform(1.0, 1.8))   # Slow, smooth

            self.set_state(tid, "TERMINATED")
            time.sleep(0.3)


# -------------------------------------------------------------
# One-to-Many (Each user thread maps to one kernel thread)
# -------------------------------------------------------------
class OneToMany(BaseThreadModel):
    def thread_task(self, tid):
        # READY state slower
        self.set_state(tid, "READY")
        time.sleep(random.uniform(0.3, 0.5))

        # RUNNING state longer
        self.set_state(tid, "RUNNING")
        time.sleep(random.uniform(0.8, 1.5))

        self.set_state(tid, "TERMINATED")
        time.sleep(0.2)

    def run(self):
        self.log("\n=== One-to-Many Model Running ===")
        time.sleep(0.7)

        threads = []
        for tid in range(self.num):
            t = threading.Thread(target=self.thread_task, args=(tid,))
            t.start()
            threads.append(t)
            time.sleep(0.2)

        for t in threads:
            t.join()


# -------------------------------------------------------------
# Many-to-Many (User threads share limited kernel threads)
# -------------------------------------------------------------
class ManyToMany(BaseThreadModel):
    def thread_task(self, tid, semaphore):
        # READY state slower
        self.set_state(tid, "READY")
        time.sleep(random.uniform(0.3, 0.5))

        # WAITING
        self.set_state(tid, "WAITING")
        semaphore.acquire()

        # RUNNING slower
        self.set_state(tid, "RUNNING")
        time.sleep(random.uniform(0.8, 1.4))

        semaphore.release()

        self.set_state(tid, "TERMINATED")
        time.sleep(0.3)

    def run(self):
        self.log("\n=== Many-to-Many Model Running ===")
        time.sleep(0.7)

        semaphore = threading.Semaphore(3)  # 3 kernel threads max

        threads = []
        for tid in range(self.num):
            t = threading.Thread(target=self.thread_task, args=(tid, semaphore))
            t.start()
            threads.append(t)
            time.sleep(0.2)

        for t in threads:
            t.join()
