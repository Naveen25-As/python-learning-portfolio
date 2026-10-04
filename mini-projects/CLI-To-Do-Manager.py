# CLI To-Do Manager.

import json
import os

FILE = "tasks.json"


def load_tasks():
    if os.path.exists(FILE):
        with open(FILE, "r") as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    with open(FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks):
    title = input("Enter task: ")

    task = {
        "title": title,
        "completed": False
    }

    tasks.append(task)
    save_tasks(tasks)

    print("Task added successfully.")


def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    print("\n===== Tasks =====")

    for index, task in enumerate(tasks, 1):
        status = "✓" if task["completed"] else " "
        print(f"{index}. [{status}] {task['title']}")


def complete_task(tasks):
    view_tasks(tasks)

    try:
        number = int(input("Enter task number: "))

        if 1 <= number <= len(tasks):
            tasks[number - 1]["completed"] = True
            save_tasks(tasks)
            print("Task completed.")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a number.")


def delete_task(tasks):
    view_tasks(tasks)

    try:
        number = int(input("Enter task number: "))

        if 1 <= number <= len(tasks):
            tasks.pop(number - 1)
            save_tasks(tasks)
            print("Task deleted.")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a number.")


def main():
    tasks = load_tasks()

    while True:
        print("\n===== TO-DO MANAGER =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()