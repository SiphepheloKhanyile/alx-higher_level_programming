#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    count = 0
    while (count < list_length):
        try:
            result = my_list_1[count] / my_list_2[count]
        except IndexError:
            result = 0
            print("out of range")
        except ZeroDivisionError:
            result = 0
            print("division by 0")
        except Exception:
            result = 0
            print("wrong type")
        finally:
            new_list.append(result)
        count += 1
    return (new_list)
