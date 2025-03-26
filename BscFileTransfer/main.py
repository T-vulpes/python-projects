from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import socket
import os
import threading

def send_file():
    filename = filedialog.askopenfilename(title="Select a file")
    if not filename:
        return

    target_ip = target_ip_entry.get()
    target_port = int(target_port_entry.get())

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target_ip, target_port))
        with open(filename, "rb") as file:
            file_data = file.read(1024)
            while file_data:
                s.send(file_data)
                file_data = file.read(1024)
        s.close()
        messagebox.showinfo("Success", "File Sent Successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"File Sending Failed: {e}")

def receive_file():
    save_path = filedialog.askdirectory(title="Select Save Location")
    if not save_path:
        return

    server_ip = "0.0.0.0"  
    server_port = 5000 

    def server_thread():
        try:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind((server_ip, server_port))
            server.listen(1)
            messagebox.showinfo("Waiting", "Waiting for file transfer...")

            conn, addr = server.accept()
            messagebox.showinfo("Connected", f"Connected to {addr}")

            received_filename = os.path.join(save_path, "received_file")
            with open(received_filename, "wb") as file:
                file_data = conn.recv(1024)
                while file_data:
                    file.write(file_data)
                    file_data = conn.recv(1024)

            conn.close()
            messagebox.showinfo("Success", f"File Received! Saved to: {received_filename}")

        except Exception as e:
            messagebox.showerror("Error", f"Receiving Failed: {e}")

    threading.Thread(target=server_thread, daemon=True).start()

# **Gönderme Penceresi**
def send():
    window = Toplevel(root)
    window.title("Send File")
    window.geometry("450x300+500+200")
    window.configure(bg="#f4fdfe")
    window.resizable(False, False)

    Label(window, text="Target IP:", font="arial 12", bg="#f4fdfe").place(x=20, y=30)
    global target_ip_entry
    target_ip_entry = Entry(window, font="arial 12")
    target_ip_entry.place(x=120, y=30, width=200)

    Label(window, text="Port:", font="arial 12", bg="#f4fdfe").place(x=20, y=70)
    global target_port_entry
    target_port_entry = Entry(window, font="arial 12")
    target_port_entry.place(x=120, y=70, width=200)
    target_port_entry.insert(0, "5000")

    send_button = Button(window, text="Select File & Send", font="arial 12", bg="#57a1f8", fg="white", command=send_file)
    send_button.place(x=120, y=120, width=200, height=40)

def receive():
    window = Toplevel(root)
    window.title("Receive File")
    window.geometry("450x200+500+200")
    window.configure(bg="#f4fdfe")
    window.resizable(False, False)

    receive_button = Button(window, text="Select Folder & Receive", font="arial 12", bg="#57a1f8", fg="white", command=receive_file)
    receive_button.place(x=100, y=70, width=250, height=50)

root = Tk()
root.title("File Transfer")
root.geometry("450x560+500+200")
root.configure(bg="#f4fdfe")
root.resizable(False, False)

Label(root, text="FileTransfer", font="arial 15 bold", bg="#f4fdfe").place(x=20, y=30)
Frame(root, width=400, height=2, bg="#f355f6").place(x=25, y=80)

sendimage = Image.open("send.png").resize((100, 100))
sendimage = ImageTk.PhotoImage(sendimage)
receiveimage = Image.open("receive.png").resize((100, 100))
receiveimage = ImageTk.PhotoImage(receiveimage)

# Butonlar
send_button = Button(root, image=sendimage, bg="#f4fdfe", bd=0, command=send)
send_button.place(x=65, y=150)

receive_button = Button(root, image=receiveimage, bg="#f4fdfe", bd=0, command=receive)
receive_button.place(x=300, y=150)

Label(root, text="Send", font="arial 15 bold", bg="#f4fdfe").place(x=90, y=260)
Label(root, text="Receive", font="arial 15 bold", bg="#f4fdfe").place(x=310, y=260)

root.mainloop()
