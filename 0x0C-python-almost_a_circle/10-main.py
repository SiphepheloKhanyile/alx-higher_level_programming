#!/usr/bin/python3
""" 10-main """
from models.square import Square

if __name__ == "__main__":

    s1 = Square(5)
    print(s1)
    print(s1.size)
    print(f"height: {s1.height}, width: {s1.width}")
    s1.size = 10
    print(f"height: {s1.height}, width: {s1.width}")
    print(s1)

    try:
        s1.size = "9"
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

