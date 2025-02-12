from tkinter import *
from tkinter import messagebox
import pandas as pd
from tkinter import ttk, filedialog

def style_config():
    style = ttk.Style()
    style.theme_use("clam")
    root.configure(bg="#1e1e1e")
    
    style.configure("TButton",
                    font=("Arial", 12, "bold"),
                    padding=10,
                    background="#333",
                    foreground="white",
                    borderwidth=2)
    style.map("TButton",
              background=[("active", "#0078d7")])

    style.configure("Treeview",
                    font=("Arial", 11),
                    rowheight=30,
                    background="#252526",
                    foreground="white",
                    fieldbackground="#252526",
                    borderwidth=0)
    style.configure("Treeview.Heading",
                    font=("Arial", 12, "bold"),
                    background="#333",
                    foreground="white")

    style.configure("TScrollbar",
                    background="#333",
                    troughcolor="#1e1e1e",
                    bordercolor="#1e1e1e")

def open_file():
    filename = filedialog.askopenfilename(
        title="Open a file",
        filetypes=[("Excel Files", "*.xlsx"), ("All Files", "*.*")]
    )

    if not filename:
        return  
    try:
        df = pd.read_excel(filename)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open the file.\nError: {e}")
        return  

    if df.empty:
        messagebox.showwarning("Warning", "The selected file is empty.")
        return  

    tree.delete(*tree.get_children())  

    tree["columns"] = list(df.columns)
    tree["show"] = "headings"

    for col in tree["columns"]:
        tree.heading(col, text=col)
        tree.column(col, width=150, anchor="center")

    for row in df.itertuples(index=False):
        tree.insert("", "end", values=row)

root = Tk()
root.title("Excel Viewer - Dark Mode")
root.geometry("1200x500+200+150")
style_config()

frame = Frame(root, bg="#1e1e1e")
frame.pack(pady=15, padx=15, fill=BOTH, expand=True)

tree_frame = Frame(frame, bg="#1e1e1e")
tree_frame.pack(fill=BOTH, expand=True)

tree_scroll_x = Scrollbar(tree_frame, orient=HORIZONTAL)
tree_scroll_y = Scrollbar(tree_frame, orient=VERTICAL)

tree = ttk.Treeview(tree_frame, xscrollcommand=tree_scroll_x.set, yscrollcommand=tree_scroll_y.set, selectmode="browse")
tree_scroll_x.config(command=tree.xview)
tree_scroll_y.config(command=tree.yview)

tree_scroll_x.pack(side=BOTTOM, fill=X)
tree_scroll_y.pack(side=RIGHT, fill=Y)
tree.pack(fill=BOTH, expand=True)

button = ttk.Button(root, text="Open Excel File", command=open_file)
button.pack(pady=15)

root.mainloop()
