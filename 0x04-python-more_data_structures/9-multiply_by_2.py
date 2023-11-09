#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    r_dic = a_dictionary.copy()
    key_l = list((r_dic))
    i = 0
    for key in r_dic:
        r_dic[key_l[i]] = r_dic[key] * 2
        i += 1
    return (r_dic)
