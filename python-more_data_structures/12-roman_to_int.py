#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or None:
        return 0
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}
    summ = 0
    prev = 0
    for char in reversed(roman_string):
        roman_string = roman_dict.get(char, 0)
        if roman_string < prev:
            summ -= roman_string
        else:
            summ += roman_string
            prev = roman_string
    return summ
