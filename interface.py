"""
Organizes all modules and deals with user input.

Function console() sends user to mini consoles for entering
or viewing information.
"""
import interface_enter, interface_view, help_page


def console():
    """Send user to appropriate module based on input."""
    print('Welcome to your week expenses calculator!')
    menu = '''
    Options (Enter the letter in parenthesis() to select):
    -Enter expenses (E)
    -View expenses for previous days or weeks (V)
    -Help (H)
    -Quit (Q)

    '''
    console_esc = False
    while not console_esc:
        user_input = input(menu)

        if str.lower(user_input) == 'e':
            interface_enter.enter_data_console()
            continue

        elif str.lower(user_input) == 'v':
            interface_view.view_console()

        elif str.lower(user_input) == 'h':
            help_page.main_help()
            # write help statement
        elif str.lower(user_input) == 'q':
            print('Bye!')
            console_esc = True

        else:
            print('Input incorrect.')
            continue



console()