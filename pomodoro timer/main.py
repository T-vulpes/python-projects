
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import winsound

class PomodoroTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Timer")
        self.root.geometry("400x500")
        self.root.configure(bg="#e6e6fa")

        self.work_time = 25 * 60  
        self.break_time = 5 * 60  
        self.current_time = self.work_time
        self.is_working = True

        self.load_clock_image()

        self.timer_label = tk.Label(root, text=self.format_time(self.current_time), font=("Helvetica", 24))
        self.timer_label.place(relx=0.5, rely=0.35, anchor="center")

        self.start_button = tk.Button(root, text="Start", command=self.start_timer, bg="#90ee90", font=("Helvetica", 14))
        self.start_button.place(relx=0.5, rely=0.55, anchor="center")

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_timer, bg="#ff6f61", font=("Helvetica", 14))
        self.reset_button.place(relx=0.5, rely=0.65, anchor="center")

        self.work_duration_label = tk.Label(root, text="Work Duration", bg="#e6e6fa", font=("Helvetica", 12))
        self.work_duration_label.place(relx=0.3, rely=0.8, anchor="center")

        self.work_duration_display = tk.Label(root, text="25 mins", font=("Helvetica", 12))
        self.work_duration_display.place(relx=0.3, rely=0.85, anchor="center")

        self.increase_work_button = tk.Button(root, text="+", command=self.increase_work_time, font=("Helvetica", 12))
        self.increase_work_button.place(relx=0.2, rely=0.85, anchor="center")

        self.decrease_work_button = tk.Button(root, text="-", command=self.decrease_work_time, font=("Helvetica", 12))
        self.decrease_work_button.place(relx=0.4, rely=0.85, anchor="center")

        self.break_duration_label = tk.Label(root, text="Break Duration", bg="#e6e6fa", font=("Helvetica", 12))
        self.break_duration_label.place(relx=0.7, rely=0.8, anchor="center")

        self.break_duration_display = tk.Label(root, text="5 mins", font=("Helvetica", 12))
        self.break_duration_display.place(relx=0.7, rely=0.85, anchor="center")

        self.increase_break_button = tk.Button(root, text="+", command=self.increase_break_time, font=("Helvetica", 12))
        self.increase_break_button.place(relx=0.6, rely=0.85, anchor="center")

        self.decrease_break_button = tk.Button(root, text="-", command=self.decrease_break_time, font=("Helvetica", 12))
        self.decrease_break_button.place(relx=0.8, rely=0.85, anchor="center")

        self.is_running = False

    def load_clock_image(self):
        clock_image = Image.open("clock.png")  
        clock_image = clock_image.resize((150, 150), Image.Resampling.LANCZOS)
        self.clock_img = ImageTk.PhotoImage(clock_image)
        self.clock_label = tk.Label(self.root, image=self.clock_img, bg="#e6e6fa")
        self.clock_label.place(relx=0.5, rely=0.2, anchor="center")

    def format_time(self, seconds):
        mins, secs = divmod(seconds, 60)
        return f"{mins:02d}:{secs:02d}"

    def start_timer(self):
        if not self.is_running:
            self.is_running = True
            self.update_timer()

    def update_timer(self):
        if self.is_running:
            if self.current_time > 0:
                self.current_time -= 1
                self.timer_label.config(text=self.format_time(self.current_time))
                self.root.after(1000, self.update_timer)
            else:
                self.is_running = False
                self.timer_finished()

    def timer_finished(self):
        winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS) 
        if self.is_working:
            messagebox.showinfo("Time's up!", "Take a break!")
            self.current_time = self.break_time
            self.is_working = False
        else:
            messagebox.showinfo("Time's up!", "Time to work!")
            self.current_time = self.work_time
            self.is_working = True

        self.timer_label.config(text=self.format_time(self.current_time))

    def reset_timer(self):
        self.is_running = False
        self.current_time = self.work_time if self.is_working else self.break_time
        self.timer_label.config(text=self.format_time(self.current_time))

    def increase_work_time(self):
        self.work_time += 60
        self.work_duration_display.config(text=f"{self.work_time // 60} mins")
        if self.is_working:
            self.current_time = self.work_time
            self.timer_label.config(text=self.format_time(self.current_time))

    def decrease_work_time(self):
        if self.work_time > 60:
            self.work_time -= 60
            self.work_duration_display.config(text=f"{self.work_time // 60} mins")
            if self.is_working:
                self.current_time = self.work_time
                self.timer_label.config(text=self.format_time(self.current_time))

    def increase_break_time(self):
        self.break_time += 60
        self.break_duration_display.config(text=f"{self.break_time // 60} mins")
        if not self.is_working:
            self.current_time = self.break_time
            self.timer_label.config(text=self.format_time(self.current_time))

    def decrease_break_time(self):
        if self.break_time > 60:
            self.break_time -= 60
            self.break_duration_display.config(text=f"{self.break_time // 60} mins")
            if not self.is_working:
                self.current_time = self.break_time
                self.timer_label.config(text=self.format_time(self.current_time))

root = tk.Tk()
app = PomodoroTimer(root)
root.mainloop()
