#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    new_list = []
    for i in my_list:
        if i == my_list[idx]:
            continue
        new_list += [i]
    my_list.clear()
    my_list.extend(new_list)
    return new_list
