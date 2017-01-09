"""
Mini-console for initializing new weeks or entering/changing data for
existing days.

Function enter_data() is a mini-console for entering or changing
information.
"""
import new_mon, tup_maker, database, interface_view

def enter_data():
    """Coordinate other modules for entering or changing information."""
    enter_esc = False
    while not enter_esc:
        try:
            overall = database.check_storage()
        except:
            overall =[]
        menu = '''
        Entry menu:
        -Initiate new week (I)
        -Enter/change data for a day (D)
        -Return to main menu (M)

        '''
        user_input = input(menu)
        if str.lower(user_input) == 'i':
            parts = new_mon.date_input()
            tuplist = tup_maker.week_tuples(parts)
            database.new_storage(tuplist, parts)
            print('Week created:\n', tuplist)

        elif str.lower(user_input) == 'd':
            day = input('Enter the date that you\'d like to add '
                        'information to in format MM/DD:\n')
            interface_view.db_search_day(overall, day)
            db_insert(overall, day)
            database.save_to_file(overall)

        elif str.lower(user_input) == 'm':
            enter_esc = True



def db_insert(db, search_kword):
    for item in db:
        if search_kword in item:
            insert_place = db.index(item) + 1
            db_new(db, insert_place)
        elif not isinstance(item, str):
            db_insert(item, search_kword)

def db_new(db, insert_place):
    new_item = input('Enter a keyword for one expenditure:\n')
    query = str('Enter prices for ' + new_item + ' in format '
                                                 '#, #, #:\n')
    item_prices = input(query)
    cost_list = number_checker(item_prices)
    print('test', cost_list)
    db.insert(insert_place, {new_item: cost_list})
    if str.lower(input('Enter more expenses? (y/n)')) == 'y':
        db_new(db, insert_place)


def number_checker(item_prices):
    t = item_prices
    cost_list = []
    try:
        for number in t.split(', '):
            cost_list.append(float(number))
    except ValueError:
        t = input('Format incorrect, re-enter:')
        cost_list = number_checker(t)
    print(cost_list)
    return cost_list