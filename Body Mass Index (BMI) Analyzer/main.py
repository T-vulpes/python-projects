from tkinter import *
import tkinter as tk
from tkinter import ttk
bmi_history = []

def BMI():
    try:
        h = float(Height.get())
        w = float(Weight.get())
        if h <= 0 or w <= 0:
            label1.config(text="Invalid Input", fg="#D0021B")
            label2.config(text="Enter valid values", fg="#D0021B")
            return
        
        m = h / 100
        bmi = round(float(w / m**2), 1)
        explanation = ""
        label1.config(text=f"BMI: {bmi}", fg="#2C3E50")

        if bmi < 18.5:
            explanation = "Underweight: You may need to gain some weight for better health."
            label2.config(text=explanation, fg="#4A90E2")
        elif 18.5 <= bmi < 24.9:
            explanation = "Normal Weight: You are at a healthy weight. Keep it up!"
            label2.config(text=explanation, fg="#7ED321")
        elif 25 <= bmi < 29.9:
            explanation = "Overweight: Consider making lifestyle changes for better health."
            label2.config(text=explanation, fg="#F5A623")
        else:
            explanation = "Obese: High risk for health issues. Consider a healthier lifestyle."
            label2.config(text=explanation, fg="#D0021B")
        
        bmi_history.append((h, w, bmi, explanation))
        update_history()
        
    except ValueError:
        label1.config(text="Invalid Input", fg="#D0021B")
        label2.config(text="Enter numbers only", fg="#D0021B")

def update_history():
    history_list.delete(0, END)
    for entry in bmi_history[-5:]:  
        history_list.insert(END, f"Height: {entry[0]} cm, Weight: {entry[1]} kg, BMI: {entry[2]}")

def clear_fields():
    Height.set("")
    Weight.set("")
    label1.config(text="")
    label2.config(text="")

def load_selected(event):
    selected = history_list.curselection()
    if selected:
        index = selected[0]
        h, w, bmi, explanation = bmi_history[index]
        Height.set(h)
        Weight.set(w)
        label1.config(text=f"BMI: {bmi}", fg="#2C3E50")
        label2.config(text=explanation, fg="#2C3E50")

root = Tk()
root.title("BMI Calculator")
root.geometry("400x600")
root.configure(bg="#34495E")
root.resizable(False, False)

frame = Frame(root, bg="#ECF0F1", bd=5, relief=RIDGE)
frame.pack(pady=20, padx=20, fill=BOTH, expand=True)
Label(frame, text="BMI Calculator", font="Arial 18 bold", bg="#ECF0F1", fg="#2C3E50").pack(pady=10)

Height = StringVar()
Weight = StringVar()

Label(frame, text="Height (cm)", font="Arial 12", bg="#ECF0F1", fg="#2C3E50").pack(pady=5)
height = Entry(frame, textvariable=Height, width=10, font="Arial 14", bd=2, justify=CENTER)
height.pack(pady=5)

Label(frame, text="Weight (kg)", font="Arial 12", bg="#ECF0F1", fg="#2C3E50").pack(pady=5)
weight = Entry(frame, textvariable=Weight, width=10, font="Arial 14", bd=2, justify=CENTER)
weight.pack(pady=5)

Button(frame, text="Calculate BMI", width=15, font="Arial 12 bold", bg="#3498DB", fg="white", command=BMI, bd=3, relief=RAISED, cursor="hand2").pack(pady=15)
Button(frame, text="Clear", width=15, font="Arial 12 bold", bg="#E74C3C", fg="white", command=clear_fields, bd=3, relief=RAISED, cursor="hand2").pack(pady=5)

label1 = Label(frame, font="Arial 18 bold", bg="#ECF0F1", fg="#2C3E50")
label1.pack(pady=10)

label2 = Label(frame, font="Arial 12 bold", bg="#ECF0F1", fg="#2C3E50", wraplength=350, justify=CENTER)
label2.pack(pady=10)

Label(frame, text="BMI History (Last 5 Entries):", font="Arial 12 bold", bg="#ECF0F1", fg="#2C3E50").pack(pady=5)
history_list = Listbox(frame, height=5, width=40, font="Arial 10", bg="#ECF0F1", fg="#2C3E50")
history_list.pack(pady=5)
history_list.bind("<<ListboxSelect>>", load_selected)
root.mainloop()
