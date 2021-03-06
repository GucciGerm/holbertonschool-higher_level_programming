#!/usr/bin/python3
def roman_to_int(roman_string):
    rn = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if type(roman_string) == str:
        result = 0
        storeprev = 0
        for g in list(roman_string):
                if rn[g] > result:
                    result = rn[g] - result
                elif rn[g] > storeprev:
                    result = rn[g] + result - storeprev * 2
                else:
                    result = rn[g] + result
                storeprev = rn[g]
        return result
    return 0
