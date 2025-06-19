#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    printed = 0
    try:
        while True:
            if count == x:
                break
            try:
                print("{:d}".format(my_list[count]), end="")
                printed += 1
            except (ValueError, TypeError):
                pass
            count += 1
    except IndexError:
        pass
    print()
    return printed
