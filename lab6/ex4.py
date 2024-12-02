class Employee:
    def __init__(self, employee_id, salary=0):
        self.salary = salary
        self.employee_id = employee_id

    def work(self):
        print("Come to office")

class Manager(Employee):
    def __init__(self, employee_id, salary=0):
        super().__init__(employee_id, salary)

    def work(self):
        print(f"Employer {self.employee_id} : Manage employees")

    def assign_task(self, task):
        print(f"Employer {self.employee_id} : Assigned task {task}")

class Engineer(Employee):
    def __init__(self, employee_id, salary=0):
        super().__init__(employee_id, salary)

    def work(self):
        print(f"Employer {self.employee_id} : Developing software")

    def assigned_project(self, project):
        print(f"Employer {self.employee_id} : Assigned to project {project}")

class Salesperson(Employee):
    def __init__(self, employee_id, salary=0):
        super().__init__(employee_id, salary)

    def work(self):
        print(f"Employer {self.employee_id} : Sell products")

    def make_sale(self, product):
        print(f"Employer {self.employee_id} : Sold product {product}")

employee = Employee(101, 3000)
manager = Manager(102, 5000)
engineer = Engineer(103, 4000)
salesperson = Salesperson(104, 3500)

print("Employee:")
employee.work()

print("\nManager:")
manager.work()
manager.assign_task("Organize team meeting")

print("\nEngineer:")
engineer.work()
engineer.assigned_project("AI Research")

print("\nSalesperson:")
salesperson.work()
salesperson.make_sale("Laptop")
