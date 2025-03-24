import tkinter as tk
from tkinter import messagebox, PhotoImage

def load_tasks():
    try:
        with open("tasklist.txt", "r") as file:
            tasks = file.readlines()
        for task in tasks:
            task = task.strip()
            if task:
                listbox.insert(tk.END, task)
    except FileNotFoundError:
        open("tasklist.txt", "w").close()

def add_task():
    task = task_entry.get()
    if task:
        listbox.insert(tk.END, task)
        with open("tasklist.txt", "a") as file:
            file.write(task + "\n")
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
        with open("tasklist.txt", "r") as file:
            tasks = file.readlines()
        with open("tasklist.txt", "w") as file:
            for index, task in enumerate(tasks):
                if index != selected_task_index:
                    file.write(task)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task!")

root = tk.Tk()
root.title("To-Do List")
root.geometry("450x550")
root.configure(bg="#1e1e2e")

heading = tk.Label(root, text="To-Do List", font="Arial 22 bold", fg="#cdd6f4", bg="#1e1e2e")
heading.pack(pady=15)

frame = tk.Frame(root, bg="#1e1e2e")
frame.pack(pady=10)

task_entry = tk.Entry(frame, width=30, font="Arial 14", bd=2, bg="#313244", fg="#cdd6f4", insertbackground="#cdd6f4")
task_entry.pack(side=tk.LEFT, padx=10)

add_button = tk.Button(frame, text="Ekle", font="Arial 12 bold", bg="#89b4fa", fg="#1e1e2e", command=add_task, padx=10, pady=5, bd=0, activebackground="#74c7ec")
add_button.pack(side=tk.LEFT)

frame1 = tk.Frame(root, bg="#1e1e2e")
frame1.pack(pady=10)

listbox = tk.Listbox(frame1, font="Arial 14", width=40, height=12, bg="#313244", fg="#cdd6f4", selectbackground="#89b4fa", bd=0, relief=tk.FLAT, highlightthickness=0)
listbox.pack(side=tk.LEFT, fill=tk.BOTH, padx=2)

scrollbar = tk.Scrollbar(frame1)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

delete_icon = PhotoImage(file="delete.png").subsample(6, 6)
delete_button = tk.Button(root, image=delete_icon, bd=0, command=delete_task, bg="#1e1e2e", activebackground="#1e1e2e")
delete_button.pack(pady=15)

load_tasks()
root.mainloop()
