"""
Store and retrieve data in a file.
"""
import json

overall = []

def storage(tuplist, parts):
    """Store weekday lists as nested lists."""
    newtry = [('week_of_' + parts[0][2:4] + parts[1] + parts[2]), tuplist]
    holder = []
    holder.extend(newtry)
    overall.extend(holder)

    return holder

def check_storage():
    """Return all stored data."""
    return overall
