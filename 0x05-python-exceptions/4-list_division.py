#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    div_result = 0
    for i in range(list_length):
        try:
            div_result = my_list_1[i] / my_list_2[i]
        except (TypeError, ValueError):
            print("{}".format("wrong type"))
            div_result = 0
        except ZeroDivisionError:
            print("{}".format("division by 0"))
            div_result = 0
        except IndexError:
            print("{}".format("out of range"))
            div_result = 0
        finally:
            new_list.append(div_result)
    return new_list
