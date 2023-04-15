def find_bills(num: int, _bills: list[int]) -> list:
    _bills.sort()
    output = []

    for _id, _bill in enumerate(_bills):
        if num < min(_bills):
            break

        used = 10
        while num:
            if used == 0:
                break

            if (_bill * used) - num == 0 or \
                    ((_bill * used) < num and check_multiples((_bill * used - num), _bills[_id + 1:])):
                num -= _bill * used
                output.extend([_bill] * used)
                break

            used -= 1

    return output


def check_multiples(number: int, arr: list):
    for n in arr:
        if number % n == 0:
            return True
    return False


def format_bills(arr: list):
    output = []
    for _bill in set(arr):
        output.append((_bill, arr.count(_bill)))
    output.sort(reverse=False)
    return output


if __name__ == '__main__':
    bills = [10, 20, 50, 100, 200, 500, 1000]
    required_amount = int(input(f"How much money do you want to withdraw? "
                                f"(The amount must be a multiple of {min(bills)}): "))

    if required_amount % min(bills) != 0:
        print(f"The amount must be a multiple of {min(bills)}")
    elif required_amount > sum(bills) * 10:
        print(print(f"The amount must be less than {sum(bills) * 10}"))
    else:
        money_list = find_bills(required_amount, bills)
        formatted_list = format_bills(money_list)
        for bill, count in formatted_list:
            print(f"{bill}x{count}")
