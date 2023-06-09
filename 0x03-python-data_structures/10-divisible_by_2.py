#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    check_me = []

    for x in range(len(my_list)):
        if my_list[x] % 2 == 0:
            check_me.append(True)
        else:
            check_me.append(False)

    return (check)
