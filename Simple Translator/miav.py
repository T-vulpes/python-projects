import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk 
import googletrans
from googletrans import Translator
import asyncio 

async def translate_text():
    text_input = source_text.get(1.0, tk.END)
    translator = Translator()    
    try:
        translated_text = await translator.translate(text_input, src=source_combo.get(), dest=target_combo.get())
        target_text.delete(1.0, tk.END)
        target_text.insert(tk.END, translated_text.text)
    except Exception as e:
        messagebox.showerror("Translation Error", str(e))

def translate_now():
    asyncio.run(translate_text())  

root = tk.Tk()
root.title("Translator")
root.geometry("900x500")
root.configure(bg="#f4f4f4")  

original_image = Image.open("arrow.png")
resized_image = original_image.resize((120, 60), Image.Resampling.LANCZOS)
arrow = ImageTk.PhotoImage(resized_image)

image_label = tk.Label(root, image=arrow, bg="#f4f4f4")
image_label.place(x=390, y=30)

languages = googletrans.LANGUAGES
language_values = list(languages.values())

source_combo = ttk.Combobox(root, values=language_values, font="Roboto 12", state="readonly", width=18)
source_combo.place(x=100, y=30)
source_combo.set("English")

source_label = tk.Label(root, text="From:", font="Roboto 11 bold", bg="#f4f4f4")
source_label.place(x=100, y=10)

target_combo = ttk.Combobox(root, values=language_values, font="Roboto 12", state="readonly", width=18)
target_combo.place(x=600, y=30)
target_combo.set("Select Language")

target_label = tk.Label(root, text="To:", font="Roboto 11 bold", bg="#f4f4f4")
target_label.place(x=600, y=10)

source_frame = tk.Frame(root, bg="white", bd=2, relief=tk.GROOVE)
source_frame.place(x=50, y=100, width=370, height=200)

source_text = tk.Text(source_frame, font="Roboto 12", bg="white", relief=tk.FLAT, wrap=tk.WORD)
source_text.place(x=0, y=0, width=360, height=190)

scrollbar1 = tk.Scrollbar(source_frame, command=source_text.yview)
scrollbar1.pack(side="right", fill="y")
source_text.configure(yscrollcommand=scrollbar1.set)

target_frame = tk.Frame(root, bg="white", bd=2, relief=tk.GROOVE)
target_frame.place(x=480, y=100, width=370, height=200)

target_text = tk.Text(target_frame, font="Roboto 12", bg="white", relief=tk.FLAT, wrap=tk.WORD)
target_text.place(x=0, y=0, width=360, height=190)

scrollbar2 = tk.Scrollbar(target_frame, command=target_text.yview)
scrollbar2.pack(side="right", fill="y")
target_text.configure(yscrollcommand=scrollbar2.set)

translate_button = tk.Button(root, text="Translate", font="Roboto 12 bold", activebackground="#6c63ff", cursor="hand2",
                          bd=0, width=12, height=2, bg="#6c63ff", fg="white", command=translate_now)
translate_button.place(x=380, y=330)
root.mainloop()
