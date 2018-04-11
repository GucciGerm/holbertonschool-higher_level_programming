#!/usr/bin/python3
for n in range(0, 10):
    if n != 8:
        for j in range(0, 10):
            if n < j:
                print("{}{}, ".format(n, j), end='')
print(89)
