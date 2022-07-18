#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    nb_printed = 0
    print(x)
    for i in range(x):
        try:
            print(my_list[i], end="")
            nb_printed += 1
        except IndexError:
            break
    if nb_printed > 0:
        print()
    return (nb_printed)
