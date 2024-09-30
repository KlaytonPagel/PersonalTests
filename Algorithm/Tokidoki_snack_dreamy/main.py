# Tokidoki Snack Dreamy problem from https://www.acmicpc.net/problem/12789
# People are currently lined up in a single line, and only the person at the front can move.
# Ingyu has created a line that only allows people to pass in order of their number.
# Between this line and the person at the front of the queue, there is space for one person to enter a single line.
# People currently in the queue can come to this space, but not the other way around.
#
# example pictures can be found in the current directory


def check_line(position: int, line: list) -> bool:
    side: list = []
    end: list = []
    next: int = 1

    while len(line) > 0:
        for person in line.copy():
            if int(line[0]) == next:
                end.append(int(line.pop(0)))
                next += 1

            elif len(side) > 0 and side[-1] == next:
                end.append(side.pop(-1))
                next += 1

            else:
                side.append(int(line.pop(0)))

    while len(side) > 0 and side[-1] == next:
        for person in side.copy():
            if int(side[-1]) == next:
                end.append(int(side.pop(-1)))
                next += 1

    if len(side) > 0 or len(end) < position:
        return False

    return True


def main() -> None:
    position: int = int(input())
    line: list = input().split()

    if check_line(position, line):
        print("Nice")
    else:
        print("Sad")


if __name__ == "__main__":
    main()
