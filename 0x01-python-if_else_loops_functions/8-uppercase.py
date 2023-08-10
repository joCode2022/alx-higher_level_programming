#!/usr/bin/python3
def uppercase(str):
     ne_str = ""
    for i in range(len(str)):
        if (ord(str[i]) >= 97 and ord(str[i]) <= 122):
             ne_str += chr(ord(str[i]) - 32)
            continue
         ne_str += str[i]
    print('{0}'.format( ne_str))
