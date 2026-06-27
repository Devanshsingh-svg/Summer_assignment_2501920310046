class StudentRecord:
    def __init__(self):
        self.records = {}
    def add_student(self, roll: int, name: str):
        self.records[roll] = name
    def view_records(self):
        return self.records

if __name__ == "__main__":
    sr = StudentRecord()
    sr.add_student(1, "Alice")
    sr.add_student(2, "Bob")
    print(f"Student Records: {sr.view_records()}")
