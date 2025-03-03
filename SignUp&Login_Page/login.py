from tkinter import *
from tkinter import messagebox
import ast

def signin():
    username = user.get()
    password = code.get()

    try:
        with open('datasheet.txt', 'r') as file:
            d = file.read()
            r = ast.literal_eval(d)  
    except (FileNotFoundError, SyntaxError):
        r = {}  

    if username in r and r[username] == password:
        screen = Toplevel(root)
        screen.title("App")
        screen.geometry("920x500+300+200")
        screen.config(bg="white")
        Label(screen, text="Your login is successful! Welcome to the home page!", bg="white", font=('Arial', 14)).pack(pady=20)
    else:
        messagebox.showerror("Invalid", "Invalid username or password")

def open_signup():
    root.destroy()
    import signUp  

root = Tk()
root.title('Login')
root.geometry("920x500+300+200")
root.configure(bg="#fff")
root.resizable(False, False)

def on_enter_user(event):
    if user.get() == "Username":
        user.delete(0, 'end')

def on_leave_user(event):
    if user.get() == '':
        user.insert(0, 'Username')

def on_enter_pass(event):
    if code.get() == "Password":
        code.delete(0, 'end')
        code.config(show="*")  

def on_leave_pass(event):
    if code.get() == '':
        code.insert(0, 'Password')
        code.config(show="") 

img = PhotoImage(file="img.png")
Label(root, image=img, bg="white").place(x=50, y=50)

frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

heading = Label(frame, text="Sign in", fg="#57a1f8", bg="white", font=("Arial", 23, "bold"))
heading.place(x=100, y=5)

user = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Arial", 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind("<FocusIn>", on_enter_user)
user.bind("<FocusOut>", on_leave_user)

Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)

code = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Arial", 11))
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind("<FocusIn>", on_enter_pass)
code.bind("<FocusOut>", on_leave_pass)

Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)

Button(frame, width=39, border=0, pady=7, text="Sign in", bg='#57a1f8', fg='white', command=signin).place(x=35, y=204)

label = Label(frame, text="Don't have an account?", fg="#000", bg="white", font=("Arial", 9))
label.place(x=75, y=270)

signup = Button(frame, width=6, border=0, text="Sign up", cursor='hand2', fg='#57a1f8', bg='white', command=open_signup)
signup.place(x=215, y=270)

root.mainloop()
