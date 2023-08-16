#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    dec_num = 0
    numbers = []
    for s in roman_string:
        for num in roman:
            if s == num:
                numbers.append(roman[num])
    numbers += [0]
    for i in range(len(numbers) - 1):
        if numbers[i] >= numbers[i + 1]:
            dec_num += numbers[i]
        else:
            dec_num -= numbers[i]
    return dec_num
