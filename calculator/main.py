import tkinter as tk

def on_button_click(value):
    current = entry.get()
    if value in '+-*/%' and current.endswith(('+', '-', '*', '/', '%')):
        pass
    else:
        entry.insert(tk.END, value)

def on_clear():
    entry.delete(0, tk.END)

def on_delete():
    current = entry.get()
    entry.delete(len(current) - 1)

def on_equals():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def on_negate():
    current = entry.get()
    if current.startswith('-'):
        entry.delete(0)
    else:
        entry.insert(0, '-')

# Main window setup
root = tk.Tk()
root.title("Calculator")

# Entry area
entry = tk.Entry(root, font=('Arial', 40), borderwidth=0, relief="solid", justify='right', bg="#3c3c3c", fg="white", highlightthickness=0)
entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Buttons with enhanced colors
buttons = [
    ('AC', 1, 0, '#ffcccb', on_clear), ('+/-', 1, 1, '#ffcccb', on_negate), ('%', 1, 2, '#ffcccb', lambda: on_button_click('%')), ('/', 1, 3, '#ffeb99', lambda: on_button_click('/')),
    ('7', 2, 0, '#cce7ff', lambda: on_button_click('7')), ('8', 2, 1, '#cce7ff', lambda: on_button_click('8')), ('9', 2, 2, '#cce7ff', lambda: on_button_click('9')), ('*', 2, 3, '#ffeb99', lambda: on_button_click('*')),
    ('4', 3, 0, '#cce7ff', lambda: on_button_click('4')), ('5', 3, 1, '#cce7ff', lambda: on_button_click('5')), ('6', 3, 2, '#cce7ff', lambda: on_button_click('6')), ('-', 3, 3, '#ffeb99', lambda: on_button_click('-')),
    ('1', 4, 0, '#cce7ff', lambda: on_button_click('1')), ('2', 4, 1, '#cce7ff', lambda: on_button_click('2')), ('3', 4, 2, '#cce7ff', lambda: on_button_click('3')), ('+', 4, 3, '#ffeb99', lambda: on_button_click('+')),
    ('0', 5, 0, '#cce7ff', lambda: on_button_click('0')), ('.', 5, 1, '#cce7ff', lambda: on_button_click('.')), ('Del', 5, 2, '#ffcccb', on_delete), ('=', 5, 3, '#ffeb99', on_equals),
]

# Creating and placing the buttons
for (text, row, col, color, action) in buttons:
    tk.Button(root, text=text, width=5, height=2, bg=color, fg="black", font=('Arial', 18), command=action).grid(row=row, column=col, sticky="nsew")

# Proportional layout
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# Run the window
root.mainloop()
