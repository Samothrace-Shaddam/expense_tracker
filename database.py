"""
Store and retrieve data in a file.
"""
import json

def check_storage():
    """Return all stored data."""
    with open('database', 'r') as database:
        try:
            overall = json.load(database)
        except:
            overall = []
        return overall


try:
    overall = check_storage()
except:
    overall = []


def new_storage(tuplist, parts):
    """Store weekday lists as nested lists."""
    new_week = [('week_of_' + parts[0][2:4] + parts[1] + parts[2])]
    tuplist.insert(0, new_week)
    holder = []
    holder.extend(tuplist)
    overall.append(holder)#need to organize placement of weeks
    save_to_file(overall)

def save_to_file(db):
    with open('database', 'w') as database:
        json.dump(db, database)

