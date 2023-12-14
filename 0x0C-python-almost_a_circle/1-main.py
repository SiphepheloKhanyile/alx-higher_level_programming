#!/usr/bin/python3
""" 1-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 2)
    print(r1.id)
    print("r1(x, y):({},{})".format(r1.x, r1.y), end="\n\n")

    r2 = Rectangle(2, 10)
    print(r2.id)
    print("r2(x, y):({},{})".format(r2.x, r2.y), end="\n\n")

    r3 = Rectangle(10, 2, 110, 20, 12)
    print(r3.id)
    print("r3(x, y):({},{})".format(r3.x, r3.y),end="\n\n")
