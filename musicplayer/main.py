from tkinter import *
from tkinter import filedialog
from pygame import mixer
import os
from PIL import Image, ImageTk  

root = Tk()
root.title("Music Player")
root.geometry("920x670+290+85")
root.configure(bg="#f0f0f0")  
root.resizable(False, False)

mixer.init()
directory = ""

def openfolder():
    global directory
    directory = filedialog.askdirectory()
    if directory:
        os.chdir(directory)
        songs = [song for song in os.listdir(directory) if song.endswith(".mp3")]
        playlist.delete(0, END)
        for song in songs:
            playlist.insert(END, song)

def playmusic():
    selected_song = playlist.get(ACTIVE)
    if selected_song:
        mixer.music.load(os.path.join(directory, selected_song))
        mixer.music.play()

def pausemusic():
    mixer.music.pause()

def stopmusic():
    mixer.music.stop()

# Görselleri yükleyip istenen boyuta getiren fonksiyon
def load_image(image_path, width, height):
    image = Image.open(image_path)
    image = image.resize((width, height), Image.LANCZOS)
    return ImageTk.PhotoImage(image)

# Görselleri aynı boyuta ayarla (örneğin 80x80)
img_width = 80
img_height = 80
play_img = load_image("play.png", img_width, img_height)
pause_img = load_image("pause.png", img_width, img_height)
stop_img = load_image("stop.png", img_width, img_height)

# Başlık etiketi
title_label = Label(root, text="Music Player", font=("Helvetica", 24, "bold"), bg="#f0f0f0", fg="#333")
title_label.pack(pady=20)

# Buton çerçevesi (kontroller)
button_frame = Frame(root, bg="#f0f0f0")
button_frame.pack(pady=20)

btn_play = Button(button_frame, image=play_img, bd=0, command=playmusic, bg="#f0f0f0", activebackground="#f0f0f0")
btn_pause = Button(button_frame, image=pause_img, bd=0, command=pausemusic, bg="#f0f0f0", activebackground="#f0f0f0")
btn_stop = Button(button_frame, image=stop_img, bd=0, command=stopmusic, bg="#f0f0f0", activebackground="#f0f0f0")

btn_play.grid(row=0, column=0, padx=20)
btn_pause.grid(row=0, column=1, padx=20)
btn_stop.grid(row=0, column=2, padx=20)

# Klasör açma butonu
folder_btn = Button(root, text="Open Folder", width=15, height=2, font=("Arial", 10, "bold"),
                    fg="white", bg="#a21b3d", command=openfolder)
folder_btn.pack(pady=20)

# Çalma listesi çerçevesi
playlist_frame = Frame(root, bd=2, relief=RIDGE, bg="#d9d9d9")
playlist_frame.pack(pady=20, padx=20, fill=BOTH, expand=True)

scroll = Scrollbar(playlist_frame)
playlist = Listbox(playlist_frame, font=("Arial", 10), bg="#ffffff", fg="black",
                   selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=scroll.set)
scroll.config(command=playlist.yview)
scroll.pack(side=RIGHT, fill=Y)
playlist.pack(side=LEFT, fill=BOTH, expand=True)

root.mainloop()
