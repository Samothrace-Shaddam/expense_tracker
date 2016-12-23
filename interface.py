import new_mon
import database
import tup_maker


def console():
    menu = '''
Welcome to your week expenses calculator!
    Options (Enter the letter in parenthesis() to select):
    -Enter expenses for a new week (E)
    -View expenses for previous days or weeks (V)
    -Help (H)

    '''
    console_esc = False
    while not console_esc:
        user_input = input(menu)

        if str.lower(user_input) == 'e':
            parts = new_mon.date_input()
            tuplist = tup_maker.week_tuples(parts)
            overall = database.storage(tuplist, parts)
            print('Week created:\n', overall)

            continue

        elif str.lower(user_input) == 'v':
            if input('print all? y/n') == 'y':
                print(database.check_storage())


            # isearch = input('Search for a week or date here. (H) for '
            #                 'input instructions.')
            # if isearch in overall:
            #     pass
            #     # print( list which contains isearch, use a generator expres-
            #     # sion)
        elif str.lower(user_input) == 'h':
            pass
            # write help statement
        else:
            pass



console()