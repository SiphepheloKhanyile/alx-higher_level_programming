#!/usr/bin/python
def max_integer(my_list=[]):
    biggest = 0
    if len(my_list) < 1:
        return None
    else:
        for a in my_list:
            if a > biggest:
                biggest = a
        return biggest
