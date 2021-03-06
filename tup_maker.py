"""
Initialize weeks by creating a list of tuples which contain the day of the
week and date, paired.
"""

import datetime


def week_tuples(parts):
    """Return a list of tuples which contain the day of the week and
    its date, paired."""
    one_day = datetime.timedelta(days=1)
    weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat',
                'Sun']
    tuplist = []
    monday = datetime.date(int(parts[0]),
                            int(parts[1]),
                            int(parts[2]))

    count = 0
    for day in weekdays:
        new_day = str(monday + (count * one_day)).split("-")
        tupholder = [weekdays[count], str(new_day[1]
                            + '/' + new_day[2])]
        tuplist.append([tuple(tupholder), ])
        count += 1

    return tuplist