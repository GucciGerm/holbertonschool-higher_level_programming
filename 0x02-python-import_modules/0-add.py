#!/usr/bin/python3
def main():
    from add_0 import add
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
    #  above we have to use the add fun to add a + b
if __name__ == "__main__":
    main()
