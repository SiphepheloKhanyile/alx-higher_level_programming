#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    r_set = []
    for item in set_1:
        if item in set_2:
            continue
        else:
            r_set.append(item)
    for elem in set_2:
        if elem in set_1:
            continue
        else:
            r_set.append(elem)
    return (set(r_set))
