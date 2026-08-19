from datetime import datetime, date
# A simple note space that will include categories and maybe a search function when I'll get more comfortable.
notes_list = []
categories = []

def notes_menu():
    while True:
        notes_choice = input("Welcome to the Notes menu ! Please choose an option: \n1. Add note\n2. Remove note\n3. Update note\n4. View all notes\n5. Categories\n6. Exit")
        if notes_choice not in [1, 2, 3, 4, 5]:
            print("Invalid input, please try again.")
            return
        elif notes_choice == '1':
            add_note()
        elif notes_choice == '2':
            remove_note()
        elif notes_choice == '3':
            update_note()
        elif notes_choice == '4':
            view_all_notes()
        elif notes_choice == '5':
            categories_menu()
        elif notes_choice == '6':
            print('Exiting the Notes menu. Returning to main menu...')
            return

def categories_menu():
    while True:
        categories_choice = input('Here is the Categories menu for notes. Please choose an option: \n1. Add category\n2. Remove category\n3. Update category\n4. View all categories\n5. Exit')
        if categories_choice not in [1, 2, 3, 4 ,5]:
            print("Invalid input, please try again.")
            return
        elif categories_choice == '1':
            add_category()
        elif categories_choice == '2':
            remove_category()
        elif categories_choice == '3':
            update_category()
        elif categories_choice =='4':
            view_all_categories()
        elif categories_choice == '5':
            print('Exiting Categories menu. Returning to Notes menu...')
            return

def add_notes():
    add_note_choice = input("Do you want to add a note ? (y/n): ").lower().strip()
    if add_note_choice == 'n':
        print("Returning to Notes menu...")
        return
    if add_note_choice != 'y':
        print("Invalid input, returning to Notes menu...")
        return
    if add_note_choice == 'y':
        while True:
            note_title = input("Enter the note title: ").strip()
            if note_title == '':
                print('Please enter a title for your note.')
                continue
            break
        note_content = input(
            "Write your note here: "
        ).strip()
        try:
            len(note_content) > 100
        except ValueError:
            print("Your note exceeds the limited amount of characters.")
            continue
        else:
            notes_list.append(note_content)
            print('Your note has been added successfully !')



def add_category():
    pass
# Categories : I'd rather have the notes separated, if i'd ever have to use a table it would be more efficient.
# A limit of categories maybe ? Alphabetical order ?
