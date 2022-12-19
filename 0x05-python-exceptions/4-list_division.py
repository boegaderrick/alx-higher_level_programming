#!/usr/bin/python3
def list_division(my_list, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            val = (my_list[i]/my_list_2[i])
        except (TypeError, ValueError):
            print("wrong type")
            val = 0
        except ZeroDivisionError:
            print("division by 0")
            val = 0
        except IndexError:
            print("out of range")
            val = 0
        finally:
            new_list.append(val)
    return new_list
