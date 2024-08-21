import tkinter as tk
from tkinter import messagebox
from pygame import mixer

class MeditationTimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Meditation Timer App")
        self.root.configure(bg="#E0F7FA")  # Light blue color

        mixer.init()

        self.timer_label = tk.Label(root, text="00:00", font=("Helvetica", 48), bg="#E0F7FA")
        self.timer_label.pack(pady=20)

        self.duration_label = tk.Label(root, text="Enter Meditation Duration (seconds):", bg="#E0F7FA")
        self.duration_label.pack(pady=10)
        self.duration_entry = tk.Entry(root, width=10)
        self.duration_entry.pack(pady=5)

        self.plan_label = tk.Label(root, text="Or Choose a Meditation Plan:", bg="#E0F7FA")
        self.plan_label.pack(pady=10)

        self.plan_var = tk.StringVar(value="Select a Plan")
        self.plan_dropdown = tk.OptionMenu(root, self.plan_var, "Beginner (2 mins)", "Intermediate (5 mins)", "Advanced (10 mins)", command=self.select_plan)
        self.plan_dropdown.pack(pady=5)

        self.guide_text = tk.Text(root, height=10, width=50, wrap="word", bg="#B2EBF2")
        self.guide_text.pack(pady=10)
        self.guide_text.insert(tk.END, "Select a plan to see meditation instructions...")
        self.guide_text.config(state=tk.DISABLED)

        self.start_button = tk.Button(root, text="Start Meditation", command=self.start_meditation, bg="#81C784", fg="black")
        self.start_button.pack(pady=5)

        self.stop_button = tk.Button(root, text="Stop Meditation", command=self.stop_meditation, bg="#FF8A65", fg="black")
        self.stop_button.pack(pady=5)

        self.reset_button = tk.Button(root, text="Reset Timer", command=self.reset_timer, bg="#FFD54F", fg="black")
        self.reset_button.pack(pady=5)

        self.music_toggle_button = tk.Button(root, text="Mute Music", command=self.toggle_music, bg="#64B5F6", fg="black")
        self.music_toggle_button.pack(pady=5)

        self.progress_label = tk.Label(root, text="", bg="#E0F7FA")
        self.progress_label.pack(pady=10)

        self.is_running = False
        self.is_music_playing = True
        self.remaining_seconds = 0

    def select_plan(self, plan):
        if plan == "Beginner (2 mins)":
            self.duration_entry.delete(0, tk.END)
            self.duration_entry.insert(0, "120")
            self.show_guide("Beginner")
        elif plan == "Intermediate (5 mins)":
            self.duration_entry.delete(0, tk.END)
            self.duration_entry.insert(0, "300")
            self.show_guide("Intermediate")
        elif plan == "Advanced (10 mins)":
            self.duration_entry.delete(0, tk.END)
            self.duration_entry.insert(0, "600")
            self.show_guide("Advanced")

    def show_guide(self, level):
        self.guide_text.config(state=tk.NORMAL)
        self.guide_text.delete(1.0, tk.END)
        if level == "Beginner":
            guide = ("Beginner Plan:\n\n"
                     "1. Sit comfortably and close your eyes.\n"
                     "2. Focus on your breath. Inhale slowly through your nose.\n"
                     "3. Exhale slowly through your mouth.\n"
                     "4. If your mind starts to wander, gently bring your focus back to your breath.\n"
                     "5. Continue this for the entire 2 minutes.")
        elif level == "Intermediate":
            guide = ("Intermediate Plan:\n\n"
                     "1. Sit comfortably in a quiet space and close your eyes.\n"
                     "2. Take a few deep breaths to settle into the meditation.\n"
                     "3. Focus on the sensation of your breath moving in and out of your body.\n"
                     "4. If thoughts arise, simply acknowledge them and let them go, returning to your breath.\n"
                     "5. Continue to maintain a steady, relaxed focus for 5 minutes.")
        elif level == "Advanced":
            guide = ("Advanced Plan:\n\n"
                     "1. Find a comfortable sitting position and close your eyes.\n"
                     "2. Begin with deep breathing, slowly bringing your awareness to your breath.\n"
                     "3. Now, shift your focus inward, observing your thoughts and feelings without judgment.\n"
                     "4. Let go of each thought as it arises, gently returning your focus to your breath.\n"
                     "5. Continue this deep, mindful meditation for the full 10 minutes, staying present in the moment.")
        self.guide_text.insert(tk.END, guide)
        self.guide_text.config(state=tk.DISABLED)

    def start_meditation(self):
        try:
            duration = int(self.duration_entry.get())
            if duration <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a positive integer for the duration.")
            return

        self.remaining_seconds = duration
        self.is_running = True
        self.progress_label.config(text="Meditation in Progress...")
        mixer.music.load("meditation_sound.mp3")  # Load the music here
        mixer.music.play(-1)  # Start the music on a loop
        self.update_timer()

    def stop_meditation(self):
        self.is_running = False
        self.progress_label.config(text="Meditation Stopped.")
        mixer.music.stop()

    def reset_timer(self):
        self.stop_meditation()
        self.timer_label.config(text="00:00")
        self.progress_label.config(text="Timer Reset.")

    def update_timer(self):
        if self.is_running and self.remaining_seconds > 0:
            minutes, seconds = divmod(self.remaining_seconds, 60)
            self.timer_label.config(text=f"{minutes:02}:{seconds:02}")
            self.remaining_seconds -= 1
            self.root.after(1000, self.update_timer)
        elif self.remaining_seconds == 0:
            self.finish_meditation()

    def finish_meditation(self):
        self.is_running = False
        self.progress_label.config(text="Meditation Finished.")
        self.stop_meditation()

    def toggle_music(self):
        if self.is_music_playing:
            mixer.music.pause()
            self.music_toggle_button.config(text="Unmute Music")
        else:
            mixer.music.unpause()
            self.music_toggle_button.config(text="Mute Music")
        self.is_music_playing = not self.is_music_playing

root = tk.Tk()
app = MeditationTimerApp(root)
root.mainloop()
