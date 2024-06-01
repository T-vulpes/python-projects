import json
from random import randint

class System:
    def __init__(self):
        self.running = True
        self.users = self.load_users()

    def run(self):
        while self.running:
            self.show_menu()
            choice = self.get_menu_choice()

            if choice == 1:
                self.login()
            elif choice == 2:
                self.register()
            elif choice == 3:
                self.forgot_password()
            elif choice == 4:
                self.exit()

    def show_menu(self):
        print("""
        1- Login
        2- Register
        3- Forgot Password
        4- Exit
        """)

    def get_menu_choice(self):
        while True:
            try:
                choice = int(input("Enter your choice: "))
                if 1 <= choice <= 4:
                    break
                else:
                    print("Please enter a number between 1 and 4.")
            except ValueError:
                print("Please enter a valid number.")
        return choice

    def load_users(self):
        try:
            with open("users.json", "r") as file:
                users = json.load(file)
        except FileNotFoundError:
            users = {}
        return users

    def save_users(self):
        with open("users.json", "w") as file:
            json.dump(self.users, file)

    def login(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        
        if username in self.users and self.users[username]["password"] == password:
            print("Login successful. Welcome, {}!".format(username))
        else:
            print("Incorrect username or password.")

    def register(self):
        username = input("Enter a new username: ")
        if username in self.users:
            print("Username already exists. Please choose another one.")
            return
        
        password = input("Enter a password: ")
        email = input("Enter your email address: ")
        activation_code = str(randint(1000, 9999))
        
        print("An activation code has been sent to your email address.")
        print("Your activation code:", activation_code)
        
        while True:
            entered_code = input("Enter the activation code: ")
            if entered_code == activation_code:
                break
            else:
                print("Incorrect activation code. Please try again.")

        self.users[username] = {"password": password, "email": email}
        self.save_users()
        print("Registration successful.")

    def forgot_password(self):
        username = input("Enter your username: ")
        if username in self.users:
            email = self.users[username]["email"]
            print("An email has been sent to your email address:", email)
        else:
            print("Username not found.")

    def exit(self):
        print("Exiting...")
        self.running = False

system = System()
system.run()
