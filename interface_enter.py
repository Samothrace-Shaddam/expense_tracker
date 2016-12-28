"""
Mini-console for initializing new weeks or entering/changing data for
existing days.

Function enter_data() is a mini-console for entering or changing
information.
"""
import new_mon
import tup_maker
import database

def enter_data():
    """Coordinate other modules for entering or changing information."""
    user_input = input('Initiate new week (I), or enter/change data '
                       'for a day(D)?\n')
    if str.lower(user_input) == 'i':
        parts = new_mon.date_input()
        tuplist = tup_maker.week_tuples(parts)
        overall = database.storage(tuplist, parts)
        print('Week created:\n', tuplist)

    if str.lower(user_input) == 'd':
        pass