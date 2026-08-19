from datetime import datetime, date

# So as of now I still don't know how to manipulate dates, I still am figuring out how I will proceed to manage these deadlines.

def deadlines_menu():
    while True:
        deadlines_choice = input('Welcome to the Deadlines menu! Please choose an option: \n1. Add deadline\n2. Remove deadline\n3. Update deadline\n4. View all deadlines\n5. Complete deadline\n6. Exit\n')
        if deadlines_choice not in ['1', '2', '3', '4', '5', '6']:
            print("Invalid choice. Please try again.")
            return
        elif deadlines_choice == '1':
            add_deadline()
        elif deadlines_choice == '2':
            remove_deadline()
        elif deadlines_choice == '3':
            update_deadline()
        elif deadlines_choice == '4':
            view_deadlines()
        elif deadlines_choice == '5':
            complete_deadline()
        elif deadlines_choice == '6':
            print('Exiting the Deadlines menu. Returning to main menu...')
            return
        
deadlines_list = []

def add_deadline():
    add_deadline_choice = input("Do you want to add a deadline ? (y/n): ").lower()
    if add_deadline_choice == 'n':
        print('Returning to Deadlines menu...')
        return
    if add_deadline_choice == 'y':
        while True:
            deadline_name = input("Enter the deadline name: ").strip()
            if deadline_name == '':
                print('Please write a name for your deadline.')
                continue
            break
        deadline_description = input(
                    "Enter the task description (Can be left blank): "
                ).strip()
        while True:
            deadline_priority = input("Enter the deadline priority (high/medium/low): ").lower().strip()
            if deadline_priority not in ["high", "medium", "low"]:
                print('Please choose high, medium or low.')
                continue
            break
        while True:
            deadline_due_date = input(
                "Enter the due date of this deadline (YYYY/MM/DD): "
            ).strip()
            try:
                due_date = datetime.strptime(
                    deadline_due_date,
                    "%Y/%m/%d"
                ).date()
            except ValueError:
                print("Please enter a valid date using YYYY/MM/DD.")
                continue
            break
        remaining_days = (due_date - date.today()).days
        today = date.today()
        if due_date < today:
            status = f"Overdue by {remaining_days} days"
        elif due_date == today:
            status = "Due today"
        else:
            status = f"Pending - {remaining_days} days remaining"
    deadlines_list.append((deadline_name, deadline_priority, deadline_description, due_date))
    print(
        f"\nDeadline added successfully!\n"
        f"Deadline added: {deadline_name}\n"
        f"Priority level: {deadline_priority}\n"
        f"Description: {deadline_description}\n"
        f"Due date: {due_date}\n"
        f"Status: {status}"
    )
    retry_response = input('Do you want to add another deadline ? (y/n): ').lower().strip()
    while True:
        if retry_response == "y":
            print("Restarting...")
            continue
        elif retry_response == "n":
            print("Returning to Deadlines menu...")
            return

def remove_deadline():
    remove_deadline_choice = input('Do you want to remove a deadline ? (y/n): ').strip().lower()
    if not deadlines_list:
        print("No deadlines available. Returning to Deadlines menu...")
        return
    if remove_deadline_choice == 'n':
        print('Returning to Deadlines menu...')
        return
    if remove_deadlines_choice == 'y':
        print('Here are the deadlines you have...')
        for i, deadline in enumerate(deadlines_list):
            print(
                f"{i + 1}. {deadline[0]}\n"
                f"    Priority: {deadline[1]}\n"
                f"    Description: {deadline[2]}\n"
                f"    Due date: {deadline[3]}\n"
                f"    Status:{deadline[4]}"
            )
        while True:
            try:
                deadline_index = int(input("Enter the number of the deadline you want to remove: ")) - 1
            except ValueError:
                print('Please enter a valid deadline number.')
                continue
            if 0 <= deadline_index < len(deadline_index):
                break
            print("Invalid deadline number.")
        removed_deadline = deadlines_list.pop(deadline_index)
        print(f"Deadline removed: {removed_deadline[0]}")
        while True:
            retry_response = input('Do you want to remove another deadline ? (y/n): ').lower().strip()
            if retry_response == 'y':
                print('Restarting...')
                continue
            elif retry_response =='n':
                print("Returning to Deadlines menu...")
                return

def update_deadline():
    pass

def view_deadlines():
    pass


def complete_deadline():
    pass

