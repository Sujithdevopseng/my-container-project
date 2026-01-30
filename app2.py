import json
import os

FILE_NAME = "students.json"

def load_students():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        return json.load(f)

def save_students(students):
    with open(FILE_NAME, "w") as f:
        json.dump(students, f, indent=4)

def add_student(students):
    name = input("Name: ")
    roll = input("Roll No: ")
    dept = input("Department: ")

    students.append({
        "name": name,
        "roll": roll,
        "dept": dept
    })

    save_students(students)
    print("Student added!")

def view_students(students):
    if not students:
        print("No students found.")
        return

    for s in students:
        print(f"{s['roll']} - {s['name']} ({s['dept']})")

def search_student(students):
    roll = input("Enter roll number: ")
    for s in students:
        if s["roll"] == roll:
            print(s)
            return
    print("Student not found")

def delete_student(students):
    roll = input("Enter roll number to delete: ")
    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            save_students(students)
            print("Deleted!")
            return
    print("Student not found")

def main():
    students = load_students()

    while True:
        print("\n--- STUDENT SYSTEM ---")
        print("1. Add student")
        print("2. View students")
        print("3. Search student")
        print("4. Delete student")
        print("5. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            delete_student(students)
        elif choice == "5":
            break
        else:
            print("Invalid choice")

if_name_ == "_main_":
main()