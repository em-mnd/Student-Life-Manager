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

def add_note():
    add_note_choice = input(
        "Do you want to add a note ? (y/n): "
    ).lower().strip()
    if add_note_choice == 'n':
        print("Returning to Notes menu...")
        return
    if add_note_choice != 'y':
        print("Please answer with 'y' or 'n'.")
        continue
    while True:
        note_title = input("Enter the note title: ").strip()
        if note_title == '':
            print("Please enter a title for your note.")
            continue
        break
    while True:
        note_content = input(
            "Write something for your note: "
        ).strip()
        if note_content == '':
            print(
                "Please write something for your note "
                "(100 characters max.)"
            )
            continue
        if len(note_content) > 100:
            print(
                "Please write a note with "
                "100 characters or less."
            )
            continue
        break
    if not categories:
        print(
            "No categories available. "
            "Creating default category 'General'..."
        )
        categories.append("General")
    while True:
        print("\n====== CATEGORIES ======")
        for i, category in enumerate(categories, start=1):
            print(f"{i}. {category}")
        category_choice = input(
            "\nChoose a category by number "
            "(or type 'new' to create a new category): "
        ).lower().strip()
        if category_choice == "new":
            add_category()
            continue
        if not category_choice.isdigit():
            print(
                "Please choose a category number "
                "or type 'new'."
            )
            continue
        category_index = int(category_choice) - 1
        if (
            category_index < 0
            or category_index >= len(categories)
        ):
            print("That category does not exist.")
            continue
        note_category = categories[category_index]
        break
    creation_date = date.today()
    note = {
        "title": note_title,
        "content": note_content,
        "category": note_category,
        "created_at": creation_date
    }
    notes_list.append(note)
    print(
        "\nYour note has been added successfully!"
        f"\nTitle: {note_title}"
        f"\nCategory: {note_category}"
        f"\nCreated: {creation_date}"
    )


def add_category():
    while True:
        category_name = input(
            "Enter the name of your new category "
            "(or 'b' to go back): "
        ).strip()
        if category_name.lower() == "b":
            print("Category creation cancelled.")
            return
        if category_name == "":
            print("Please enter a category name.")
            continue
        category_exists = False
        for category in categories:
            if category.lower() == category_name.lower():
                category_exists = True
                break
        if category_exists:
            print(
                f"The category '{category_name}' "
                "already exists."
            )
            continue
        categories.append(category_name)
        print(
            f"Category '{category_name}' "
            "has been added successfully!"
        )
        return