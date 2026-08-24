from datetime import datetime, date

# So as of now I still don't know how to manipulate dates, I still am figuring out how I will proceed to manage these deadlines.
deadlines_list = []

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
        
def get_deadline_status(due_date):
    today = date.today()
    remaining_days = (due_date - today).days
    if due_date < today:
        return f"Overdue by {abs(remaining_days)} day(s)."
    if due_date == today:
        return "Due today."
    return f"Pending - {remaining_days} day(s) remaining."

def ask_for_due_date(prompt):
    while True:
        deadline_due_date = input(prompt).strip()
        try:
            return datetime.strptime(deadline_due_date, "%Y/%m/%d").date()
        except ValueError:
            print('Please enter a valid date using YYYY/MM/DD.')


def add_deadline():
    while True:
        add_deadline_choice = input(
            "Do you want to add a deadline ? (y/n): "
        ).lower().strip()
        if add_deadline_choice == 'n':
            print("Returning to Deadlines menu...")
            return
        if add_deadlines_choice != 'y':
            print("Please answer (y)es or (n)o.")
            continue
        while True:
            deadline_name = input("Enter the name of your deadline").strip()
            if deadline_name == "":
                print("Please provide a name for your deadline.")
                continue
            break
        deadline_description = input(
            "Enter a description for your deadline (Can be left blank): "
        ).strip()
        while True:
            deadline_priority = input(
                "What's the priority of your deadline ? (high/medium/low): "
            ).lower().strip()
            if deadline_priority not in ["high", "medium", "low"]:
                print("Please choose high, medium or low.")
                continue
            break
        due_date = ask_for_due_date(
            "Enter the due date of this deadline (YYYY/MM/DD): "
        )
        deadlines_list.append(
            (deadline_name, deadline_priority, deadline_description, due_date)
        )
        status = get_deadline_status(due_date)
        print(
            "\nDeadline added successfully!\n"
            f"Name: {deadline_name}\n"
            f"Priority: {deadline_priority}\n"
            f"Description: {deadline_description}\n"
            f"Due date: {due_date}\n"
            f"Status: {status}"
        )
        while True:
            retry_response = input(
                "Do you want to add another deadline ? (y/n): "
            ).lower().strip()
            if retry_response == 'y':
                print("Restarting....")
                continue
            if retry_response == 'n':
                print("Returning to Deadlines menu...")
                return
            else:
                print("Please answer with 'y' or 'n'.")
                continue

def remove_deadline():
    if not deadlines_list:
        print("No deadlines available. Returning to Deadlines menu...")
        return
    remove_deadline_choice = input('Do you want to remove a deadline ? (y/n): ').strip().lower()
    if remove_deadline_choice == 'n':
        print('Returning to Deadlines menu...')
        return
    if remove_deadline_choice != 'y':
        print("Please answer with 'y' or 'no'.")
        continue
    
    while True:
        print("\n======== DEADLINES ========")
        for i, deadline in enumerate(deadlines_list, start=1):
            print(
                f"\n{i}. {deadline[0]}\n"
                f"    Priority: {deadline[1]}\n"
                f"    Description: {deadline[2]}\n"
                f"    Due date: {deadline[3]}"
            )
        print("\n===========================")
        while True:
            try:
                deadline_index = int(
                    input("Enter the number of the deadline you want to remove: ")
                ) - 1
            except ValueError:
                print("Please enter a valid deadline number.")
                continue
            
            if 0 <= deadline_index < len(deadlines_list):
                break
            print("Invalid deadline number") #does the user get to retry after this ?
        removed_deadline = deadlines_list.pop(deadline_index)
        print(f"Deadline removed successfully: {removed_deadline[0]}")
        
        while True:
            retry_response = input(
            "Do you want to remove another deadline ? (y/n): "
        ).lower().strip()
            if retry_response == 'y':
                print("Restarting...")
                continue
            if retry_response == 'n':
                print("Returning to Deadlines menu...")
                return
            else:
                print("Please answer with 'y' or 'n'.")
                continue

def update_deadline():
    if not deadlines_list:
        print("No deadlines to update.\nReturning to Deadlines menu...")
        return

    update_deadline_choice = input(
        "Do you want to update a deadline? (y/n): "
    ).lower().strip()

    if update_deadline_choice == "n":
        print("Returning to Deadlines menu...")
        return
    if update_deadline_choice != "y":
        print("Invalid response. Returning to Deadlines menu...")
        return

    while True:
        print("\n======== DEADLINES ========")
        for i, deadline in enumerate(deadlines_list, start=1):
            print(
                f"\n{i}. {deadline[0]}\n"
                f"    Priority: {deadline[1]}\n"
                f"    Description: {deadline[2]}\n"
                f"    Due date: {deadline[3]}"
            )
        print("\n===========================")

        while True:
            try:
                deadline_index = int(
                    input("Enter the number of the deadline you want to update: ")
                ) - 1
            except ValueError:
                print("Please enter a valid deadline number.")
                continue

            if 0 <= deadline_index < len(deadlines_list):
                break
            print("Invalid deadline number.")

        old_name, old_priority, old_description, old_due_date = deadlines_list[
            deadline_index
        ]

        new_name = input(
            f"Enter the new name (press Enter to keep '{old_name}'): "
        ).strip()
        if new_name == "":
            new_name = old_name

        new_description = input(
            "Enter the new description "
            "(press Enter to keep the current description): "
        ).strip()
        if new_description == "":
            new_description = old_description

        while True:
            new_priority = input(
                f"Enter the new priority (high/medium/low) "
                f"or press Enter to keep '{old_priority}': "
            ).lower().strip()

            if new_priority == "":
                new_priority = old_priority
                break
            if new_priority in ["high", "medium", "low"]:
                break
            print("Please choose high, medium or low.")

        while True:
            new_due_date_text = input(
                f"Enter the new due date (YYYY/MM/DD) "
                f"or press Enter to keep '{old_due_date}': "
            ).strip()

            if new_due_date_text == "":
                new_due_date = old_due_date
                break

            try:
                new_due_date = datetime.strptime(
                    new_due_date_text, "%Y/%m/%d"
                ).date()
                break
            except ValueError:
                print("Please enter a valid date using YYYY/MM/DD.")

        deadlines_list[deadline_index] = (
            new_name,
            new_priority,
            new_description,
            new_due_date,
        )

        print(
            "\nDeadline updated successfully!\n"
            f"Name: {new_name}\n"
            f"Priority: {new_priority}\n"
            f"Description: {new_description}\n"
            f"Due date: {new_due_date}\n"
            f"Status: {get_deadline_status(new_due_date)}"
        )

        retry_response = input(
            "Do you want to update another deadline? (y/n): "
        ).lower().strip()

        if retry_response == "y":
            print("Restarting...")
            continue
        if retry_response == "n":
            print("Returning to Deadlines menu...")
            return

        print("Invalid response. Returning to Deadlines menu...")
        return

def view_deadlines():
    def view_deadlines():
    if not deadlines_list:
        print("No deadlines available to view.\nReturning to Deadlines menu...")
        return
    print("\n======== DEADLINES ========")
    for i, deadline in enumerate(deadlines_list, start=1):
        print(
            f"\n{i}. {deadline[0]}\n"
            f"    Priority: {deadline[1]}\n"
            f"    Description: {deadline[2]}\n"
            f"    Due date: {deadline[3]}\n"
            f"    Status: {get_deadline_status(deadline[3])}"
        )
    print("\n===========================")
    while True:
        exit_view = input(
            "Press 'e' to go back to Deadlines menu: "
        ).lower().strip()

        if exit_view == "e":
            print("Returning to Deadlines menu...")
            return

        print("Wrong key, please select 'e'.")


def complete_deadline():
    pass
#once i grasp this in habits.py i'll be able to use it here.

