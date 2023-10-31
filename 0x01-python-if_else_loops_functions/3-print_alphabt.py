#!/usr/bin/python3
for a in range(ord('a'), ord('z')):
    if chr(a) in 'qe':
        continue
    print("{:c}".format(a), end="")
