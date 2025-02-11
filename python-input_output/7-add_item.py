#!/usr/bin/python3
"""Load, add, save"""


import json
import sys
from os.path import exists

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


"""
Function that adds all arguments to
a Python lst, then save them to a file
"""


filename = "add_item.json"

my_list = []

if exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

for args in sys.argv[1:]:
    my_list.append(args)
save_to_json_file(my_list, filename)
