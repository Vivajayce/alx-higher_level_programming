#!/usr/bin/python3
def roman_to_int(roman_string):
    summ= 0
    for i in range(len(S)-1,-1,-1):
        num = roman[S[i]]
        if 3*num < summ:
            summ = summ-num
        else:
            summ = summ+num
    return summ
