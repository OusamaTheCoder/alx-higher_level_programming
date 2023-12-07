#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = [replace if value == search else value for value in my_list]

    return new_list
