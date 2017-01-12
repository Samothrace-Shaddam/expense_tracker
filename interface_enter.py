"""
Mini-console for initializing new weeks or entering/changing data for
existing days.

Function enter_data() is a mini-console for entering or changing
information.
"""
import new_mon, tup_maker, database, interface_view, help_page



def enter_data_console(command):
    """Coordinate other modules for entering or changing information."""
    enter_esc = False
    while not enter_esc:
        overall = database.check_storage()
        menu = '''
        Entry menu:
        -Initiate new week (I)
        -Enter/change data for a day (D)
        -Return to main menu (M)
        -Help (H)

        '''
        if command == None: #gives the possibility to start the console
            user_input = str.lower(input(menu)) #with a selection
        else:
            user_input = command


        if user_input == 'i':
            parts = new_mon.date_input() #get & check date input
            tuplist = tup_maker.week_tuples(parts) #create week list
            database.new_storage(tuplist, parts) #store week
            print('Week created:\n', tuplist)

        elif user_input == 'd':
            day = input('Enter the date that you\'d like to add '
                        'information to in format MM/DD:\n')
            interface_view.db_search_day(overall, day)

            check_save = db_find_insert(overall, day)
            if check_save == 1:
                database.save_to_file(overall)

        elif user_input == 'm':
            enter_esc = True

        elif user_input == 'h':
            help_page.enter_help()

        else:
            print('Input incorrect.')
            continue



def db_find_insert(db, search_kword):
    check_save = 0
    for item in db:
        if search_kword in item:
            insert_place = db.index(item) + 1
            check_save = db_new_exps(db, insert_place)
            break
        elif not isinstance(item, str):
            check_save = db_find_insert(item, search_kword)
    return check_save

def db_new_exps(db, insert_place):
    console_esc = False
    while not console_esc:
        new_item = input('Enter a keyword for one expenditure:\n')
        query = str('Enter prices for ' + new_item + ' in format '
                                                     '#, #, #:\n')
        item_prices = input(query)
        cost_list = number_checker(item_prices)
        db.insert(insert_place, {new_item: cost_list})
        print(new_item, cost_list)
        user_input = str.lower(input('Enter more expenses? (y/n)'
                           '\n(C) to cancel.\n'))
        if user_input == 'y':
            continue

        elif user_input == 'n':
            return 1

        elif user_input == 'c':
            return 0



def number_checker(item_prices):
    t = item_prices
    cost_list = []
    try:
        for number in t.split(', '):
            cost_list.append(float(number))
    except ValueError:
        t = input('Format incorrect, re-enter in format \'#, #, #:')
        cost_list = number_checker(t)
    return cost_list