import tkinter as tk
import time
import threading


class Visualizer:
    def __init__(self, parent, num_threads):
        self.parent = parent
        self.num_threads = num_threads

        # FIXED BACKGROUND — replaces broken transparent color
        self.canvas = tk.Canvas(
            parent,
            width=800,
            height=260,
            bg="#DCE3EC",     # MATCHES main.py background
            highlightthickness=0
        )
        self.canvas.pack()

        self.thread_objects = {}
        self.thread_glow = {}
        self.create_threads()


    # ---------------------------------------------------------------
    # Create glowing circles for threads
    # ---------------------------------------------------------------
    def create_threads(self):
        spacing = 800 // (self.num_threads + 1)
        x_pos = spacing

        for tid in range(self.num_threads):
            # Main circle
            circle = self.canvas.create_oval(
                x_pos - 25, 120 - 25,
                x_pos + 25, 120 + 25,
                fill="#AAAAAA",
                outline=""
            )

            # Glow
            glow = self.canvas.create_oval(
                x_pos - 40, 120 - 40,
                x_pos + 40, 120 + 40,
                fill="#AAAAAA20",
                outline=""
            )

            self.thread_objects[tid] = circle
            self.thread_glow[tid] = glow
            x_pos += spacing

        self.canvas.update()


    # ---------------------------------------------------------------
    # Thread State Colors
    # ---------------------------------------------------------------
    def get_colors(self, state):
        if state == "READY":
            return ("#F0C75E", "#F0C75E55")
        elif state == "RUNNING":
            return ("#50FA7B", "#50FA7BAA")
        elif state == "WAITING":
            return ("#4A90E2", "#4A90E255")
        elif state == "TERMINATED":
            return ("#FF5C5C", "#FF5C5C55")
        return ("#AAAAAA", "#AAAAAA20")


    # ---------------------------------------------------------------
    # Update circle colors & glow
    # ---------------------------------------------------------------
    def update_state(self, tid, state):
        fill_color, glow_color = self.get_colors(state)

        circle = self.thread_objects[tid]
        glow = self.thread_glow[tid]

        self.canvas.itemconfig(circle, fill=fill_color)
        self.canvas.itemconfig(glow, fill=glow_color)

        if state == "RUNNING":
            threading.Thread(target=self.pulse_effect, args=(glow,)).start()

        self.canvas.update()


    # ---------------------------------------------------------------
    # Breathing glow animation
    # ---------------------------------------------------------------
    def pulse_effect(self, glow_id):
        try:
            for _ in range(6):
                self.canvas.scale(glow_id, 0, 0, 1.03, 1.03)
                self.canvas.update()
                time.sleep(0.03)

            for _ in range(6):
                self.canvas.scale(glow_id, 0, 0, 0.97, 0.97)
                self.canvas.update()
                time.sleep(0.03)
        except:
            pass
