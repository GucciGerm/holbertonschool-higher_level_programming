#!/usr/bin/python3
def main():
    from sys import argv    # importing arguments from system module

    argcount = len(argv) - 1   # count is 1 less
    print("{} argument".format(argcount), end='')

    if argcount == 0:
        print('s.')
    elif argcount == 1:
        print(':')
    else:
        print('s:')
    for n in range(1, len(argv)):
        print('{}: {}'.format(n, argv[n]))
if __name__ == "__main__":
    main()
