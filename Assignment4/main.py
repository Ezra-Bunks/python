"""
Course: BSE2302	PROFESSIONAL SOFTWARE ENGINEERING MINI PRACTICAL PROJECT II
Assignment3: Contact Manager
Name: Mukisa Ben Ezra
RegNo: 24/U/21328
Date: June 18, 2026
"""

class ContactManager:

    def __init__(self):
        self.contacts = []


    # Validation Methods

    def validate_phone(self, phone):
        allowed = "+-0123456789"

        for char in phone:
            if char not in allowed:
                return False

        return True

    def validate_email(self, email):
        if email == "":
            return True

        return "@" in email and "." in email


    # CRUD Methods

    def add_contact(self, name, phone, email=""):

        if not self.validate_phone(phone):
            print("Error: Invalid phone number.")
            return

        if not self.validate_email(email):
            print("Error: Invalid email address.")
            return

        contact = {
            "name": name,
            "phone": phone,
            "email": email
        }

        self.contacts.append(contact)
        print("Contact added successfully.")

    def view_contact(self, name):

        for contact in self.contacts:
            if contact["name"].lower() == name.lower():

                print("\nContact Found")
                print("---------------------")
                print("Name :", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])

                return

        print("Contact not found.")

    def update_contact(self, name, new_phone, new_email=""):

        if not self.validate_phone(new_phone):
            print("Error: Invalid phone number.")
            return

        if not self.validate_email(new_email):
            print("Error: Invalid email address.")
            return

        for contact in self.contacts:

            if contact["name"].lower() == name.lower():

                contact["phone"] = new_phone
                contact["email"] = new_email

                print("Contact updated successfully.")
                return

        print("Contact not found.")

    def delete_contact(self, name):

        for contact in self.contacts:

            if contact["name"].lower() == name.lower():
                self.contacts.remove(contact)
                print("Contact deleted successfully.")
                return

        print("Contact not found.")


    # Search Methods

    def search_contacts(self, keyword):

        results = []

        for contact in self.contacts:

            if (
                keyword.lower() in contact["name"].lower()
                or keyword.lower() in contact["phone"].lower()
                or keyword.lower() in contact["email"].lower()
            ):
                results.append(contact)

        if len(results) == 0:
            print("No matching contacts found.")
            return

        print("\nSearch Results")
        print("=" * 40)

        for contact in results:
            print(f"Name : {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print("-" * 40)


    # List All Contacts

    def list_contacts(self):

        if len(self.contacts) == 0:
            print("No contacts available.")
            return

        print("\nAll Contacts")
        print("=" * 40)

        for contact in self.contacts:
            print(f"Name : {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print("-" * 40)



def main():

    manager = ContactManager()

    while True:

        print("\n=== Contact Manager Menu ===")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Search Contacts")
        print("6. List All Contacts")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == "1":

            name = input("Enter Name: ")
            phone = input("Enter Phone Number: ")
            email = input("Enter Email (optional): ")

            manager.add_contact(name, phone, email)

        elif choice == "2":

            name = input("Enter Name to View: ")
            manager.view_contact(name)

        elif choice == "3":

            name = input("Enter Name to Update: ")
            phone = input("Enter New Phone Number: ")
            email = input("Enter New Email: ")

            manager.update_contact(name, phone, email)

        elif choice == "4":

            name = input("Enter Name to Delete: ")
            manager.delete_contact(name)

        elif choice == "5":

            keyword = input("Enter Search Keyword: ")
            manager.search_contacts(keyword)

        elif choice == "6":

            manager.list_contacts()

        elif choice == "7":

            print("Thank you for using Contact Manager.")
            break

        else:
            print("Invalid choice. Please choose between 1 and 7.")


if __name__ == "__main__":
    main()