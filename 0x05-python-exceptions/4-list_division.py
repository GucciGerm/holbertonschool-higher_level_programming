#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newlist = [0] * list_length
    for n in range(list_length):
        try:
            newlist[n] = my_list_1[n] / my_list_2[n]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            pass
    return newlist
