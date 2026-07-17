import main

# Daily habits are saved here (add, remove, update, view, complete today)

# Here I store the habit name, the notes according to habits (details about the habit),
# completion status and date created and maybe streak.

# I might filter completed habits for the day and then unmark them the next, but that is for later.
# Weekly completion status might be a good idea to implement as well, but that is for later.

habits_list = []

def habits_menu():
    while True:
        input("Welcome to the Habits feature! Please choose an option: \n1. Add habit\n2. Remove habit\n3. Update habit\n4. View all habits\n5. Exit\n")
        habits_choice = input(f"Enter your choice (1-5): ")
        if habits_choice not in ['1', '2', '3', '4', '5']:
            print("Invalid choice. Please try again.")
            habits_menu()
        elif habits_choice == '1':
            add_habit()
        elif habits_choice == '2':
            pass
        elif habits_choice == '3':
            pass
        elif habits_choice == '4':
            pass
        elif habits_choice == '5':
            print('Exiting the Habits feature. Returning to main menu.')
            main.slm_main_menu()

def add_habit():
    input("Do you want to add an habit ? (y/n): ")
    if input().lower() == 'y':
        habit_name = input("Enter the habit name: ")
        habit_priority = input("Enter the habit priority: ")
        habits_list.append(habit_name, habit_priority)
        print(f'Habit added: {habit_name}\n Priority: {habit_priority}\n')
    elif input().lower() == 'n':
        print('Returning to main menu.')
        main.slm_main_menu()


def remove_habit():
    input("Do you want to remove an habit ? (y/n): ")
    if input().lower() == 'y':
        habit_name = input("Which habit do you want to delete ?: ")
        for i, habit in enumerate(habits_list):
            if habit[0] == habit_name:
                habits_list.pop(i)
                print(f'Habit removed: {habit_name}')
        else:
            print('Habit not found.')
    elif input().lower() == 'n':
        print("Returning to main menu.")
        main.slm_main_menu


def update_habit():
    input('Do you want to update a task ? (y/n): ')
    if input().lower() == 'y':
        print("Here are the habits you have: ")
        for i, habit in enumerate(habits_list):
            print(f'{i + 1}. {habit[0:]}')
        habit_index = int(input("Enter the number of the habit you want to update: "))
        if 0 <= habit_index < len(habits_list):
            habit_name = input("Enter the new habit name: ")
            habit_priority = input("Enter the new priority level: ")
            print(f"Habit updated: {habit_name}")
        else:
            print("Invalid habit number")


