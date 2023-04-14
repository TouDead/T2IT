def find_bills(num: int, _bills: list[int]) -> list:
    _bills.sort(reverse=True)
    output = []

    for _bill in _bills:
        while num // _bill:
            output.append(_bill)
            num -= _bill

    return output


def format_bills(arr: list):
    output = []

    for _bill in set(arr):
        output.append((_bill, arr.count(_bill)))
    output.sort(reverse=False)

    return output


if __name__ == '__main__':
    bills = [1000, 500, 200, 100, 50, 20, 10]
    required_amount = int(input(f"How much money do you want to withdraw? "
                                f"(The amount must be a multiple of {min(bills)})"))

    if required_amount % min(bills):
        print(f"The amount must be a multiple of {min(bills)}")
    else:
        money_list = find_bills(required_amount, bills)
        formatted_list = format_bills(money_list)

        for bill, count in formatted_list:
            print(f"{bill}x{count}")
