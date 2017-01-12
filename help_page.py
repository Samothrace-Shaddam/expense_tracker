'''
Contains help files for the program, if you're looking for the README,
go to the README.
'''

def main_help():
    help_text = '''
Press the keys shown on the menu and hit enter to control different parts
of the program. Selections are not case sensitive. (Entering 'E' or 'e'
will both take you to the Enter menu.)
Enter 'q' from the main menu to quit the program. All data is saved at
entry time.
Specific control help can be found in the help (h) file of each
sub-console.
    '''
    print(help_text)

def enter_help():
    help_text = '''
From the enter console, you can add expenses to your database.
In the current version, you must "initiate" a week before you can add
information to a day in that week. After initiating, go to (D) to
enter expenses. Data is saved after answering (N) no to the enter more
expenses prompt. If you have made a mistake, you can (C) cancel at this
time.
'''
    print(help_text)