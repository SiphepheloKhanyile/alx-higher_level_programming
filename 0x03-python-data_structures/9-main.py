#!/usr/bin/python3
max_integer = __import__('9-max_integer').max_integer

my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}\n".format(max_value))

my = []
max2 = max_integer(my)
print("Max2: {}\n".format(max2))

m3 = [1]
mx = max_integer(m3)
print("Mx: {}\n".format(mx))

