from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk  # Pillow kütüphanesi ile resimleri küçültmek için
import ast

def toggle_password():
    if code.cget('show') == '*':
        code.config(show='')
        eye_button.config(image=eye_open_img)
    else:
        code.config(show='*')
        eye_button.config(image=eye_closed_img)

def signup():
    username = user.get()
    password = code.get()
    confirm_password = confirm_code.get()

    if password == confirm_password:
        try:
            with open('datasheet.txt', 'r+') as file:
                d = file.read()
                try:
                    r = ast.literal_eval(d)  # Dosyayı sözlüğe çevir
                except:
                    r = {}  # Eğer dosya bozuksa, boş sözlük olarak başlat

                dict2 = {username: password}
                r.update(dict2)  # Yeni kullanıcıyı ekle

                file.seek(0)
                file.truncate(0)  # Dosyanın içeriğini temizle
                file.write(str(r))  # Güncellenmiş veriyi yaz

            messagebox.showinfo('Signup', 'Successfully signed up')
            window.destroy()
            import login  # Kayıt sonrası login ekranına yönlendirme

        except FileNotFoundError:
            with open('datasheet.txt', 'w') as file:
                file.write(str({username: password}))  # Yeni dosya oluştur ve kullanıcıyı ekle
    else:
        messagebox.showerror('Invalid', 'Both passwords should match!')

window = Tk()
window.title("Sign Up")
window.geometry("925x500+300+200")
window.configure(bg="white")
window.resizable(False, False)

img = PhotoImage(file="imgg.png")
Label(window, image=img, border=0, bg="white").place(x=50, y=90)

frame = Frame(window, width=350, height=390, bg="white")
frame.place(x=480, y=50)

heading = Label(frame, text="Sign Up", fg="#57a1f8", bg="white", font=("Arial", 23, "bold"))
heading.place(x=100, y=5)

def on_enter_user(event):
    if user.get() == "Username":
        user.delete(0, 'end')

def on_leave_user(event):
    if user.get() == '':
        user.insert(0, 'Username')

user = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Arial", 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind("<FocusIn>", on_enter_user)
user.bind("<FocusOut>", on_leave_user)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

def on_enter_pass(event):
    if code.get() == "Password":
        code.delete(0, 'end')
        code.config(show="*")

def on_leave_pass(event):
    if code.get() == '':
        code.insert(0, 'Password')
        code.config(show="")

code = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Arial", 11), show="*")
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind("<FocusIn>", on_enter_pass)
code.bind("<FocusOut>", on_leave_pass)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

# Göz resimlerini 25x25 boyutuna küçültme
eye_closed_raw = Image.open("eye.png").resize((25, 25))  
eye_open_raw = Image.open("eye_open.png").resize((25, 25))

# Tkinter uyumlu hale getir
eye_closed_img = ImageTk.PhotoImage(eye_closed_raw)
eye_open_img = ImageTk.PhotoImage(eye_open_raw)

eye_button = Button(frame, image=eye_closed_img, border=0, bg="white", command=toggle_password)
eye_button.place(x=260, y=145)  # Yüksekliği biraz düşürdüm ki hizalama daha iyi olsun

def on_enter_confirm(event):
    if confirm_code.get() == "Confirm Password":
        confirm_code.delete(0, 'end')
        confirm_code.config(show="*")

def on_leave_confirm(event):
    if confirm_code.get() == '':
        confirm_code.insert(0, 'Confirm Password')
        confirm_code.config(show="")

confirm_code = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Arial", 11))
confirm_code.place(x=30, y=220)
confirm_code.insert(0, 'Confirm Password')
confirm_code.bind("<FocusIn>", on_enter_confirm)
confirm_code.bind("<FocusOut>", on_leave_confirm)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=247)

Button(frame, width=39, border=0, pady=7, text="Sign Up", bg='#57a1f8', fg='white', command=signup).place(x=35, y=280)

label = Label(frame, text="I have an account", fg="#000", bg="white", font=("Arial", 9))
label.place(x=75, y=320)

signin = Button(frame, width=6, border=0, text="Sign In", cursor='hand2', fg='#57a1f8', bg='white')
signin.place(x=215, y=320)

window.mainloop()
