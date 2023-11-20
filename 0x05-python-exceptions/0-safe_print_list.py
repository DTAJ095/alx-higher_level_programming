#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    nb_element = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            nb_element += 1;
        except IndexError:
            break
    print()
    return (nb_element)

