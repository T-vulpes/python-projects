from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename, askopenfilename
import os, subprocess

root = Tk()
root.title("Python Idle")
root.geometry("1280x720+150+80")
root.configure(bg="#1E1E1E")  
root.resizable(False, False)

file_path = ""

def set_file_path(path):
    global file_path
    file_path = path

def openfile():
    path = askopenfilename(filetypes=[('Python Files', '*.py')])
    if not path:
        return
    with open(path, 'r') as file:
        code = file.read()
        code_input.delete("1.0", END)
        code_input.insert("1.0", code)
        set_file_path(path)

def runfile():
    global file_path
    if not file_path:
        messagebox.showerror("Python Idle", "Save your code before running")
        return
    command = f'python "{file_path}"'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    code_output.delete("1.0", END)
    code_output.insert("1.0", output.decode())
    code_output.insert("1.0", error.decode())

def savefile():
    global file_path
    if not file_path:
        path = asksaveasfilename(filetypes=[('Python Files', '*.py')], defaultextension=".py")
        if not path:
            return
    else:
        path = file_path
    
    with open(path, 'w') as file:
        code = code_input.get("1.0", END)
        file.write(code)
        set_file_path(path)

# Styling Text Areas
dark_grey = "#2D2D2D"
code_color = "#FFCC00"  # Yellowish text color for the input field
terminal_green = "#00FF00"

code_input = Text(root, font=("Consolas", 14), bg=dark_grey, fg=code_color, insertbackground="white", borderwidth=2, relief=SOLID)
code_input.place(x=180, y=0, width=680, height=720)

code_output = Text(root, font=("Consolas", 14), bg=dark_grey, fg=terminal_green, insertbackground="white", borderwidth=2, relief=SOLID)
code_output.place(x=860, y=0, width=420, height=720)

openimg = PhotoImage(file="open.png").subsample(3, 3)
saveimg = PhotoImage(file="save.png").subsample(3, 3)
runimg = PhotoImage(file="run.png").subsample(3, 3)

button_style = {"bg": "#0F0F0F", "bd": 2, "highlightthickness": 2, "highlightbackground": "#00FF00", "highlightcolor": "#00FF00", "width": 60, "height": 60}

Button(root, image=openimg, **button_style, command=openfile).place(x=30, y=30)
Button(root, image=runimg, **button_style, command=runfile).place(x=30, y=145)
Button(root, image=saveimg, **button_style, command=savefile).place(x=30, y=260)

status_bar = Label(root, text="Ready", bd=1, relief=SUNKEN, anchor=W, bg="#1E1E1E", fg="white")
status_bar.pack(side=BOTTOM, fill=X)

root.mainloop()
