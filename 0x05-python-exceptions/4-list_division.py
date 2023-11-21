#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    result = 0
    count = 0
    while (count < list_length):
        try:
            result = my_list_1[count] / my_list_2[count]
            new_list.append(result)
        except IndexError:
            result = 0
            new_list.append(result)
            print("out of range")
        except ZeroDivisionError:
            result = 0
            new_list.append(result)
            print("division by 0")
        except TypeError:
            result = 0
            new_list.append(result)
            print("wrong type")
        count += 1
    return (new_list)
