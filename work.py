import os
print("Welcome back, user!")

if os.path.exists("tasks.txt"):
    with open("tasks.txt", "r") as file:
        tasks = [line.strip() for line in file.readlines()]

tasks = []

def show_menu():
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Clear All Tasks")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == '1':
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added.")
    elif choice == '2':
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    elif choice == '3':
        task_num = int(input("Enter task number to delete: "))
        if 0 < task_num <= len(tasks):
            tasks.pop(task_num - 1)
            print("Task deleted.")
        else:
            print("Invalid task number.")
    elif choice == '4':
        tasks.clear()
        print("All tasks cleared.")
    elif choice == '5':
        break

    else:
        print("Invalid choice.")
print('Hello from me\!')
