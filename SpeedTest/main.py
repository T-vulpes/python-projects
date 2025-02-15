from tkinter import *
import speedtest
import threading

def check():
    def run_speedtest():
        try:
            test = speedtest.Speedtest()
            test.get_best_server()

            downloading = round(test.download() / (1024 * 1024), 2)
            download.config(text=str(downloading) + " Mbps")
            Downlad.config(text=str(downloading) + " Mbps")

            uploading = round(test.upload() / (1024 * 1024), 2)
            upload.config(text=str(uploading) + " Mbps")

            ping.config(text=str(test.results.ping) + " ms")

        except Exception as e:
            ping.config(text="Error")
            download.config(text="Error")
            upload.config(text="Error")
            Downlad.config(text="Error")
            print("Speedtest Error:", e)

    threading.Thread(target=run_speedtest, daemon=True).start()

root = Tk()
root.title("Speed Test")
root.geometry("360x600")
root.configure(bg="#1a212d")

Label(root, text="Please wait for the result...", font="arial 9 italic", bg="#1a212d", fg="white").pack(pady=5)
top_img = PhotoImage(file="top.png").subsample(2)
Label(root, image=top_img, bg="#1a212d").pack()

main_img = PhotoImage(file="grap.png").subsample(2)
Label(root, image=main_img, bg="#1a212d").pack()

button_img = PhotoImage(file="startbutton.png").subsample(2)
start_button = Button(root, image=button_img, bg="#1a212d", bd=0, activebackground="#1a212d", cursor="hand2", command=check)
start_button.pack(pady=10)

Label(root, text="PING", font="arial 9 bold", bg="#384056", fg="white").place(x=85, y=80)  
Label(root, text="DOWNLOAD", font="arial 9 bold", bg="#384056", fg="white").place(x=140, y=80)
Label(root, text="UPLOAD", font="arial 9 bold", bg="#384056", fg="white").place(x=250, y=80)

Label(root, text="MS", font="arial 7 bold", bg="#384056", fg="white").place(x=75, y=100)
Label(root, text="MBPS", font="arial 7 bold", bg="#384056", fg="white").place(x=165, y=100)
Label(root, text="MBPS", font="arial 7 bold", bg="#384056", fg="white").place(x=265, y=100)

ping = Label(root, text="00", font="arial 10 bold", bg="#384056", fg="white")
ping.place(x=95, y=65, anchor="center")

download = Label(root, text="00", font="arial 10 bold", bg="#384056", fg="white")
download.place(x=180, y=65, anchor="center")

upload = Label(root, text="00", font="arial 10 bold", bg="#384056", fg="white")
upload.place(x=270, y=65, anchor="center")
Downlad = Label(root, text="00", font="arial 30 bold", bg="#384056", fg="white")
Downlad.place(x=185, y=270, anchor="center")

root.mainloop()
