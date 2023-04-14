def processing_num(num: int, _fizz: int, _buzz: int) -> str:
    output = ""

    if not num % _fizz:
        output += 'F'
    if not num % _buzz:
        output += 'B'

    return output if output else str(num)


if __name__ == "__main__":
    fizz = int(input("Enter fizz: "))
    buzz = int(input("Enter buzz: "))

    with open("number.txt", 'r', encoding="utf-8") as f:
        with open("output.txt", 'w', encoding='utf-8') as wf:
            for line in f.readlines():
                text = "-".join(list([processing_num(int(x), fizz, buzz) for x in line.replace("\n", "").split("-")]))
                wf.write(text+"\n")
