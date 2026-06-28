import csv
import json

# --- Configuration ---
CSV_FILE = 'students.csv'
JSON_FILE = 'students.json'

# --- Student Class ---
class Student:
    """Represents a single student record."""

    def __init__(self, reg_no, name, age, grade, address="", contact="", program=""):
        self.reg_no = reg_no
        self.name = name
        self.age = age
        self.grade = grade
        self.address = address
        self.contact = contact
        self.program = program

    def __str__(self):
        """Returns a user-friendly string representation of the student."""
        return (f"Reg No: {self.reg_no}\n"
                f"  Name: {self.name}\n"
                f"  Age: {self.age}\n"
                f"  Grade: {self.grade}\n"
                f"  Address: {self.address if self.address else 'N/A'}\n"
                f"  Contact: {self.contact if self.contact else 'N/A'}\n"
                f"  Program: {self.program if self.program else 'N/A'}\n"
                f"--------------------")

    def to_csv_row(self):
        """Returns basic student details as a list for CSV."""
        return [self.reg_no, self.name, self.age, self.grade]

    def to_json_data(self):
        """Returns additional student details as a dictionary for JSON."""
        return {
            "reg_no": self.reg_no,
            "address": self.address,
            "contact": self.contact,
            "program": self.program
        }

    @staticmethod
    def from_csv_row(row):
        """Creates a Student object from a CSV row."""
        # Basic type conversion, will raise ValueError if data is not convertible
        reg_no, name, age, grade = row
        return Student(reg_no, name, int(age), float(grade))

    def update_from_json_data(self, json_data):
        """Updates student's additional details from JSON data."""
        self.address = json_data.get("address", self.address)
        self.contact = json_data.get("contact", self.contact)
        self.program = json_data.get("program", self.program)


# --- StudentManagementSystem Class ---
class StudentManagementSystem:
    """Manages student records, including file operations."""

    def __init__(self, csv_file=CSV_FILE, json_file=JSON_FILE):
        self.csv_file = csv_file
        self.json_file = json_file
        self.students = {}  # Dictionary to store Student objects: {reg_no: Student_object}
        self._load_data()

    def _load_data(self):
        """Loads student data from CSV and JSON files."""
        try:
            with open(self.csv_file, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header row
                for row in reader:
                    try:
                        student = Student.from_csv_row(row)
                        self.students[student.reg_no] = student
                    except ValueError:
                        print(f"Skipping malformed CSV row: {row}")
        except FileNotFoundError:
            print(f"CSV file '{self.csv_file}' not found. Starting with no basic student data.")
        except Exception as e:
            print(f"Error loading basic student data: {e}")

        try:
            with open(self.json_file, mode='r', encoding='utf-8') as file:
                json_data_list = json.load(file)
                for json_data in json_data_list:
                    reg_no = json_data.get("reg_no")
                    if reg_no and reg_no in self.students:
                        self.students[reg_no].update_from_json_data(json_data)
                    elif reg_no:
                        print(f"Warning: Student with Reg No {reg_no} found in JSON but not CSV. Skipping JSON details.")
        except FileNotFoundError:
            print(f"JSON file '{self.json_file}' not found. Starting with no additional student data.")
        except json.JSONDecodeError as e:
            print(f"Error decoding additional student data from '{self.json_file}': {e}")
        except Exception as e:
            print(f"Error loading additional student data: {e}")
        print("Data loading complete.")

    def _save_data(self):
        """Saves all student data back to CSV and JSON files."""
        try:
            with open(self.csv_file, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['reg_no', 'name', 'age', 'grade']) # Write header
                for student in self.students.values():
                    writer.writerow(student.to_csv_row())
        except Exception as e:
            print(f"Error saving basic student data: {e}")

        try:
            json_data_list = [student.to_json_data() for student in self.students.values()]
            with open(self.json_file, mode='w', encoding='utf-8') as file:
                json.dump(json_data_list, file, indent=4)
        except Exception as e:
            print(f"Error saving additional student data: {e}")
        print("Data saving complete.")

    def add_student(self):
        """Prompts for student details and adds a new student."""
        print("\n--- Add New Student ---")
        try:
            reg_no = input("Enter Registration Number: ").strip().upper()

            if reg_no in self.students:
                print(f"Error: Student with Registration Number '{reg_no}' already exists.")
                return

            name = input("Enter Name: ").strip()
            if not name:
                print("Error: Name cannot be empty.")
                return

            age = int(input("Enter Age: "))
            grade = float(input("Enter Grade: "))

            address = input("Enter Address (optional): ").strip()
            contact = input("Enter Contact (optional): ").strip()
            program = input("Enter Program (optional): ").strip()

            new_student = Student(reg_no, name, age, grade, address, contact, program)
            self.students[reg_no] = new_student
            self._save_data()
            print(f"Student '{name}' (Reg No: {reg_no}) added successfully.")

        except ValueError as e:
            print(f"Input Error: Please enter valid numbers for Age and Grade. ({e})")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def view_all_students(self):
        """Displays all student records."""
        print("\n--- All Student Records ---")
        if not self.students:
            print("No student records available.")
            return

        for student in self.students.values():
            print(student)
        print("---------------------------")

    def search_student(self):
        """Searches for a student by registration number and displays details."""
        print("\n--- Search Student ---")
        reg_no = input("Enter Registration Number to search: ").strip().upper()

        if reg_no not in self.students:
            print(f"Search Error: Student with Registration Number '{reg_no}' not found.")
            return

        student = self.students[reg_no]
        print("\n--- Student Found ---")
        print(student)

    def update_student(self):
        """Updates details of an existing student."""
        print("\n--- Update Student ---")
        try:
            reg_no = input("Enter Registration Number of student to update: ").strip().upper()

            if reg_no not in self.students:
                print(f"Update Error: Student with Registration Number '{reg_no}' not found.")
                return

            student = self.students[reg_no]
            print(f"Current details for {student.name} (Reg No: {reg_no}):")
            print(student)

            print("\nEnter new details (leave blank to keep current value):")
            new_name = input(f"New Name ({student.name}): ").strip()
            if new_name:
                student.name = new_name

            new_age_str = input(f"New Age ({student.age}): ").strip()
            if new_age_str:
                student.age = int(new_age_str)

            new_grade_str = input(f"New Grade ({student.grade}): ").strip()
            if new_grade_str:
                student.grade = float(new_grade_str)

            new_address = input(f"New Address ({student.address if student.address else 'N/A'}): ").strip()
            if new_address:
                student.address = new_address

            new_contact = input(f"New Contact ({student.contact if student.contact else 'N/A'}): ").strip()
            if new_contact:
                student.contact = new_contact

            new_program = input(f"New Program ({student.program if student.program else 'N/A'}): ").strip()
            if new_program:
                student.program = new_program

            self._save_data()
            print(f"Student '{student.name}' (Reg No: {reg_no}) updated successfully.")

        except ValueError as e:
            print(f"Input Error: Please enter valid numbers for Age and Grade. ({e})")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def delete_student(self):
        """Deletes a student record by registration number."""
        print("\n--- Delete Student ---")
        reg_no = input("Enter Registration Number of student to delete: ").strip().upper()

        if reg_no not in self.students:
            print(f"Delete Error: Student with Registration Number '{reg_no}' not found.")
            return

        student_name = self.students[reg_no].name
        del self.students[reg_no]
        self._save_data()
        print(f"Student '{student_name}' (Reg No: {reg_no}) deleted successfully.")

    def run(self):
        """Main menu-driven loop for the Student Management System."""
        print("Welcome to the Student Record Management System!")

        while True:
            print("\n=== Main Menu ===")
            print("1. Add New Student")
            print("2. View All Students")
            print("3. Search Student")
            print("4. Update Student Details")
            print("5. Delete Student Record")
            print("6. Exit")

            choice = input("Enter your choice (1-6): ").strip()

            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.view_all_students()
            elif choice == '3':
                self.search_student()
            elif choice == '4':
                self.update_student()
            elif choice == '5':
                self.delete_student()
            elif choice == '6':
                print("Exiting Student Management System. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
