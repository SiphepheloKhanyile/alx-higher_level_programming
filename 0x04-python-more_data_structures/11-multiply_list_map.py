#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    ls = my_list.copy()
    return_lis = list((map(lambda x: x * number, ls)))
    return (return_lis)
