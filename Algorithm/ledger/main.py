

def main() -> None:
    ledger = []

    loopTimes = int(input("Enter the amount of items >> "))
    for i in range(loopTimes - 1):
        userIn = int(input(">> "))

        if not userIn:
            ledger.pop(-1)


def displayIntro() -> None:
    print("Enter a number to add it to the ledger")
    print("Enter the number 0 To remove the last item")
    print("Enter q to quit")


def calc(ledger: list) -> int:
    sum = 0
    for item in ledger:
        sum += int(item)

    return sum


if __name__ == "__main__":
    main()
