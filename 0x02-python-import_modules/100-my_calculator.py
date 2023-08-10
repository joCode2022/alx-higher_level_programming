#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ == '__main__':

    l_av = len(argv) - 1

    if l_av == 3:
        operator = argv[2]
        number_w = int(argv[1])
        number_y = int(argv[3])
        if operator == '+':
            res = add(number_w, number_y)
            print('{:d} + {:d} = {:d}'.format(number_w, number_y, res))
            exit(0)
        elif operator == '-':
            res = sub(number_w, number_y)
            print('{:d} - {:d} = {:d}'.format(number_w, number_y, res))
            exit(0)
        elif operator == '*':
            res = mul(number_w, number_y)
            print('{:d} * {:d} = {:d}'.format(number_w, number_y, res))
            exit(0)
        elif operator == '/':
            res = div(number_w, number_y)
            print('{:d} / {:d} = {:d}'.format(number_w, number_y, res))
            exit(0)
        else:
            print('Unknown operator. Available operators: +, -, * and /')
            exit(1)
    else:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
