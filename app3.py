import os

FILE_NAME = "passwords.txt"
MASTER_PASSWORD = "admin123"

def authenticate():
    pwd = input("Enter master password: ")
    return pwd == MASTER_PASSWORD

def add_password():
    site = input("Website: ")
    username = input("Username: ")
    password = input("Password: ")

    with open(FILE_NAME, "a") as f:
        f.write(f"{site}|{username}|{password}\n")

    print("Saved successfully!")

def view_passwords():
    if not os.path.exists(FILE_NAME):
        print("No data found")
        return

    with open(FILE_NAME, "r") as f:
        for line in f:
            site, user, pwd = line.strip().split("|")
            print(f"Site: {site}, User: {user}, Pass: {pwd}")

def main():
    if not authenticate():
        print("Wrong password!")
        return

    while True:
        print("\n--- PASSWORD MANAGER ---")
        print("1. Add password")
        print("2. View passwords")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_password()
        elif choice == "2":
            view_passwords()
        elif choice == "3":
            break
        else:
            print("Invalid choice")

if_name_ == "_main_":
main()