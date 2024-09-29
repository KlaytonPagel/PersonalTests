

def main() -> None:
    displayIntro()
    ledger = []

    loopTimes = int(input("Enter the amount of items >> "))
    for i in range(loopTimes):
        userIn = int(input(">> "))

        if not userIn:
            ledger.pop(-1)
            
        ledger.append(userIn)
        
    displayTotal(ledger)

def displayIntro() -> None:
    print("Enter a number to add it to the ledger")
    print("Enter the number 0 To remove the last item")
    print("Enter q to quit")


def displayTotal(ledger: list) -> None:
    sum = 0
    for item in ledger:
        sum += int(item)

    print(f"The total is: {sum}")


if __name__ == "__main__":
    main()
