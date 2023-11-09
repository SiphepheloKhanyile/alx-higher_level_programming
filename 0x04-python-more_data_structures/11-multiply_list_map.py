#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    return_lis = list((map(lambda x: x * number, my_list)))
    return (return_lis)
