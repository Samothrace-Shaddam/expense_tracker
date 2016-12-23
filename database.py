import tup_maker

holder = []

def storage(tuplist, parts):
    newtry = [('week_of_' + parts[0][2:4] + parts[1] + parts[2]), tuplist]
    try:
        overall
    except NameError:
        overall = []
    tup_maker.week_tuples(parts)
    overall.extend(newtry)
    holder.extend(overall)
    return overall

def check_storage():
    return holder
