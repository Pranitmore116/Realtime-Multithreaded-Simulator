import threading
import time
import random


# ================================================================
# SEMAPHORE DEMO (Simulates critical section access)
# ================================================================
class SemaphoreDemo:
    def __init__(self, log_func):
        self.log = log_func
        self.sem = threading.Semaphore(1)  # mutex / binary semaphore

    def thread_task(self, tid):
        self.log(f"[Semaphore] Thread {tid} waiting for critical section...")
        time.sleep(random.uniform(0.1, 0.3))

        self.sem.acquire()
        self.log(f"[Semaphore] Thread {tid} ENTERED critical section")
        time.sleep(random.uniform(0.3, 0.5))
        self.log(f"[Semaphore] Thread {tid} EXITED critical section")

        self.sem.release()

    def run_demo(self):
        self.log("\n=== Semaphore Demo Started ===\n")
        time.sleep(0.3)

        threads = []
        for tid in range(1, 5):
            t = threading.Thread(target=self.thread_task, args=(tid,))
            t.start()
            threads.append(t)
            time.sleep(0.1)

        for t in threads:
            t.join()

        self.log("\n=== Semaphore Demo Completed ===\n")


# ================================================================
# MONITOR DEMO (Producer–Consumer with wait/notify)
# ================================================================
class Monitor:
    def __init__(self):
        self.lock = threading.Lock()
        self.condition = threading.Condition(self.lock)
        self.resource_available = False


class MonitorDemo:
    def __init__(self, log_func):
        self.log = log_func
        self.monitor = Monitor()

    def consumer(self):
        with self.monitor.condition:
            self.log("[Monitor] Consumer: Waiting for resource...")
            while not self.monitor.resource_available:
                self.monitor.condition.wait()

            self.log("[Monitor] Consumer: Resource consumed!")
            self.monitor.resource_available = False

    def producer(self):
        time.sleep(random.uniform(0.3, 0.6))  # simulate work
        with self.monitor.condition:
            self.monitor.resource_available = True
            self.log("[Monitor] Producer: Resource created ✔")
            self.monitor.condition.notify()

    def run_demo(self):
        self.log("\n=== Monitor Demo Started ===\n")
        time.sleep(0.3)

        c = threading.Thread(target=self.consumer)
        p = threading.Thread(target=self.producer)

        c.start()
        time.sleep(0.2)
        p.start()

        c.join()
        p.join()

        self.log("\n=== Monitor Demo Completed ===\n")
