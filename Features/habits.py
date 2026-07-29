import main

# Daily habits are saved here (add, remove, update, view, complete today)

# Here I store the habit name, the notes according to habits (details about the habit),
# completion status and date created and maybe streak.

# I might filter completed habits for the day and then unmark them the next, but that is for later.
# Weekly completion status might be a good idea to implement as well, but that is for later.

habits_list = []

def habits_menu():
    while True:
        habits_choice = input("Welcome to the Habits feature! Please choose an option: \n1. Add habit\n2. Remove habit\n3. Update habit\n4. View all habits\n5. Complete habit\n6. Exit\n")
        if habits_choice not in ['1', '2', '3', '4', '5']:
            print("Invalid choice. Please try again.")
            return
        elif habits_choice == '1':
            add_habit()
        elif habits_choice == '2':
            remove_habit()
        elif habits_choice == '3':
            update_habit()
        elif habits_choice == '4':
            view_habits()
        elif habits_choice == '5':
            complete_habit()
        elif habits_choice == '6':
            print('Exiting the Habits menu. Returning to main menu...')
            return

def add_habit():
    add_habit_choice = input("Do you want to add an habit ? (y/n): ").lower()
    if add_habit_choice == 'n':
        print('Returning to Habit menu...')
        return
    if add_habit_choice == 'y':
        while True:
            habit_name = input("Enter the habit name: ").strip()
            if habit_name == '':
                print('Please write a name for your habit.')
                continue
            break
        while True:
            habit_priority = input("Enter the habit priority (high/medium/low): ").lower().strip()
            if habit_priority not in ["high", "medium", "low"]:
                print('Please choose high, medium or low.')
                continue
            break
        while True:
            habit_status = input('Have you completed this habit already ? (y/n): ').lower().strip()
            if habit_status not in ['y', 'n']:
                print('Please answer (y)es or (n)o.')
                continue
            break
        if habit_status == 'y':
            completion_status = True
            print('You have completed this habit for today !')
        if habit_status == 'n':
            completion_status = False
            print('This habit has not been completed yet.')
        habits_list.append((habit_name, habit_priority, completion_status))
        print(
            f"Habit added: {habit_name}\n"
            f"Priority level: {habit_priority}\n"
            f"Status: {completion_status}"
        )
    while True:
        retry_response = input('Do you want to add another habit ? (y/n): ').lower().strip()
        if retry_response == 'y':
            print('Restarting...')
            continue
        elif retry_response == 'n':
            print('Returning to Habits menu...')
            return


def remove_habit():
    remove_habit_choice = input("Do you want to remove an habit ? (y/n): ").lower().strip()
    if not habits_list:
        print("No habits to remove. Returning to Habits menu...")
        return
    if remove_habit_choice == 'n':
        print("Returning to Habits menu.")
        return
    if remove_habit_choice == 'y':
        print("Here are the habits you have:")
        input("Which habit do you want to delete ?: ")
        for i, habit in enumerate(habits_list):
            print(
                f"{i + 1}. {habit[0]}\n"
                f"    Priority: {habit[1]}"
                f"    Status: {habit[2]}"
                )
        while True:
            try:
                habit_index = int(input("Enter the number of the habit you want to remove: ")) - 1
            except  ValueError:
                print("Please enter a valid habit number.")
                continue
            if 0 <= habit_index < len(habits_list):
                break
            print("Invalid habit number.")
        removed_habit = habits_list.pop(habit_index)
        print(f"Habit removed: {removed_habit[0]}")
        while True:
            retry_response = input("Do you want to remove another habit ? (y/n): " ).lower().strip()
            if retry_response == 'y':
                print("Restarting...")
                continue
            elif retry_response== 'n':
                print("Returning to Habits menu...")
                return


def update_habit():
    if not habits_list:
        print('No habits to update.\nReturning to Habits menu...')
        return
    else:
        update_habit_response = input('Do you want to update a habit ? (y/n): ').lower().strip()
        if update_habit_response == 'y':
            print('Here are the habits you have:')
            for i, habit in enumerate(habits_list):
                print(
                    f"{i + 1}. {habit[0]}\n"
                    f"      {habit[1]}\n"
                    f"      {habit[2]}\n"
                    )
            while True:
                try:
                    habit_index = int(
                        input("Enter the number of the habit you want to update: ").lower().strip()
                    ) - 1
                except ValueError:
                    print('Please enter a valid habit number.')
                    continue
                
                if 0 <= habit_index < len(habits_list):
                    break
                
                print('Invalid habit number.')
                
            while True:
                habit_name = input('Enter the new name of your habit: ').strip()
                if habit_name == "":
                    print("Please write a name for your habit.")
                    continue
                break

def view_habits():
    pass

def complete_habit():
    while True:
        if not habits_list:
            print('No habits to complete. Returning to menu...')
            return
        else:
            print("\n==== HABITS ====")
            for i, habit in enumerate(habits_list):
                print(
                    f"\n{i + 1}. {habit[0]}\n"
                    f"    Priority : {habit[1]}"
                    f"    Status : Not complete"
                )
            
            print("\n==============")
            while True:
                try:
                    habit_index = int(
                        input('Enter the number of the habit you want to mark as completed: ')
                    ) - 1
                except ValueError:
                    print('Please enter a valid habit number.')
                    continue
                if 0 <= habit_index < len(habits_list):
                    break
                
                print('Invalid habit number.')
            # I want to mark the habit as completed after the user inputs the right number but I don't know how to do so, myb use a class so that i can have 'Complete ?: False' then user says they completed the habit and it becomes 'True' and shows as 'Completed'.