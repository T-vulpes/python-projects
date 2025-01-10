from tkinter import *
from tkinter import messagebox
import time
import wavio as wv
import sounddevice as sound
from scipy.io.wavfile import write
from PIL import Image, ImageTk

root = Tk()
root.geometry("600x700+400+80")
root.resizable(False, False)
root.title("Voice Recorder")
root.configure(background="#ffffff")

def Record():
    try:
        freq = 44100
        dura = int(duration.get())
        if dura <= 0:
            raise ValueError("Duration must be a positive integer.")

        myimg.config(image=record_click_photo)
        root.update()

        recording = sound.rec(dura * freq, samplerate=freq, channels=2)
        for temp in range(dura, 0, -1):
            countdown_label.config(text=f"Recording in {temp}...", fg="#FF4500")
            root.update()
            time.sleep(1)

        countdown_label.config(text="Recording Complete!", fg="#32CD32")
        sound.wait()

        # Kaydedilen dosyayı yaz
        write("recording.wav", freq, recording)
        messagebox.showinfo("Success", "Recording saved as 'recording.wav'")

    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))
    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        # Resmi eski haline döndür (record.png)
        myimg.config(image=record_photo)
        root.update()

# Resimleri yeniden boyutlandırma
record_image = Image.open("record.png").resize((100, 100))
record_click_image = Image.open("recordClick.png").resize((100, 100))

record_photo = ImageTk.PhotoImage(record_image)
record_click_photo = ImageTk.PhotoImage(record_click_image)

# Arayüz elemanları
myimg = Label(image=record_photo, background="#ffffff")
myimg.pack(padx=5, pady=5)

Label(text="Voice Recorder", font="arial 30 bold", background="#ffffff", fg="#1E90FF").pack()

duration = StringVar()
Entry(root, textvariable=duration, font="arial 20", width=10, justify='center').pack(pady=10)
Label(text="Enter duration in seconds", font="arial 15", background="#ffffff", fg="#FF1493").pack()

record_button = Button(text="Record", font="arial 20", bg="#FF6347", fg="#ffffff", border=0, command=Record)
record_button.pack(pady=30)

# Geri sayım etiketi
countdown_label = Label(text="", font="arial 20 bold", background="#ffffff", fg="#000000")
countdown_label.pack(pady=20)

root.mainloop()
