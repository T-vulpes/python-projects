import tkinter as tk
from tkinter import messagebox

def add_task():
    box.insert(tk.END, e.get())
    e.delete(0, tk.END)

def delete_task():
    if len(box.curselection()) > 0:
        index = box.curselection()[0]
        box.delete(index)

def save_tasks():
    with open('tasks.txt', 'w', encoding='utf-8') as f:
        tasks = box.get(0, tk.END)
        f.writelines('\n'.join(tasks))
    messagebox.showinfo("Saved", "Tasks have been saved")

def load_tasks():
    with open('tasks.txt', 'r', encoding='utf-8') as f:
        tasks = f.readlines()
    box.delete(0, tk.END)
    for task in tasks:
        task = task.strip()
        box.insert(tk.END, task)

window = tk.Tk()
window.title("To-Do List")

# Adding scrollbar
frame = tk.Frame(window)
frame.pack()
box = tk.Listbox(frame, width=50, height=10)
box.pack(side=tk.LEFT)

scroll = tk.Scrollbar(frame, command=box.yview())
scroll.pack(side=tk.RIGHT, fill=tk.Y)
box.config(yscrollcommand=scroll.set)

e = tk.Entry(window, width=40)
e.pack()
e.focus()

add_button = tk.Button(window, text="Add Task", width=40, command=add_task)
add_button.pack()

delete_button = tk.Button(window, text="Delete Task", width=40, command=delete_task)
delete_button.pack()

save_button = tk.Button(window, text="Save Tasks", width=40, command=save_tasks)
save_button.pack()

load_button = tk.Button(window, text="Load Tasks", width=40, command=load_tasks)
load_button.pack()

window.mainloop()
