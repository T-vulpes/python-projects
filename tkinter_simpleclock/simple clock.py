import tkinter as tk
from tkinter import Canvas
import time
import math

class SimpleClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Clock")
        self.root.geometry("400x400")
        self.canvas = Canvas(root, width=500, height=500, bg='darkred')
        self.canvas.pack(
        self.update_clock()

    def update_clock(self):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')

        self.canvas.delete("all") 
        self.canvas.create_oval(50, 50, 350, 350, outline='white', width=4)

        for i in range(12):
            angle = math.radians(30 * i - 90)  
            x1 = 200 + 130 * 0.8 * math.cos(angle)
            y1 = 200 + 130 * 0.8 * math.sin(angle)
            x2 = 200 + 130 * 0.9 * math.cos(angle)
            y2 = 200 + 130 * 0.9 * math.sin(angle)
            self.canvas.create_line(x1, y1, x2, y2, fill="white", width=3)

        self.canvas.create_text(200, 200, text=current_time, font=('calibri', 20, 'bold'), fill='white')

        self.root.after(1000, self.update_clock)

if __name__ == "__main__":
    root = tk.Tk()
    clock = SimpleClock(root)
    root.mainloop()
