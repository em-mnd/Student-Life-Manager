# So as of now I still don't know how to manipulate dates, I still am figuring out how I will proceed to manage these deadlines.

def deadline_menu():
    while True:
        print('Welcome to the Deadline menu! Please choose an option: \n1. Add deadline')
        deadline_choice = input(f"Enter your choice (1-5): ")
# Might not be optimal to ask them to choose an option (in which they would type it all out) and then ask them to choose by typing the number. Gotta choose the latter.