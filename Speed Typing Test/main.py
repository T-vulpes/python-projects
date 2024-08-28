import tkinter as tk
import time

class SpeedTypingTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Speed Typing Test")
        self.root.configure(bg="#d1c4e9")  # Background color

        self.sentences = [
            "Cultural diversity enriches society.",
            "Turkish cuisine is famous for its rich flavors.",
            "Russia is the largest country in the world by land area.",
            "Software development requires continuous learning.",
            "Volleyball is a popular sport in many countries.",
            "Traditional Turkish music reflects deep-rooted heritage.",
            "Moscow is the capital city of Russia.",
            "Open-source software benefits from community collaboration.",
            "The Turkish national volleyball team has achieved great success.",
            "Folk dances are an essential part of Turkish culture.",
            "Russia has a long history of classical literature.",
            "Learning to code opens up new career opportunities.",
            "Volleyball matches can be intense and competitive.",
            "Turkey is known for its historical sites and landmarks.",
            "The Hermitage Museum in Russia is one of the largest in the world.",
            "Agile methodology is widely used in software projects.",
            "Beach volleyball is played on sand courts.",
            "Turkish coffee is a symbol of hospitality.",
            "The Trans-Siberian Railway connects Moscow to Vladivostok.",
            "Debugging is a crucial part of the software development process."
        ]

        self.start_time = 0
        self.sentence_index = 0
        self.correct_count = 0

        # Main label
        self.label = tk.Label(root, text="Welcome to the Speed Typing Test!", font=("Helvetica", 16), bg="#d1c4e9", fg="#5e35b1")
        self.label.pack(pady=10)

        # Frame for the text and typing area
        self.frame = tk.Frame(root, bg="#d1c4e9")
        self.frame.pack(pady=10)

        # Display area for the sentence
        self.text_display = tk.Text(self.frame, height=4, width=50, font=("Helvetica", 14), wrap="word", bg="#ede7f6", fg="#4527a0")
        self.text_display.pack(side=tk.LEFT, padx=10)
        self.text_display.config(state=tk.DISABLED)

        # Typing area
        self.text_area = tk.Text(self.frame, height=4, width=50, font=("Helvetica", 14), wrap="word", bg="#ede7f6", fg="#4527a0")
        self.text_area.pack(side=tk.RIGHT, padx=10)
        self.text_area.bind("<Return>", self.check_typing)

        self.result_label = tk.Label(root, text="", font=("Helvetica", 16), bg="#d1c4e9", fg="#5e35b1")
        self.result_label.pack(pady=10)

        self.start_button = tk.Button(root, text="Start Test", command=self.start_test, font=("Helvetica", 14), bg="#7e57c2", fg="white")
        self.start_button.pack(pady=10)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_test, font=("Helvetica", 14), bg="#7e57c2", fg="white", state=tk.DISABLED)
        self.reset_button.pack(pady=10)

    def start_test(self):
        self.start_time = time.time()
        self.sentence_index = 0
        self.correct_count = 0
        self.text_area.config(state=tk.NORMAL)
        self.show_sentence()

    def show_sentence(self):
        if self.sentence_index < len(self.sentences):
            self.sentence = self.sentences[self.sentence_index]
            self.label.config(text="Type the following sentence as quickly as you can:")
            self.result_label.config(text="")
            self.text_display.config(state=tk.NORMAL)
            self.text_display.delete(1.0, tk.END)
            self.text_display.insert(tk.END, self.sentence)
            self.text_display.config(state=tk.DISABLED)
            self.text_area.delete(1.0, tk.END)  # Clear the typing area
            self.start_button.config(state=tk.DISABLED)
            self.reset_button.config(state=tk.NORMAL)
            self.text_area.focus()
        else:
            self.end_game()

    def check_typing(self, event=None):
        typed_text = self.text_area.get(1.0, tk.END).strip()

        if not typed_text:
            return  # If the user didn't type anything, return

        if typed_text == self.sentence:
            self.correct_count += 1
            self.sentence_index += 1
            self.show_sentence()  # Move to the next sentence
        else:
            self.text_display.config(state=tk.NORMAL)
            self.text_display.delete(1.0, tk.END)
            self.text_display.insert(tk.END, self.sentence)
            self.text_display.tag_add("wrong", 1.0, "end")
            self.text_display.tag_config("wrong", foreground="red")
            self.text_display.config(state=tk.DISABLED)
            self.text_area.config(state=tk.DISABLED)
            self.label.config(text="Incorrect typing! Game over.")
            self.show_results(self.calculate_wpm())
            self.reset_button.config(state=tk.NORMAL)

    def calculate_wpm(self):
        total_time = time.time() - self.start_time
        words_typed = sum(len(sentence.split()) for sentence in self.sentences[:self.sentence_index])
        words_per_minute = (words_typed / total_time) * 60 if total_time > 0 else 0
        return words_per_minute

    def end_game(self):
        words_per_minute = self.calculate_wpm()
        self.label.config(text="Congratulations! You typed all the sentences correctly!")
        self.show_results(words_per_minute)
        self.text_area.config(state=tk.DISABLED)
        self.reset_button.config(state=tk.NORMAL)
        self.start_button.config(state=tk.DISABLED)

    def show_results(self, words_per_minute):
        total_time = time.time() - self.start_time
        self.result_label.config(text=f"Typing Speed: {words_per_minute:.2f} WPM | Total Time: {total_time:.2f} seconds")

    def reset_test(self):
        self.label.config(text="Welcome to the Speed Typing Test!")
        self.text_display.config(state=tk.NORMAL)
        self.text_display.delete(1.0, tk.END)
        self.text_display.config(state=tk.DISABLED)
        self.text_area.delete(1.0, tk.END)
        self.result_label.config(text="")
        self.start_button.config(state=tk.NORMAL)
        self.reset_button.config(state=tk.DISABLED)
        self.sentence_index = 0
        self.correct_count = 0

if __name__ == "__main__":
    root = tk.Tk()
    app = SpeedTypingTest(root)
    root.mainloop()
