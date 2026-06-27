class EmployeeManagement:
    def __init__(self):
        self.employees = {}
    def add_employee(self, emp_id: int, name: str):
        self.employees[emp_id] = name
    def view_employees(self):
        return self.employees

if __name__ == "__main__":
    em = EmployeeManagement()
    em.add_employee(101, "John")
    print(f"Employees: {em.view_employees()}")
