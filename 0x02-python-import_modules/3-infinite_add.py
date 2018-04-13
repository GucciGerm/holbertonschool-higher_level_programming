#!/usr/bin/python3
def main():
    from sys import argv
    argnum = 0
    for n in range(1, len(argv)):    # we want to add argument being passed to
        argnum += int(argv[n])    # the argument num / using int to cast
    print(argnum)
if __name__ == "__main__":
    main()
