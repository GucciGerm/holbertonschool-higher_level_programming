#!/usr/bin/python3
for n in range(1, 90):
    if n != 89:
        print("{:02d}, ".format(n), end='')
print("{}".format(n))
