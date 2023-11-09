#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    d_list = list((sorted(a_dictionary.items())))
    for x, y in d_list:
        biggest = y
        key = x
        if y > biggest:
            biggest = y
            key = x
    return (key)
