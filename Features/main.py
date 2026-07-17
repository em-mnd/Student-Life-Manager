import tasks
import notes
import habits

# Display the main menu options to the user

# Print menu options and ask for input
# Make a choice variable to store user choice, depending on choice another menu might be displayed
# depending on the feature selected or the user might want to exit
# here there is no logic for other features, it's a gateway for them


def slm_main_menu():
    while True:
        main_menu_choices = input("Welcome to the Student Life Manager! Please select a feature to use: \n1. Tasks\n2. Habits\n3. Deadlines\n4. Notes\n5. Budget\n6. Exit\nEnter your choice (1-6): ")
        if main_menu_choices not in ['1', '2', '3', '4', '5', '6']:
            print("Invalid choice. Please try again.")
            continue
        elif main_menu_choices == '1':
            print("You selected Tasks.")
            tasks.tasks_menu()
        elif main_menu_choices == '2':
            print("You selected Habits.")
            habits.habits_menu()
        elif main_menu_choices == '3':
            print("You selected Deadlines.")
            # Call the deadlines feature function here
        elif main_menu_choices == '4':
            print("You selected Notes.")
            # Call the notes feature function here
        elif main_menu_choices == '5':
            print("You selected Budget.")
            # Call the budget feature function here
        elif main_menu_choices == '6':
            print("Exiting the Student Life Manager. Goodbye!")
            exit()

slm_main_menu()