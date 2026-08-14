# Error log

This file contains few errors that might have confused me, broke my code files or appeared during testing or debugging sessions.
I will make sure to log those errors and hopefully the solutions I found to solve or fix them.
Errors will be dated and sorted depending the difficulty to fix them (high/medium/low).

## 11/08/2026

Debug session :
- Started a test session to make sure habits file  and tasks file worked smoothly with main file (which contains the main menu).
- Ran the file and noticed that the main menu directly showed the habits menu without being solicited making it bad for the user to actually access said main menu.
- Immediately thought that the error came from circular import for which I wrote in the main menu file 'import tasks, habits' instead of 2 separate imports('import tasks' first then 'import habits').
- After that I began a debug session within my python files; the main menu still showed the habits menu instead of its own.
- My first small error was to have not included 6 in the option list, 6 being the option to exit, so when I typed 6 to the habits menu to exit it sent back 'invalid choice...' but it still proceeded to show the main menu (Still figuring out how).
  -> That was partly fixed /: I included 6 in the habits menu choices list and it worked.
- But another issue came up /: Once I found access to the main menu by exiting the habits menu, I selected 1 to access the tasks menu, but an AttributeError surged due to a circular import ("module 'tasks' doesn't have an attribute called tasks_menu")
- So I was unable to test if my tasks file's functions worked well through the main menu and said main menu doesn't show the right menu to the user.

## 13/08/2026

Debug session — solution for the 11/08/2026:
- After testing the files and looking further into the issue, I understood that the main problem was indeed related to circular imports, but not because I had written import tasks, habits on the same line.
- The actual circular import came from main.py importing tasks.py and habits.py, while both tasks.py and habits.py were also importing main.py.
- I removed import main from both the tasks and habits files so the imports now only go one way: main.py imports the feature files, but the feature files do not import main.py back.
- I also noticed that tasks_menu() and habits_menu() were both being called at the bottom of their respective files. Since Python executes the code inside a file when it is imported, this explained why the Habits menu appeared immediately even though I had not selected it from the main menu.
- I removed those calls from the bottom of both files and kept slm_main_menu() in main.py as the entry point of the program.
- I changed the imports in the main file so I could access the feature menus through their respective modules and keep it clearer which function belonged to which file.
- The issue with option 6 in the Habits menu was fixed by adding '6' to the list of accepted choices. It can now properly exit the Habits menu instead of first returning "Invalid choice".
- I also understood why exiting the Habits menu was still somehow taking me back to the main menu before I had fixed everything: habits_menu() had originally been called from the main menu, so once it reached return, Python continued from where that function had been called.
- After applying the changes, the program now opens with the Student Life Manager main menu as intended. The Tasks and Habits menus are only opened once I select them, and exiting either feature correctly returns me to the main menu.
