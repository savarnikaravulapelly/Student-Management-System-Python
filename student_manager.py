import os

FILE_NAME = "students.txt"


def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    dept = input("Enter department: ")

    with open(FILE_NAME, "a") as f:
        f.write(f"{roll},{name},{dept}\n")

    print("✅ Student added successfully\n")


def view_students():
    if not os.path.exists(FILE_NAME):
        print("No records found.\n")
        return

    with open(FILE_NAME, "r") as f:
        records = f.readlines()

    print("\n📋 Student Records:")
    for record in records:
        roll, name, dept = record.strip().split(",")
        print(f"Roll: {roll} | Name: {name} | Dept: {dept}")
    print()


def search_student():
    roll_search = input("Enter roll number to search: ")

    with open(FILE_NAME, "r") as f:
        for line in f:
            roll, name, dept = line.strip().split(",")
            if roll == roll_search:
                print(f"Found → {name} ({dept})\n")
                return

    print("Student not found.\n")


def menu():
    while True:
        print("===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice\n")


menu()
