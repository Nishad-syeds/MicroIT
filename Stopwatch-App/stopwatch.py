import tkinter as tk
import time

class Stopwatch:
    def __init__(self, master):
        self.master = master
        self.running = False
        self.start_time = 0

        self.setup_ui()

    def setup_ui(self):
        self.master.title("Stopwatch")
        self.master.geometry("300x200")
        self.master.config(bg="#f0f0f0")

        self.time_display = tk.Label(self.master, text="00:00:00", font=("Arial", 40), bg="#f0f0f0")
        self.time_display.pack(pady=20)

        self.start_btn = tk.Button(self.master, text="Start", command=self.start, width=10)
        self.start_btn.pack(side="left", padx=10)

        self.stop_btn = tk.Button(self.master, text="Stop", command=self.stop, width=10)
        self.stop_btn.pack(side="left", padx=10)

        self.reset_btn = tk.Button(self.master, text="Reset", command=self.reset, width=10)
        self.reset_btn.pack(side="left", padx=10)

    def update_time(self):
        if self.running:
            current_time = time.time() - self.start_time
            minutes = int(current_time / 60)
            seconds = int(current_time % 60)
            milliseconds = int((current_time * 100) % 100)
            self.time_display.config(text=f"{minutes:02}:{seconds:02}:{milliseconds:02}")
            self.master.after(10, self.update_time)

    def start(self):
        if not self.running:
            self.running = True
            self.start_time = time.time() - self.get_elapsed_time()
            self.update_time()

    def stop(self):
        self.running = False

    def reset(self):
        self.start_time = time.time()
        self.time_display.config(text="00:00:00")

    def get_elapsed_time(self):
        current = self.time_display.cget("text")
        minutes, seconds, milliseconds = map(int, current.split(":"))
        return minutes * 60 + seconds + milliseconds / 100

if __name__ == "__main__":
    root = tk.Tk()
    stopwatch = Stopwatch(root)
    root.mainloop()
