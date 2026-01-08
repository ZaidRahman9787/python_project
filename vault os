import json
import os

FILE = "database.json"


def open_json():
    if os.path.exists(FILE):
        pass
    else:
        with open(FILE, "w") as f:
            json.dump([], f)


def read_json():
    with open(FILE, "r") as f:
        return json.load(f)


def add_element(username, password):
    data = read_json()
    data.append({
        "username": username,
        "password": password
    })
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)


def delete_element(index):
    data = read_json()
    data.pop(index)
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)


def update_element(index, new_password):
    data = read_json()
    data[index]["password"] = new_password
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)


def show_data():
    data = read_json()
    if len(data) == 0:
        print("No data")
    else:
        for i in range(len(data)):
            print(i + 1, data[i]["username"], data[i]["password"])


open_json()

while True:
    print("\n1. View")
    print("2. Add")
    print("3. Update")
    print("4. Delete")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "1":
        show_data()

    elif choice == "2":
        u = input("Username: ")
        p = input("Password: ")
        add_element(u, p)
        print("Added")

    elif choice == "3":
        show_data()
        idx = int(input("Select number: ")) - 1
        new_p = input("New password: ")
        update_element(idx, new_p)
        print("Updated")

    elif choice == "4":
        show_data()
        idx = int(input("Select number: ")) - 1
        delete_element(idx)
        print("Deleted")

    elif choice == "5":
        break

    else:
        print("Invalid option")
