#!/usr/bin/python3
uppercase = __import__('8-uppercase').uppercase

uppercase("best")
uppercase("Best School 98 Battery street")
def uppercase(str):
    tmp = list(str)
    for i in range(len(tmp)):
        if (ord(tmp[i]) > 96 and ord(tmp[i]) < 123):
            tmp[i] = chr(ord(tmp[i]) - 32)
            print("{}".format(("").join(tmp)))
