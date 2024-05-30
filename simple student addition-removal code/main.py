import sqlite3

class University:
    def __init__(self, name, country):
        self.name = name
        self.country = country
        self.running = True
        self.connect()

    def run(self):
        self.menu()
        choice = self.get_choice()

        if choice == 1:
            self.add_student()
        elif choice == 2:
            self.remove_student()
        elif choice == 3:
            self.update_student()
        elif choice == 4:
            self.show_all_students()
        elif choice == 5:
            self.exit()

    def add_student(self):
        print("**** STUDENT INFORMATION ****")
        name = input("Enter student's name: ").lower().capitalize()
        surname = input("Enter student's surname: ").lower().capitalize()
        faculty = input("Enter student's faculty: ").lower().capitalize()
        department = input("Enter student's department: ").lower().capitalize()
        student_id = input("Enter student's ID: ")

        while True:
            try:
                student_type = int(input("Enter student's type (1 or 2): "))
                if student_type not in (1, 2):
                    print("Student type should be 1 or 2.")
                    continue
                break
            except ValueError:
                print("Student type should be a number (1 or 2).")

        status = input("Enter student's status (Active or Passive): ")

        self.cursor.execute("INSERT INTO students VALUES('{}','{}','{}','{}','{}','{}','{}')".format(name, surname, faculty, department, student_id, student_type, status))
        self.connection.commit()

        print("Record added successfully!")

    def remove_student(self):
        self.cursor.execute("SELECT * FROM students")
        all_students = self.cursor.fetchall()
        convert_value = lambda x: [str(y) for y in x]

        for index, student in enumerate(all_students, 1):
            print("{}) {}".format(index, " ".join(convert_value(student))))

        while True:
            try:
                selection = int(input("Select the student to delete: "))
                break
            except ValueError:
                print("Please enter a valid number.")

        self.cursor.execute("DELETE FROM students WHERE rowid={}".format(selection))
        self.connection.commit()
        print("\nStudent deleted successfully!")

    def update_student(self):
        self.cursor.execute("SELECT * FROM students")
        all_students = self.cursor.fetchall()
        convert_value = lambda x: [str(y) for y in x]

        for index, student in enumerate(all_students, 1):
            print("{}) {}".format(index, " ".join(convert_value(student))))

        while True:
            try:
                selection = int(input("\nSelect the student to update: "))
                break
            except ValueError:
                print("Please enter a valid number.")

        while True:
            try:
                update_choice = int(input("1)Name\n2)Surname\n3)Faculty\n4)Department\n5)Student ID\n6)Type\n7)Status\nSelect which field to update: "))
                if update_choice < 1 or update_choice > 7:
                    continue
                break
            except ValueError:
                print("Please enter a valid number!")

        operations = ["name", "surname", "department", "faculty", "student_id", "student_type", "status"]

        if update_choice == 6:
            while True:
                try:
                    new_value = int(input("Enter the new value:"))
                    if new_value not in (1, 2):
                        continue
                    break
                except ValueError:
                    print("Please enter a valid number!")

            self.cursor.execute("UPDATE students SET student_type={} WHERE rowid={}".format(new_value, selection))
        else:
            new_value = input("Enter the new value:")
            self.cursor.execute("UPDATE students SET {}='{}' WHERE rowid={}".format(operations[update_choice - 1], new_value, selection))

        self.connection.commit()
        print("Update successful!")

    def show_all_students(self):
        self.cursor.execute("SELECT * FROM students")
        all_students = self.cursor.fetchall()
        convert_value = lambda x: [str(y) for y in x]

        for index, student in enumerate(all_students, 1):
            print("{}) {}".format(index, " ".join(convert_value(student))))

    def exit(self):
        self.running = False

    def menu(self):
        print("**** {} ADMIN SYSTEM **** ".format(self.name))
        print("\n 1)Add Student \n 2)Remove Student \n 3)Update Student \n 4)Show All Students\n 5)Exit")

    def get_choice(self):
        while True:
            try:
                choice = int(input("Select: "))
                if choice < 1 or choice > 5:
                    print("Your choice should be between 1 and 5! Please try again.\n")
                    continue
            except ValueError:
                print("Your choice should be a number! Please select the correct operation: ")

            return choice

    def connect(self):
        self.connection = sqlite3.connect("university.db")
        self.cursor = self.connection.cursor()

        self.cursor.execute("CREATE TABLE IF NOT EXISTS students(name TEXT,surname TEXT,department TEXT,faculty TEXT,student_id TEXT,student_type INT,status TEXT)")
        self.connection.commit()

university = University("Middle East Technical University", "Turkey")
while university.running:
    university.run()
