"""
Mini-console for viewing or searching stored information.

Function view_console() displays searched information or the whole
database.
"""
import database

def view_console():
    menu = '''
    View menu:
     -View entire log (V)
     -Search log (S)

'''
    user_input = input(menu)
    if str.lower(user_input) == 'v':
        print(database.check_storage())

    elif str.lower(user_input) == 's':
        isearch = input('Search for a week or date here. (H) for '
                        'input instructions.')
        templ = database.check_storage()
        if isearch in templ:
            return templ[isearch]
            # print( list which contains isearch, use a generator expres-
            # sion)