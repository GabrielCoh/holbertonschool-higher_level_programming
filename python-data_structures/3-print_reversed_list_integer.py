#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        my_list.reverse()
    for item in range(len(my_list)):
        print("{:d}".format(my_list[item]))
