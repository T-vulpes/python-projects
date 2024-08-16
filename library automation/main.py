import sqlite3
import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
import io

conn = sqlite3.connect('library.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL,
                    is_admin INTEGER NOT NULL)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    author TEXT NOT NULL,
                    year INTEGER NOT NULL,
                    image BLOB)''')

cursor.execute("INSERT OR IGNORE INTO users (username, password, is_admin) VALUES ('admin', 'admin123', 1)")

conn.commit()

class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.configure(bg='#2C3E50')
        self.is_admin = False 

        self.welcome_label = tk.Label(root, text="Welcome to the Library", font=("Helvetica", 16, "bold"), fg="#ECF0F1", bg="#2C3E50")
        self.welcome_label.pack(pady=20)

        self.login_button = tk.Button(root, text="Login", command=self.login, font=("Helvetica", 12), bg="#1ABC9C", fg="#ECF0F1")
        self.login_button.pack(pady=10)
        
        self.register_button = tk.Button(root, text="Register", command=self.register, font=("Helvetica", 12), bg="#3498DB", fg="#ECF0F1")
        self.register_button.pack(pady=10)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def login(self):
        self.clear_screen()

        self.login_label = tk.Label(self.root, text="Login", font=("Helvetica", 16, "bold"), fg="#ECF0F1", bg="#2C3E50")
        self.login_label.pack(pady=20)

        self.username_label = tk.Label(self.root, text="Username:", font=("Helvetica", 12), fg="#ECF0F1", bg="#2C3E50")
        self.username_label.pack(pady=5)
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(pady=5)

        self.password_label = tk.Label(self.root, text="Password:", font=("Helvetica", 12), fg="#ECF0F1", bg="#2C3E50")
        self.password_label.pack(pady=5)
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack(pady=5)

        self.login_button = tk.Button(self.root, text="Login", command=self.check_login, font=("Helvetica", 12), bg="#1ABC9C", fg="#ECF0F1")
        self.login_button.pack(pady=20)

    def check_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()

        if user:
            self.clear_screen()
            self.is_admin = user[3] == 1  # Kullanıcının admin olup olmadığını kontrol et
            if self.is_admin:  # Admin
                self.admin_dashboard()
            else:  # Normal kullanıcı
                self.user_dashboard()
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def register(self):
        self.clear_screen()

        self.register_label = tk.Label(self.root, text="Register", font=("Helvetica", 16, "bold"), fg="#ECF0F1", bg="#2C3E50")
        self.register_label.pack(pady=20)

        self.new_username_label = tk.Label(self.root, text="Username:", font=("Helvetica", 12), fg="#ECF0F1", bg="#2C3E50")
        self.new_username_label.pack(pady=5)
        self.new_username_entry = tk.Entry(self.root)
        self.new_username_entry.pack(pady=5)

        self.new_password_label = tk.Label(self.root, text="Password:", font=("Helvetica", 12), fg="#ECF0F1", bg="#2C3E50")
        self.new_password_label.pack(pady=5)
        self.new_password_entry = tk.Entry(self.root, show="*")
        self.new_password_entry.pack(pady=5)

        self.register_button = tk.Button(self.root, text="Register", command=self.create_account, font=("Helvetica", 12), bg="#3498DB", fg="#ECF0F1")
        self.register_button.pack(pady=20)

    def create_account(self):
        username = self.new_username_entry.get()
        password = self.new_password_entry.get()

        try:
            cursor.execute("INSERT INTO users (username, password, is_admin) VALUES (?, ?, 0)", (username, password))
            conn.commit()
            messagebox.showinfo("Success", "Account created successfully")
            self.login()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Username already exists")

    def admin_dashboard(self):
        self.clear_screen()

        self.dashboard_label = tk.Label(self.root, text="Admin Dashboard", font=("Helvetica", 16, "bold"), fg="#ECF0F1", bg="#2C3E50")
        self.dashboard_label.pack(pady=20)

        self.add_book_button = tk.Button(self.root, text="Add Book", command=self.add_book, font=("Helvetica", 12), bg="#1ABC9C", fg="#ECF0F1")
        self.add_book_button.pack(pady=10)
        
        self.view_books_button = tk.Button(self.root, text="View All Books", command=self.view_books, font=("Helvetica", 12), bg="#3498DB", fg="#ECF0F1")
        self.view_books_button.pack(pady=10)
        
        self.view_users_button = tk.Button(self.root, text="View Users", command=self.view_users, font=("Helvetica", 12), bg="#E67E22", fg="#ECF0F1")
        self.view_users_button.pack(pady=10)

        self.logout_button = tk.Button(self.root, text="Logout", command=self.logout, font=("Helvetica", 12), bg="#E74C3C", fg="#ECF0F1")
        self.logout_button.pack(pady=20)

    def user_dashboard(self):
        self.clear_screen()

        self.dashboard_label = tk.Label(self.root, text="User Dashboard", font=("Helvetica", 16, "bold"), fg="#ECF0F1", bg="#2C3E50")
        self.dashboard_label.pack(pady=20)

        self.view_books_button = tk.Button(self.root, text="View All Books", command=self.view_books, font=("Helvetica", 12), bg="#3498DB", fg="#ECF0F1")
        self.view_books_button.pack(pady=10)

        self.borrow_book_button = tk.Button(self.root, text="Borrow Book", command=self.borrow_book, font=("Helvetica", 12), bg="#1ABC9C", fg="#ECF0F1")
        self.borrow_book_button.pack(pady=10)

        self.logout_button = tk.Button(self.root, text="Logout", command=self.logout, font=("Helvetica", 12), bg="#E74C3C", fg="#ECF0F1")
        self.logout_button.pack(pady=20)

    def add_book(self):
        self.clear_screen()

        self.add_book_label = tk.Label(self.root, text="Add Book", font=("Helvetica", 16, "bold"), fg="#ECF0F1", bg="#2C3E50")
        self.add_book_label.pack(pady=20)

        self.title_label = tk.Label(self.root, text="Title:", font=("Helvetica", 12), fg="#ECF0F1", bg="#2C3E50")
        self.title_label.pack(pady=5)
        self.title_entry = tk.Entry(self.root)
        self.title_entry.pack(pady=5)

        self.author_label = tk.Label(self.root, text="Author:", font=("Helvetica", 12), fg="#ECF0F1", bg="#2C3E50")
        self.author_label.pack(pady=5)
        self.author_entry = tk.Entry(self.root)
        self.author_entry.pack(pady=5)

        self.year_label = tk.Label(self.root, text="Year:", font=("Helvetica", 12), fg="#ECF0F1", bg="#2C3E50")
        self.year_label.pack(pady=5)
        self.year_entry = tk.Entry(self.root)
        self.year_entry.pack(pady=5)

        self.image_label = tk.Label(self.root, text="Select Image:", font=("Helvetica", 12), fg="#ECF0F1", bg="#2C3E50")
        self.image_label.pack(pady=5)
        self.image_button = tk.Button(self.root, text="Browse", command=self.select_image, font=("Helvetica", 12), bg="#1ABC9C", fg="#ECF0F1")
        self.image_button.pack(pady=5)

        self.add_button = tk.Button(self.root, text="Add Book", command=self.save_book, font=("Helvetica", 12), bg="#3498DB", fg="#ECF0F1")
        self.add_button.pack(pady=20)

        self.back_button = tk.Button(self.root, text="Back", command=self.admin_dashboard, font=("Helvetica", 12), bg="#E74C3C", fg="#ECF0F1")
        self.back_button.pack(pady=10)

    def select_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png")])
        if self.image_path:
            messagebox.showinfo("Selected", f"Selected image: {self.image_path}")

    def save_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        year = self.year_entry.get()

        if title and author and year and self.image_path:
            with open(self.image_path, 'rb') as file:
                image_data = file.read()

            cursor.execute("INSERT INTO books (title, author, year, image) VALUES (?, ?, ?, ?)", (title, author, year, image_data))
            conn.commit()

            messagebox.showinfo("Success", "Book added successfully")
            self.admin_dashboard()
        else:
            messagebox.showerror("Error", "All fields and image selection are required")

    def view_books(self):
        self.clear_screen()

        self.view_books_label = tk.Label(self.root, text="All Books", font=("Helvetica", 16, "bold"), fg="#ECF0F1", bg="#2C3E50")
        self.view_books_label.pack(pady=20)

        cursor.execute("SELECT title, author, year FROM books")
        books = cursor.fetchall()

        for book in books:
            book_label = tk.Label(self.root, text=f"Title: {book[0]}, Author: {book[1]}, Year: {book[2]}", font=("Helvetica", 12), fg="#ECF0F1", bg="#2C3E50")
            book_label.pack(pady=5)

        self.back_button = tk.Button(self.root, text="Back", command=self.user_dashboard if not self.is_admin else self.admin_dashboard, font=("Helvetica", 12), bg="#E74C3C", fg="#ECF0F1")
        self.back_button.pack(pady=10)

    def borrow_book(self):
        self.clear_screen()

        self.borrow_label = tk.Label(self.root, text="Borrow a Book", font=("Helvetica", 16, "bold"), fg="#ECF0F1", bg="#2C3E50")
        self.borrow_label.pack(pady=20)

        cursor.execute("SELECT id, title FROM books")
        books = cursor.fetchall()

        self.book_var = tk.StringVar(self.root)
        self.book_var.set("Select a book")
        self.book_menu = tk.OptionMenu(self.root, self.book_var, *[book[1] for book in books])
        self.book_menu.pack(pady=10)

        self.days_label = tk.Label(self.root, text="Days:", font=("Helvetica", 12), fg="#ECF0F1", bg="#2C3E50")
        self.days_label.pack(pady=5)
        self.days_entry = tk.Entry(self.root)
        self.days_entry.pack(pady=5)

        self.borrow_button = tk.Button(self.root, text="Borrow", command=self.calculate_cost, font=("Helvetica", 12), bg="#1ABC9C", fg="#ECF0F1")
        self.borrow_button.pack(pady=20)

    def calculate_cost(self):
        days = int(self.days_entry.get())
        cost_per_day = 10
        total_cost = days * cost_per_day

        messagebox.showinfo("Total Cost", f"Total cost for borrowing the book for {days} days is: {total_cost} units")
        self.user_dashboard()

    def view_users(self):
        self.clear_screen()

        self.view_users_label = tk.Label(self.root, text="All Users", font=("Helvetica", 16, "bold"), fg="#ECF0F1", bg="#2C3E50")
        self.view_users_label.pack(pady=20)

        cursor.execute("SELECT username, is_admin FROM users")
        users = cursor.fetchall()

        for user in users:
            role = "Admin" if user[1] == 1 else "User"
            user_label = tk.Label(self.root, text=f"Username: {user[0]}, Role: {role}", font=("Helvetica", 12), fg="#ECF0F1", bg="#2C3E50")
            user_label.pack(pady=5)

        self.back_button = tk.Button(self.root, text="Back", command=self.admin_dashboard, font=("Helvetica", 12), bg="#E74C3C", fg="#ECF0F1")
        self.back_button.pack(pady=10)

    def logout(self):
        self.clear_screen()
        self.__init__(self.root)

root = tk.Tk()
app = LibraryApp(root)
root.mainloop()
