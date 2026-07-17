# A simple note space that will include categories and maybe a search function when I'll get more comfortable.

def notes_menu():
    while True:
        input("Welcome to the Notes feature! Please choose an option: \n1. Add Category\n2. Remove Category\n3. Update Category\n4. View Categories\n5. Add Notes\n6. Remove Notes\n7. Update Notes\n8. Exit\n")
        note_choice = input().index[1:9]
        while True:
            if input() in note_choice not in [1, 2, 3, 4, 5, 6, 7, 8]:
                print("Invalid input, please try again.")
            else:
                pass

def add_category():
    pass
# Categories : I'd rather have the notes separated, if i'd ever have to use a table it would be more efficient.
# A limit of categories maybe ? Alphabetical order ?

def add_notes():
    pass
# Thinking about adding a limit of characters, but I don't think that would be efficient. Maybe separate notes by most recent to oldest, or levels of importance then again would it be user friendly ?
