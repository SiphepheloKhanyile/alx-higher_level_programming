#!/usr/bin/python3
def search_replace(my_list, search, replace):
    r_list = []
    for a in my_list:
        if a != search:
            r_list.append(a)
        else:
            r_list.append(replace)
    return (r_list)
