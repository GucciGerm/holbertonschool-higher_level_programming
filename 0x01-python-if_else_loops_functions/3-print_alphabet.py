#!/usr/bin/python3

for n in range(ord('a'), ord('z') + 1):
    if (chr(n) != 'q') and (chr(n) != 'e'):
        print("{}".format(chr(n)), end='')
