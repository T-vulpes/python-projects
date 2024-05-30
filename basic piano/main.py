import tkinter as tk
from playsound import playsound
import threading

def play_sound(note, button):
    button.config(relief=tk.SUNKEN)
    threading.Thread(target=playsound, args=(note,)).start()
    button.after(50, lambda: button.config(relief=tk.RAISED))

def do():
    play_sound('nota-do.wav', b1)

def re():
    play_sound('nota-re.wav', b2)

def mi():
    play_sound('nota-mi.wav', b3)

def fa():
    play_sound('nota-fa.wav', b4)

def sol():
    play_sound('nota-sol.wav', b5)

def la():
    play_sound('nota-lya.wav', b6)

def si():
    play_sound('nota-si.wav', b7)

def auto_play():
    with open('nota.txt') as f:
        lines = f.readlines()

    def play_notes(i):
        if i < len(lines):
            line = lines[i].split()
            def play_single_note(j):
                if j < len(line):
                    note = line[j].lower()
                    if note == 'do':
                        do()
                    elif note == 're':
                        re()
                    elif note == 'mi':
                        mi()
                    elif note == 'fa':
                        fa()
                    elif note == 'sol':
                        sol()
                    elif note == 'la':
                        la()
                    elif note == 'si':
                        si()
                    j += 1
                    window.after(200, lambda: play_single_note(j))
            play_single_note(0)
            i += 1
            window.after(200 * len(line) + 1000, lambda: play_notes(i))

    play_notes(0)

window = tk.Tk()
window.title('Piano')
window.geometry('520x400')

b1 = tk.Button(window, text='Do', font='Verdana 14 bold', bg='white', fg='black', height=10, width=3, command=do)
b1.place(x=50, y=20)
b2 = tk.Button(window, text='Re', font='Verdana 14 bold', bg='white', fg='black', height=10, width=3, command=re)
b2.place(x=110, y=20)
b3 = tk.Button(window, text='Mi', font='Verdana 14 bold', bg='white', fg='black', height=10, width=3, command=mi)
b3.place(x=170, y=20)
b4 = tk.Button(window, text='Fa', font='Verdana 14 bold', bg='white', fg='black', height=10, width=3, command=fa)
b4.place(x=230, y=20)
b5 = tk.Button(window, text='Sol', font='Verdana 14 bold', bg='white', fg='black', height=10, width=3, command=sol)
b5.place(x=290, y=20)
b6 = tk.Button(window, text='La', font='Verdana 14 bold', bg='white', fg='black', height=10, width=3, command=la)
b6.place(x=350, y=20)
b7 = tk.Button(window, text='Si', font='Verdana 14 bold', bg='white', fg='black', height=10, width=3, command=si)
b7.place(x=410, y=20)
b8 = tk.Button(window, text='Auto', font='Verdana 14 bold', bg='white', fg='black', height=1, width=10, command=auto_play)
b8.place(x=200, y=300)

window.mainloop()
