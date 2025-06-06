import tkinter as tk
from pynput import mouse
import threading
import math

class MouseTrackerApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Mouse Path Tracker")
        self.root.geometry("800x600")

        self.canvas = tk.Canvas(self.root, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.last_x = None
        self.last_y = None
        self.total_distance = 0.0
        self.distance_label = tk.Label(self.root, text="Distance: 0 px", font=("Arial", 12))
        self.distance_label.pack()

        self.listener_thread = threading.Thread(target=self.start_listener, daemon=True)
        self.listener_thread.start()

        self.root.mainloop()

    def start_listener(self):
        with mouse.Listener(on_move=self.on_move) as listener:
            listener.join()

    def on_move(self, x, y):
        self.root.after(0, self.update_canvas, x, y)

    def update_canvas(self, x, y):
        if self.last_x is not None and self.last_y is not None:
            self.canvas.create_line(self.last_x, self.last_y, x, y, fill="blue")
            self.total_distance += math.dist((self.last_x, self.last_y), (x, y))
            self.distance_label.config(text=f"Distance: {int(self.total_distance)} px")
        self.last_x = x
        self.last_y = y

if __name__ == "__main__":
    MouseTrackerApp()
