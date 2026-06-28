class ContactManager:
    def __init__(self):
        self.contacts = {}
    def add_contact(self, name: str, phone: str):
        self.contacts[name] = phone
    def get_contact(self, name: str):
        return self.contacts.get(name, "Not found")

if __name__ == "__main__":
    cm = ContactManager()
    cm.add_contact("Alice", "123-456-7890")
    print("Alice's phone:", cm.get_contact("Alice"))
