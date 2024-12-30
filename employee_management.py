import json

def save_employees(employees):
    with open("employees.json", "w") as file:
        json.dump(employees, file)

class Employee:
    def __init__(self, name, id, salary, department):
        self.name = name
        self.id = id
        self.salary = salary
        self.department = department

    def display_employee(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.id}")
        print(f"Salary: {self.salary}")
        print(f"Department: {self.department}")


employee1 = Employee("John Doe", 1, 50000, "HR")
employee2 = Employee("Jane Smith", 2, 60000, "Finance")

employee1.display_employee()
employee2.display_employee()

def save_employees(employees):
    with open("employees.json", "w") as file:
        json.dump(employees, file)

employees = [employee1.__dict__, employee2.__dict__]
save_employees(employees)

def load_employees():
    with open("employees.json", "r") as file:
        return json.load(file)

loaded_employees = load_employees()
for emp in loaded_employees:
    print(emp)

def add_employee():
    name = input("Enter employee name: ")
    id = input("Enter employee ID: ")
    salary = input("Enter employee salary: ")
    department = input("Enter employee department: ")
    return Employee(name, id, salary, department)

employee3 = add_employee()
employee3.display_employee()
