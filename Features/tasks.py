import main

# Everything related to tasks (add, remove, update, view, complete)

# Here I store the task name, the notes according to tasks (details about the task),
# priority levels (high, medium, low or none), completion status and date created.

# I could filter completed tasks but that is for later.

def tasks_menu():
    while True:
        tasks_menu_choices = input("Welcome to the Tasks feature! Please select an option: \n1. Add Task\n2. Remove Task\n3. Update Task\n4. View Tasks\n5. Exit\n")
        if tasks_menu_choices not in ['1', '2', '3', '4', '5']:
            print("Invalid choice. Please try again.")
            continue
        break
    while True:
        if tasks_menu_choices == '1':
            add_task()
        elif tasks_menu_choices == '2':
            remove_task()
        elif tasks_menu_choices == '3':
            update_task()
        elif tasks_menu_choices == '4':
            view_tasks()
        elif tasks_menu_choices == '5':
            print("Exiting the Tasks feature. Returning to main menu.")
            return

tasks_list = []

def add_task():
    add_task_response = input(
        "Do you want to add a task? (y/n): "
    ).lower()
    if add_task_response == "n":
        print("Returning to tasks menu.")
        return
    if add_task_response == "y":
        while True:
            task_name = input("Enter the task name: ").strip()
            if task_name == "":
                print("Please write a name for your task.")
                continue
            break
        task_desc = input(
            "Enter the task description (Can be left blank): "
        ).strip()
        while True:
            task_priority = input(
                "Enter the task priority (high/medium/low): "
            ).lower().strip()
            if task_priority not in ["high", "medium", "low"]:
                print("Please choose high, medium or low.")
                continue
            break
        tasks_list.append((task_name, task_desc, task_priority))
        print(
            f"Task added: {task_name}\n"
            f"Description: {task_desc}\n"
            f"Priority level: {task_priority}"
        )
    while True:
        retry_response = input("Do you want to add another task? (y/n): ").lower().strip()
        if retry_response == "y":
            print("Restarting function...")
            continue
        elif retry_response == "n":
            print("Returning to Tasks menu...")
            return



def remove_task():
    remove_task_response = input("Do you want to remove a task? (y/n): ")
    if not tasks_list:
        print("No tasks to remove.\nReturning to Tasks menu.")
        return
    if remove_task_response.lower() == "y":
        print("Here are the tasks you have:")
        for i, task in enumerate(tasks_list):
            print(f"{i + 1}. {task[0]} - {task[1]} - {task[2]}")
        while True:
            try:
                task_index = int(
                    input("Enter the number of the task you want to remove: ")
                ) - 1
            except ValueError:
                print("Please enter a valid task number.")
                continue
            if 0 <= task_index < len(tasks_list):
                break
            print("Invalid task number.")
        removed_task = tasks_list.pop(task_index)
        print(f"Task removed: {removed_task[0]}")
        while True:
            retry_response = input("Do you want to remove another task? (y/n): ").lower().strip()
            if retry_response == "y":
                print("Restarting function...")
                continue
            elif retry_response == "n":
                print("Returning to Tasks menu...")
                return
    elif remove_task_response.lower() == "n":
        print("Returning to Tasks menu.")
        return


def update_task():
    update_task_response = input("Do you want to update a task? (y/n): ")
    if not tasks_list:
        print("No tasks to update.\nReturning to Tasks menu.")
        return
    if update_task_response.lower() == 'y':
        print("Here are the tasks you have:")
        for i, task in enumerate(tasks_list):
            print(f"{i + 1}. {task[0]} - {task[1]} - {task[2]}")
        while True:
            try:
                task_index = int(
                    input("Enter the number of the task you want to update: ")
                ) - 1
            except ValueError:
                print("Please enter a valid task number.")
                continue
            
            if 0 <= task_index < len(tasks_list):
                break
            
            print('Invalid task number.')  
        while True:
            task_name = input("Enter the new task name: ").strip()
            if task_name == "":
                print("Please write a name for your task.")
                continue
            break
        task_desc = input("Enter the new task description: ")
        task_priority = input(
            "Enter the new task priority (high/medium/low): "
        )
        tasks_list[task_index] = (
            task_name,
            task_desc,
            task_priority
        )
        print(
            f"Task added: {task_name}\n"
            f"Description: {task_desc}\n"
            f"Priority level: {task_priority}"
        )
        while True:
            retry_response = input("Do you want to update another task? (y/n): ").lower().strip()
            if retry_response == "y":
                print("Restarting function...")
                continue
            elif retry_response == "n":
                print("Returning to Tasks menu...")
                return
    elif update_task_response.lower() == 'n':
        print('Returning to Tasks menu')
        return


def view_tasks():
    if not tasks_list:
        print('No tasks available to view.\n Returning to Tasks menu.')
        return
    view_task_response = input("Do you want to view your tasks? (y/n): ")
    if view_task_response.lower() == 'n':
        print("Returning to Tasks menu.")
        return
    elif view_task_response.lower() == 'y':
        print("\n=== TASKS ===")
        
        for i, task in enumerate(tasks_list):
            print(
                f"\n{i + 1}. {task[0]}\n"
                f"    Description: {task[1]}"
                f"    Priority: {task[2]}"
            )
        print("\n=============")

tasks_menu()