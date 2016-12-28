"""
Accepts date input, checks that it is correct and returns the date as a list.

TODO:
    Change functionality to eliminate the initialization of weeks, instead,
    simply check that dates are valid and store information for them.
"""
import datetime


def date_input():
    """Check that date input is correct and return the date as a list."""
    mon_date = input('Please enter Monday\'s date'
                     ' for the week you would like \nto'
                     ' initiate in YYYY/MM/DD format. \n')

    minyear = 2000
    maxyear = (datetime.date.today().year + 1)
    correct_date = False
    while not correct_date:
        #create a list containing the elements of date input
        dateparts = mon_date.split('/')
        #use datetime to return the integer value of the weekday
        #of the date entered for later checking
        d_o_w = datetime.datetime(int(dateparts[0]),
                                  int(dateparts[1]),
                                  int(dateparts[2])).weekday()

        #use exception checking with datetime to confirm that
        #input is a valid date, else replace input
        try:
            dateobj = datetime.date(int(dateparts[0]),
                                    int(dateparts[1]),
                                    int(dateparts[2]))
        except:
            mon_date = input('Improper date format, '
                             're-enter\n')
            continue

        #check that years are recent
        if int(dateparts[0]) > maxyear \
                or int(dateparts[0]) < minyear:
            mon_date = input("Year out of range, "
                             "re-enter\n")
            continue

        #check that input is a monday
        elif d_o_w != 0:
            mon_date = input('Date entered is not a '
                             'Monday, re-enter\n')
            continue

        else:
            correct_date = True

    #if everything checks, create a list of date elements
    else:
        parts = mon_date.split('/')
        return parts


