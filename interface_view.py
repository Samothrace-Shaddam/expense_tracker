"""
Mini-console for viewing or searching stored information.

Function view_console() displays searched information or the whole
database.

Function organized_print() prints the database in format:
week
    day
      item


"""
import database

def view_console():
    menu = '''
        View menu:
         -View entire log (V)
         -Search log (S)
         -Raw data (R)

'''
    user_input = input(menu)
    if str.lower(user_input) == 'v':
        organized_print(database.check_storage())

    elif str.lower(user_input) == 's':
        templ = database.check_storage()
        query = input('Search for a timeframe(T) or an expense(X)?\n')
        if str.lower(query) == 'x':
            xsearch = input('Search for an expense:\n')
            db_search_exp(templ, xsearch)
        elif str.lower(query) == 't':
            tsearch = input('Search for a week or date here. (H) for '
                        'input instructions.\n')
            db_search_day(templ, tsearch)


    elif str.lower(user_input) == 'r':
        print(database.check_storage())

def organized_print(nest_list):
    for week in nest_list:
        for week_level in week:
            counter = 0
            if week_level == week[0]: #week[0] is week_of_######
                print(week_level)
            else:
                for day_level in week_level:
                    if counter == 0:
                        print('    ', week_level[0])
                        counter += 1
                    else:
                        print('      ', day_level)


def db_search_day(db, search_kword):
    for item in db:
        stored_info = db.index(item) + 1
        if search_kword in item:
            print(db)
        elif not isinstance(item, str) and not isinstance(item, dict):
            db_search_day(item, search_kword)

def db_search_exp(db, xsearch_kword):
    for item in db:
        stored_info = db.index(item) + 1
        if xsearch_kword in item:
            print(db[0], item)
        elif not isinstance(item, str) and not isinstance(item, dict):
            db_search_exp(item, xsearch_kword)

'''
example database:
[[['week_of_161128'], [['Mon', '11/28'], {'food': '5, 34'}], [['Tue', '11/29']], [['Wed', '11/30']], [['Thu', '12/01']], [['Fri', '12/02']], [['Sat', '12/03']], [['Sun', '12/04']]], [['week_of_170102'], [['Mon', '01/02']], [['Tue', '01/03']], [['Wed', '01/04']], [['Thu', '01/05']], [['Fri', '01/06']], [['Sat', '01/07']], [['Sun', '01/08']]]]
'''