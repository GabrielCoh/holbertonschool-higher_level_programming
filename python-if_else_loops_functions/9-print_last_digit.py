#!/usr/bin/python3
def print_last_digit(i):
    last = abs(i) % 10
    print(last, end='')
    return last
