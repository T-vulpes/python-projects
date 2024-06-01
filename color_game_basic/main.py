import tkinter
import random

colors = [["yellow", "yellow"], ["black", "black"], ["orange", "orange"], ["grey", "grey"], ["green", "green"], ["red", "red"], ["blue", "blue"], ["navy blue", "navy blue"], ["purple", "purple"], ["pink", "pink"], ["brown", "brown"], ["white", "white"], ["violet", "violet"]]

def start(event):
    if remaining_time == 60:
        count_down()
    new_color()

def new_color():
    global score
    global remaining_time

    if remaining_time > 0:

        if entry.get().lower() == colors[1][1].lower():
            score += 1

        entry.delete(0, tkinter.END)

        random.shuffle(colors)
        label.config(fg=str(colors[1][0]), text=str(colors[0][1]))
        score_label.config(text="Score: " + str(score))

def count_down():
    global remaining_time
    if remaining_time > 0:
        remaining_time -= 1
        time_label.config(text="Remaining Time: " + str(remaining_time))
        time_label.after(1000, count_down)

score = 0
remaining_time = 60

window = tkinter.Tk()
window.title('Color Game')
window.geometry("450x350")

description = tkinter.Label(window, text="Type the Color of the Words, Not the Word Itself", font=("Helvetica", 12))
description.pack()

score_label = tkinter.Label(window, text="Press Enter to Start", font=("Helvetica", 12))
score_label.pack()

time_label = tkinter.Label(window, text="Remaining Time: " + str(remaining_time), font=("Helvetica", 12))
time_label.pack()

label = tkinter.Label(window, font=("Helvetica", 25))
label.pack()

entry = tkinter.Entry(window)

window.bind('<Return>', start)
entry.pack()
entry.focus_set()
window.mainloop()
