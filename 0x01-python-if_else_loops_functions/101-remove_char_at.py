#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    new_str = ""
    for char in str:
        if i != n:
            new_str += char
        i += 1
    return (new_str)
