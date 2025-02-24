from tkinter import *
from tkinter import filedialog, messagebox
from PyPDF2 import PdfFileWriter, PdfFileReader
import os

def browse():
    global filename
    filename = filedialog.askopenfilename(
        initialdir=os.getcwd(),
        title="Select File",
        filetypes=(("PDF Files", "*.pdf"), ("All Files", "*.*"))
    )
    entry1.insert(END, filename)

def protect_pdf():
    mainfile = source.get()
    protectfile = target.get()
    code = password.get()

    if mainfile == "" or protectfile == "" or code == "":
        messagebox.showerror("Invalid", "All fields must be filled!")
    else:
        try:
            pdf_reader = PdfFileReader(mainfile)
            pdf_writer = PdfFileWriter()

            for idx in range(pdf_reader.numPages):
                page = pdf_reader.getPage(idx)
                pdf_writer.addPage(page)

            pdf_writer.encrypt(code)

            with open(protectfile, "wb") as f:
                pdf_writer.write(f)

            target.set("")
            source.set("")
            password.set("")
            messagebox.showinfo("Success", "PDF Protected Successfully!")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

root = Tk()
root.title("PDF Protector")
root.geometry("700x550")
root.resizable(False, False)
root.configure(bg="#f0f0f0")  # Arka plan rengi

frame = Frame(root, width=580, height=290, bd=5, relief=GROOVE, bg="#e6e6e6")
frame.place(x=10, y=130)

source = StringVar()
Label(frame, text="PDF File:", font="Arial 10", fg="#4c4542", bg="#e6e6e6").place(x=30, y=50)
entry1 = Entry(frame, width=30, textvariable=source, font="Arial 15", bd=1)
entry1.place(x=150, y=48)
Button(frame, text="Browse", width=10, bg="#8f8f8f", fg="white", command=browse).place(x=500, y=45)

target = StringVar()
Label(frame, text="Target PDF:", font="Arial 10", fg="#4c4542", bg="#e6e6e6").place(x=30, y=100)
entry2 = Entry(frame, width=30, textvariable=target, font="Arial 15", bd=1)
entry2.place(x=150, y=100)

password = StringVar()
Label(frame, text="Set Password:", font="Arial 10", fg="#4c4542", bg="#e6e6e6").place(x=30, y=150)
entry3 = Entry(frame, width=30, textvariable=password, font="Arial 15", bd=1, show="*")
entry3.place(x=150, y=150)

protect_button = Button(root, text="Protect PDF", compound=LEFT, width=20, height=2, 
                        bg="#5c5c5c", fg="white", font="Arial 15", command=protect_pdf)
protect_button.place(x=230, y=450)

root.mainloop()
