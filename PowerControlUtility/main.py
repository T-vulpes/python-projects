from tkinter import *
from PIL import Image, ImageTk  
import os

def resize_image(file_path, width, height):
    image = Image.open(file_path)  
    resized_image = image.resize((width, height), Image.Resampling.LANCZOS)  
    return ImageTk.PhotoImage(resized_image)

def restarttime():
    os.system('shutdown -r -t 0')

def restart():
    os.system('shutdown -r -t 60')

def shutdown():
    os.system('shutdown -s -t 0')

def logout():
    os.system('shutdown -l')

root = Tk()
root.title("Shutdown Utility")
root.geometry("400x500")
root.config(bg="#2c3e50")

# Resimleri yeniden boyutlandırarak yükle
restarttimebutton = resize_image("restartime.png", 100, 100)
firstbutton = Button(root, image=restarttimebutton, borderwidth=0, cursor="hand2", command=restarttime, bg="#2c3e50")
firstbutton.place(x=50, y=50)

closebutton = resize_image("close.png", 100, 100)
secondbutton = Button(root, image=closebutton, borderwidth=0, cursor="hand2", command=root.destroy, bg="#2c3e50")
secondbutton.place(x=250, y=50)

restartbutton = resize_image("restart.png", 100, 100)
thirdbutton = Button(root, image=restartbutton, borderwidth=0, cursor="hand2", command=restart, bg="#2c3e50")
thirdbutton.place(x=50, y=200)

shutdownbutton = resize_image("shutdown.png", 100, 100)
fourthbutton = Button(root, image=shutdownbutton, borderwidth=0, cursor="hand2", command=shutdown, bg="#2c3e50")
fourthbutton.place(x=250, y=200)

logoutbutton = resize_image("logout.png", 100, 100)
fifthbutton = Button(root, image=logoutbutton, borderwidth=0, cursor="hand2", command=logout,)
fifthbutton.place(x=50, y=350)

# Üstte bir etiket ekleyelim
label = Label(root, text="System Control Panel", font=("Helvetica", 18), fg="white", bg="#2c3e50")
label.place(x=100, y=10)

root.mainloop()
