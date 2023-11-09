#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        biggest = 0
        key = ""
        for x, y in a_dictionary.items():
            if y > biggest:
                biggest = y
                key = x
    return (key)
