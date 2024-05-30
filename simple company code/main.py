class Company:
    def __init__(self, name):
        self.name = name
        self.running = True

    def program(self):
        while self.running:
            self.show_menu()
            choice = self.get_menu_choice()

            if choice == 1:
                self.add_employee()
            elif choice == 2:
                self.remove_employee()
            elif choice == 3:
                self.show_salaries()
            elif choice == 4:
                self.show_employee_salaries()
            elif choice == 5:
                self.record_expense()
            elif choice == 6:
                self.record_income()
            elif choice == 7:
                self.exit_program()
            else:
                print("Invalid choice! Please enter a number between 1 and 7.")

    def show_menu(self):
        print(f"**** Welcome to {self.name} Automation ****\n\n"
              "1-Add Employee\n"
              "2-Remove Employee\n"
              "3-Show Total Budget\n"
              "4-Show Employees\n"
              "5-Pay Salaries\n"
              "5-Record Expense\n"
              "6-Record Income\n"
              "7-Exit\n")

    def get_menu_choice(self):
        while True:
            try:
                choice = int(input("Please enter your choice: "))
                if 1 <= choice <= 7:
                    return choice
                else:
                    print("Invalid choice! Please enter a number between 1 and 7.")
            except ValueError:
                print("Invalid choice! Please enter a valid number.")

    def add_employee(self):
        with open("employees.txt", "a") as file:
            emp_id = self.get_next_employee_id()
            name = input("Enter employee's first name: ")
            surname = input("Enter employee's surname: ")
            age = input("Enter employee's age: ")
            gender = input("Enter employee's gender: ")
            salary = input("Enter employee's salary: ")
            file.write(f"{emp_id} - {name} - {surname} - {age} - {gender} - {salary}\n")
            print("Employee added successfully.")

    def get_next_employee_id(self):
        try:
            with open("employees.txt", "r") as file:
                lines = file.readlines()
                if lines:
                    last_id = int(lines[-1].split(" - ")[0])
                    return last_id + 1
                else:
                    return 1
        except FileNotFoundError:
            return 1

    def remove_employee(self):
        try:
            with open("employees.txt", "r") as file:
                employees = file.readlines()
            if not employees:
                print("No employees found.")
                return
            print("Employees:")
            for i, employee in enumerate(employees, start=1):
                print(f"{i}. {employee.strip()}")
            choice = int(input("Please enter the number of the employee you want to remove: "))
            if 1 <= choice <= len(employees):
                del employees[choice - 1]
                with open("employees.txt", "w") as file:
                    file.writelines(employees)
                print("Employee removed successfully.")
            else:
                print("Invalid choice! Please enter a valid employee number.")
        except FileNotFoundError:
            print("No employees found.")

    def show_salaries(self):
        try:
            with open("budget.txt", "r") as file:
                budget = int(file.read())
            print(f"The total budget is: {budget}")
        except FileNotFoundError:
            print("Budget file not found. Please make sure 'budget.txt' exists.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def show_employee_salaries(self):
        try:
            with open("employees.txt", "r") as file:
                employees = file.readlines()
            if not employees:
                print("No employees found.")
                return
            print("Employees and their salaries:")
            for employee in employees:
                parts = employee.split(" - ")
                print(f"{parts[1]} {parts[2]} - Salary: {parts[-1]}")
        except FileNotFoundError:
            print("No employees found.")

    def pay_salaries(self):
        try:
            with open("employees.txt", "r") as file:
                employees = file.readlines()
            if not employees:
                print("No employees found.")
                return
            total_salaries = sum(int(employee.split(" - ")[-1]) for employee in employees)
            
            with open("budget.txt", "r") as file:
                budget = int(file.read())
            
            if budget < total_salaries:
                print("Insufficient budget to pay salaries.")
                return
            
            budget -= total_salaries
            
            with open("budget.txt", "w") as file:
                file.write(str(budget))
            
            print("Salaries paid successfully.")
        except FileNotFoundError:
            print("No employees found.")
        except ValueError:
            print("Invalid data found in files.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def record_expense(self):
        try:
            expense = int(input("Enter the expense amount: "))
            with open("budget.txt", "r") as file:
                budget = int(file.read())
            budget -= expense
            with open("budget.txt", "w") as file:
                file.write(str(budget))
            print("Expense recorded successfully. budget.txt updated")
        except ValueError:
            print("Invalid input! Please enter a valid number for the expense.")

    def record_income(self):
        try:
            income = int(input("Enter the income amount: "))
            with open("budget.txt", "r") as file:
                budget = int(file.read())
            budget += income
            with open("budget.txt", "w") as file:
                file.write(str(budget))
            print("Income recorded successfully. budget.txt updated")
        except ValueError:
            print("Invalid input! Please enter a valid number for the income.")

    def exit_program(self):
        self.running = False
        print("Program Terminated !!")


company = Company("Deens")
company.program()
