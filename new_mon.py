import datetime


def date_input():
    mon_date = input('Please enter the date of the Monday'
                     ' of the week \nyou would like to'
                     ' record in YYYY/MM/DD format. \n')

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


