#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) < 1:
        return None
    biggest = 0
    for x, y in a_dictionary.items():
        if y > biggest:
            biggest = y
            key = x
    return (key)
