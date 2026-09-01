import tkinter as tk
from tkinter import ttk
from thread_models import ManyToOne, OneToMany, ManyToMany
from synchronization import SemaphoreDemo, MonitorDemo
from visualizer import Visualizer
import threading


# -----------------------------------------------------
# Rounded rectangle (Windows-safe)
# -----------------------------------------------------
def round_rect(canvas, x1, y1, x2, y2, radius=20, fill="#FFFFFF", outline=""):
    points = [
        x1 + radius, y1,
        x2 - radius, y1,
        x2, y1,
        x2, y1 + radius,
        x2, y2 - radius,
        x2, y2,
        x2 - radius, y2,
        x1 + radius, y2,
        x1, y2,
        x1, y2 - radius,
        x1, y1 + radius,
        x1, y1
    ]
    return canvas.create_polygon(points, smooth=True, fill=fill, outline=outline)


# -----------------------------------------------------
# Glass-like card (NOW FULLY FIXED)
# -----------------------------------------------------
class GlassCard(tk.Canvas):
    def __init__(self, parent, width, height):
        super().__init__(
            parent,
            width=width,
            height=height,
            bg="#DCE3EC",        # match window background (FIXED)
            highlightthickness=0
        )

        shadow = "#DCE3EC"      # blend shadow with bg (IMPORTANT FIX)
        surface = "#FFFFFF"     # white card surface

        round_rect(self, 10, 10, width, height, radius=25, fill=shadow)
        round_rect(self, 0, 0, width - 10, height - 10, radius=25, fill=surface)


# -----------------------------------------------------
# Main App
# -----------------------------------------------------
class App:
    def __init__(self, root):
        self.root = root
        root.title("Real-Time Multi-threaded Application Simulator")
        root.geometry("1000x800")

        # Final background (FIXED)
        root.configure(bg="#DCE3EC")
        root["background"] = "#DCE3EC"

        # ------------------- TITLE (FIXED) -------------------
        tk.Label(
            root,
            text="Real-Time Multi-threaded Application Simulator",
            font=("Segoe UI", 22, "bold"),
            bg="#DCE3EC",            # FIXED
            fg="#2A2D34"
        ).pack(pady=15)

        # ------------------- CONTROL PANEL -------------------
        control_card = GlassCard(root, width=900, height=190)
        control_card.pack(pady=10)

        control_frame = tk.Frame(control_card, bg="#FFFFFF")
        control_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Model Selection
        tk.Label(
            control_frame, text="Select Model:",
            font=("Segoe UI", 14, "bold"),
            bg="#FFFFFF", fg="#333"
        ).grid(row=0, column=0, padx=10, pady=5)

        self.model_var = tk.StringVar(value="Many-to-One")
        self.model_select = ttk.Combobox(
            control_frame,
            textvariable=self.model_var,
            values=["Many-to-One", "One-to-Many", "Many-to-Many"],
            font=("Segoe UI", 12),
            state="readonly",
            width=18
        )
        self.model_select.grid(row=0, column=1, padx=10)

        # Thread count
        tk.Label(
            control_frame, text="Threads:",
            font=("Segoe UI", 14, "bold"),
            bg="#FFFFFF", fg="#333"
        ).grid(row=1, column=0, padx=10, pady=10)

        self.thread_count = tk.Entry(
            control_frame, font=("Segoe UI", 12),
            width=10, justify="center"
        )
        self.thread_count.insert(0, "5")
        self.thread_count.grid(row=1, column=1, padx=10)

        # Buttons
        ttk.Style().configure("Glass.TButton",
                              font=("Segoe UI", 11, "bold"),
                              padding=7)

        ttk.Button(control_frame, text="Run Thread Model",
                   style="Glass.TButton",
                   command=self.run_model).grid(row=2, column=0, pady=10)

        ttk.Button(control_frame, text="Semaphore Demo",
                   style="Glass.TButton",
                   command=self.run_semaphore).grid(row=2, column=1, pady=10)

        ttk.Button(control_frame, text="Monitor Demo",
                   style="Glass.TButton",
                   command=self.run_monitor).grid(row=2, column=2, pady=10)

        # ------------------- LOGS LABEL (FIXED) -------------------
        tk.Label(
            root, text="Logs:",
            font=("Segoe UI", 17, "bold"),
            bg="#DCE3EC",            # FIXED
            fg="#2A2D34"
        ).pack()

        # LOG CARD
        log_card = GlassCard(root, width=900, height=180)
        log_card.pack(pady=10)

        self.log_box = tk.Text(
            log_card, height=8, font=("Consolas", 12),
            bg="#FFFFFF", fg="#222", bd=0
        )
        self.log_box.place(relx=0.5, rely=0.5, anchor="center",
                           width=850, height=150)

        # ------------------- VISUALIZATION LABEL (FIXED) -------------------
        tk.Label(
            root, text="Thread Visualization:",
            font=("Segoe UI", 17, "bold"),
            bg="#DCE3EC",            # FIXED
            fg="#2A2D34"
        ).pack(pady=5)

        viz_card = GlassCard(root, width=900, height=300)
        viz_card.pack(pady=10)

        self.visualizer_frame = tk.Frame(viz_card, bg="#FFFFFF")
        self.visualizer_frame.place(relx=0.5, rely=0.5, anchor="center")

    def log(self, msg):
        self.log_box.insert(tk.END, msg + "\n")
        self.log_box.see(tk.END)

    def run_model(self):
        num = int(self.thread_count.get())

        for widget in self.visualizer_frame.winfo_children():
            widget.destroy()

        viz = Visualizer(self.visualizer_frame, num)
        model_choice = self.model_var.get()

        if model_choice == "Many-to-One":
            model = ManyToOne(num, self.log, viz.update_state)
        elif model_choice == "One-to-Many":
            model = OneToMany(num, self.log, viz.update_state)
        else:
            model = ManyToMany(num, self.log, viz.update_state)

        threading.Thread(target=model.run).start()

    def run_semaphore(self):
        threading.Thread(target=lambda: SemaphoreDemo(self.log).run_demo()).start()

    def run_monitor(self):
        threading.Thread(target=lambda: MonitorDemo(self.log).run_demo()).start()


root = tk.Tk()
App(root)
root.mainloop()
