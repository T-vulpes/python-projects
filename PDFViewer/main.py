import fitz  
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog

root = Tk()
root.geometry("900x700")
root.title("Vivid PDF Viewer")
root.configure(bg="#f5f5dc") 

frame = Frame(root, bg="#d9ead3")  
frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

canvas = Canvas(frame, bg="#ffffff", highlightthickness=0) 
scrollbar = Scrollbar(frame, orient=VERTICAL, command=canvas.yview, bg="#d9ead3")
scrollbar.pack(side=RIGHT, fill=Y)

canvas.pack(side=LEFT, fill=BOTH, expand=True)
canvas.configure(yscrollcommand=scrollbar.set)

inner_frame = Frame(canvas, bg="#ffffff")  
canvas.create_window((0, 0), window=inner_frame, anchor="nw")

images = []

def browse_files():
    filename = filedialog.askopenfilename(
        title="Select PDF File",
        filetypes=(("PDF Files", "*.pdf"), ("All Files", "*.*"))
    )
    if filename:
        display_pdf(filename)

def display_pdf(pdf_path):
    global images
    images.clear()  
    for widget in inner_frame.winfo_children():
        widget.destroy()  

    pdf_document = fitz.open(pdf_path)
    page_count = pdf_document.page_count

    for page_number in range(page_count):
        page = pdf_document[page_number]
        pix = page.get_pixmap()  
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        img_tk = ImageTk.PhotoImage(img)
        images.append(img_tk) 

        label = Label(inner_frame, image=img_tk, bg="#ffffff")
        label.pack(pady=10)

    inner_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))
    canvas.yview_moveto(0)

def on_mousewheel(event):
    canvas.yview_scroll(-1 * int(event.delta / 120), "units")

canvas.bind_all("<MouseWheel>", on_mousewheel)  # Windows 
canvas.bind_all("<Button-4>", lambda e: canvas.yview_scroll(-1, "units"))   #linux
canvas.bind_all("<Button-5>", lambda e: canvas.yview_scroll(1, "units"))  #linux

btn_frame = Frame(root, bg="#f5f5dc")
btn_frame.pack(pady=10)

open_btn = Button(
    btn_frame, 
    text="📂 Open PDF", 
    command=browse_files, 
    width=20, 
    font=("Arial", 14, "bold"), 
    bg="#4caf50",  
    fg="white", 
    activebackground="#45a049", 
    activeforeground="white", 
    bd=3, 
    relief=RAISED,
    cursor="hand2"
)
open_btn.pack()

inner_frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))
root.mainloop()
