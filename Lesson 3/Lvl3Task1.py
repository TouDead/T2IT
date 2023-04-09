def processing_num(num: int, fizz: int, buzz: int) -> str:
    output = ""

    if not num % fizz:
        output += 'F'
    if not num % buzz:
        output += 'B'

    return output if output else str(num)


if __name__ == '__main__':
    f = int(input("Enter fizz: "))
    b = int(input("Enter buzz: "))
    length = int(input("Enter end number: "))

    print("-".join([processing_num(x+1, f, b) for x in range(length)]))
