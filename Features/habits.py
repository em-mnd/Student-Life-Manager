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
            habits_menu()
        elif habits_choice == '1':
            add_habit()
        elif habits_choice == '2':
            remove_habit()
        elif habits_choice == '3':
            update_habit
        elif habits_choice == '4':
            view_habits()
        elif habits_choice == '5':
            complete_habit()
        elif habits_choice == '6':
            print('Exiting the Habits menu. Returning to main menu.')
            return

def add_habit():
    add_habit_choice = input("Do you want to add an habit ? (y/n): ")
    if add_habit_choice.lower() == 'y':
        habit_name = input("Enter the habit name: ")
        habit_priority = input("Enter the habit priority: ")
        habits_list.append(habit_name, habit_priority)
        print(f'Habit added: {habit_name}\n Priority: {habit_priority}\n')
    elif add_habit_choice.lower() == 'n':
        print('Returning to Habit menu.')
        return


def remove_habit():
    remove_habit_choice = input("Do you want to remove an habit ? (y/n): ")
    if remove_habit_choice.lower() == 'y':
        habit_name = input("Which habit do you want to delete ?: ")
        for i, habit in enumerate(habits_list):
            if habit[0] == habit_name:
                habits_list.pop(i)
                print(f'Habit removed: {habit_name}')
        else:
            print('Habit not found.')
    elif remove_habit_choice.lower() == 'n':
        print("Returning to Habits menu.")
        return


def update_habit():
    update_habit_choice = input('Do you want to update a task ? (y/n): ')
    if update_habit_choice.lower() == 'y':
        print("Here are the habits you have: ")
        for i, habit in enumerate(habits_list):
            print(f'{i + 1}. {habit[0:]}')
        habit_index = int(input("Enter the number of the habit you want to update: "))
        if 0 <= habit_index < len(habits_list):
            habit_name = input("Enter the new habit name: ")
            habit_priority = input("Enter the new priority level: ")
            print(
                f"Habit updated: {habit_name}"
                f"Priority level updated: {habit_priority}")
        else:
            print("Invalid habit number")
    if update_habit_choice == 'n':
        print('Returning to Habits menu.')
        return


def view_habits():
    pass

def complete_habit():
    pass