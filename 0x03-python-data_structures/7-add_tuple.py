#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        if len(tuple_a) < 1:
            a = 0 + tuple_b[0]
            b = 0 + tuple_b[1]
        else:
            a = tuple_a[0] + tuple_b[0]
            b = tuple_b[1] + 0
        #a = 0 + tuple_b[0]
        #b = 0 + tuple_b[1]
        return (a, b)
    elif len(tuple_b) < 2:
        if len(tuple_b) < 1:
            a = 0 + tuple_a[0]
            b = 0 + tuple_a[1]
        else:
            a = tuple_a[0] + tuple_b[0]
            b = tuple_a[1] + 0
        return (a, b)
    else:
        a = tuple_a[0] + tuple_b[0]
        b = tuple_a[1] + tuple_b[1]
        return (a, b)
