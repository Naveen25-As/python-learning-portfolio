# To-Do List.

tasks = []


def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added!")


def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("\n--- Tasks ---")

    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


def delete_task():
    view_tasks()

    try:
        number = int(input("Enter task number to delete: "))

        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            print(f"Deleted: {removed}")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a number.")


while True:
    print("\n===== To-Do List =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        break
    else:
        print("Invalid choice.")