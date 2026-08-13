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
