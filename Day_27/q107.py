class SalaryManagement:
    def __init__(self):
        self.salaries = {}
    def set_salary(self, emp_id: int, salary: float):
        self.salaries[emp_id] = salary
    def get_salary(self, emp_id: int):
        return self.salaries.get(emp_id, 0.0)

if __name__ == "__main__":
    sm = SalaryManagement()
    sm.set_salary(101, 50000.0)
    print(f"Employee 101 Salary: {sm.get_salary(101)}")
