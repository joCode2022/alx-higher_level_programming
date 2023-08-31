#!/usr/bin/python3
"""
This is the "5-test_indentation" module.
The 5-text_indentation module supplies one function, text_indentation(text).
"""

def text_indentation(text):
    """splits a text into lines along "?", ":", "." followed by 2 new lines"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    signal = 0
    for a in text:
        if signal == 0:
            if a == ' ':
                continue
            else:
                signal = 1
        if signal == 1:
            if a == '?' or a == '.' or a == ':':
                print(a)
                print()
                signal = 0
            else:
                print(a, end="")
