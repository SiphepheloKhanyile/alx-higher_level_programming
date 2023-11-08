#!/usr/bin/python3
def uniq_add(my_list=[]):
    r_list = []
    result = 0
    for item in my_list:
        if item not in r_list:
            r_list.append(item)
    for elem in r_list:
        result += elem
    return (result)
