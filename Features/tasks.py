import main

# Everything related to tasks (add, remove, update, view, complete)

# Here I store the task name, the notes according to tasks (details about the task),
# priority levels (high, medium, low or none), completion status and date created.

# I could filter completed tasks but that is for later.

def tasks_menu():
    while True:
        input("Welcome to the Tasks feature! Please select an option: \n1. Add Task\n2. Remove Task\n3. Update Task\n4. View Tasks\n5. Exit\n")
        tasks_menu_choices = input(f"Enter your choice (1-5): ")
        if tasks_menu_choices not in ['1', '2', '3', '4', '5']:
            print("Invalid choice. Please try again.")
            tasks_menu()
        elif tasks_menu_choices == '1':
            add_task()
        elif tasks_menu_choices == '2':
            remove_task()
        elif tasks_menu_choices == '3':
            update_task()
        elif tasks_menu_choices == '4':
            view_tasks()
        elif tasks_menu_choices == '5':
            print("Exiting the Tasks feature. Returning to main menu.")
            main.slm_main_menu()

tasks_list = []

def add_task():
    input("Do you want to add a task? (y/n): ")
    if input().lower() == 'y':
        task_name = input("Enter the task name: ")
        task_desc = input("Enter the task description: ")
        task_priority = input("Enter the task priority (high/medium/low): ")
        tasks_list.append((task_name, task_desc, task_priority))
        print(f"Task added: {task_name}\n Description: {task_desc}\n Priority level: {task_priority}\n")
    elif input().lower() == 'n':
        print("Returning to main menu.")
        main.slm_main_menu()


def remove_task():
    input("Do you want to remove a task? (y/n): ")
    if input().lower() == 'y':
        task_name = input("Enter the task name: ")
        for i, task in enumerate(tasks_list):
            if task[0] == task_name:
                tasks_list.pop(i)
                print(f"Task removed: {task_name}")
        else:
            print("Task not found.")
    elif input().lower() == 'n':
        print("Returning to main menu.")
        main.slm_main_menu()


def update_task():
    input("Do you want to update a task? (y/n): ")
    if input().lower() == 'y':
        #Show the list of tasks to user, it's more user friendly if they can see and pick a number
        print("Here are the tasks you have:")
        for i, task in enumerate(tasks_list):
            print(f"{i + 1}. {task[0]} - {task[1]} - {task[2]}")
        task_index = int(input("Enter the number of the task you want to update: ")) - 1
        if 0 <= task_index < len(tasks_list):
            task_name = input("Enter the new task name: ")
            task_notes = input("Enter the new task notes: ")
            task_priority = input("Enter the new task priority (high/medium/low): ")
            tasks_list[task_index] = (task_name, task_notes, task_priority)
            print(f"Task updated: {task_name}")
        else:
            print("Invalid task number.")


def view_tasks():
    input("Do you want to view your tasks? (y/n): ")
    if input().lower() == 'n':
        print("Returning to main menu.")
        main.slm_main_menu()
    elif input().lower() == 'y':
        if not tasks_list:
            print("No tasks found.")
        else:
            print(tasks_list)
