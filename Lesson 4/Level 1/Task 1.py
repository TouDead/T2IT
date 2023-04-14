def sum_with_while(_list: list) -> int:
    my_sum = 0
    i = 0

    while i < len(_list):
        my_sum += _list[i]
        i += 1

    return my_sum


def sum_with_for(_list: list) -> int:
    my_sum = 0

    for i in _list:
        my_sum += i

    return my_sum


if __name__ == '__main__':
    my_list = list(range(1, 11))
    print(f"The result of the calculation through the while {sum_with_while(my_list)}")
    print(f"The result of the calculation through the for {sum_with_for(my_list)}")
