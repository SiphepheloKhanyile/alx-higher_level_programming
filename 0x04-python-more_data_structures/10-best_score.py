#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    for x, y in sorted(a_dictionary.items()):
        biggest = y
        key = x
        if y > biggest:
            biggest = y
            key = x
    return (key)
