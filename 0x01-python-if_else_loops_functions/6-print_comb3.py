#!/usr/bin/python3
for a in range(10):
    for b in range(1, 10):
        if a == 9 and b == 9:
            print("{:d}{:d}".format(a, b))
        else:
            print("{:d}{:d}".format(a, b), end=", ")
