#!/usr/bin/python3
import dis
def magic_calculation(c, b):
    result = 0

    for i in range(1, 3):
        try:
            if i > c:
                raise Exception('Too far')

            result += c ** b / i
        except:
            result = b + c
            break

    return result
