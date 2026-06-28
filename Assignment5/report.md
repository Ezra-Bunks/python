# Student Record Management System Report

## 1. Program Design

The Student Record Management System is built using Object-Oriented Programming (OOP) principles, separating concerns into two primary classes:

*   **`Student` Class:** Represents a single student record, encapsulating attributes like registration number, name, age, grade, address, contact, and program. It includes methods to convert student data to CSV row format (`to_csv_row`) and JSON dictionary format (`to_json_data`), and a static method to create a Student object from a CSV row (`from_csv_row`).

*   **`StudentManagementSystem` Class:** Manages a collection of `Student` objects. It handles file input/output (CSV for basic data, JSON for additional details), user interaction through a menu-driven interface, and orchestrates CRUD (Create, Read, Update, Delete) operations. This class is responsible for the overall application logic and persistence.

The application's entry point is `main.py`, which initializes and runs the `StudentManagementSystem`.

## 2. Key Functions

The `StudentManagementSystem` class provides the following core functionalities:

*   **`_load_data()`:** Reads student records from `students.csv` and `students.json` into memory upon system startup.
*   **`_save_data()`:** Writes all current student records from memory back to `students.csv` and `students.json` after any modification.
*   **`add_student()`:** Prompts the user for new student details, creates a `Student` object, and adds it to the system.
*   **`view_all_students()`:** Displays all student records currently in the system.
*   **`search_student()`:** Finds and displays details of a student using their registration number.
*   **`update_student()`:** Modifies details of an existing student identified by their registration number.
*   **`delete_student()`:** Removes a student record from the system using their registration number.
*   **`run()`:** Implements the main interactive command-line interface (CLI) loop, presenting a menu and executing chosen operations.

## 3. Exception Handling Strategy

The system incorporates `try-except` blocks to manage potential errors gracefully, ensuring robustness and providing user feedback.

*   **`StudentNotFoundException` (Custom Exception):** Raised when an operation (search, update, delete) is attempted on a student registration number that does not exist. This provides specific error context.
*   **`ValueError`:** Catches errors related to invalid data types during input (e.g., non-numeric age/grade) or malformed CSV rows during loading.
*   **`FileNotFoundError`:** Handled during data loading to allow the system to start with an empty state if data files are missing.
*   **`json.JSONDecodeError`:** Catches errors when parsing malformed JSON data.
*   **General `Exception`:** Catches any other unexpected errors during file operations or CRUD actions, ensuring the program doesn't crash abruptly.

All significant events, warnings, and errors are recorded in `student_system.log` using Python's `logging` module, providing a detailed audit trail without cluttering the console output.

## 4. Testing Results (Conceptual)

Conceptual testing confirms the system's adherence to requirements:

*   **Persistence:** Adding, updating, or deleting students correctly modifies `students.csv` and `students.json`. Restarting the application loads the latest data.
*   **CRUD Operations:** All add, view, search, update, and delete functions work as expected for existing and new records.
*   **Error Handling:**
    *   Attempting to add a student with an existing registration number results in an error message.
    *   Searching for a non-existent student raises `StudentNotFoundException`, caught and reported to the user.
    *   Providing non-numeric input for age or grade triggers `ValueError`.
    *   Missing `students.csv` or `students.json` files are handled, and the system starts with no data.
    *   Malformed data in CSV/JSON files is logged as a warning, and the system attempts to continue processing valid records.
*   **Logging:** The `student_system.log` file is generated and populated with system initialization messages, user actions, warnings (e.g., non-existent student operations, invalid menu choices), and errors.
*   **User Interface:** The menu-driven CLI is interactive, prompts for necessary input, and provides clear feedback.
