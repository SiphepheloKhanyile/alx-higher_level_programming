#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for a in my_string:
        if ord(a) != ord('c') and ord(a) != ord('C'):
            new_str += a
    return new_str
