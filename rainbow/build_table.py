import hashlib
from itertools import product


if __name__ == "__main__":
    def build_dict_table() -> None:
        with open("passwords.txt", "rb") as file:
            lines = file.readlines()
            file.close()
        with open("rainbow_dict.txt", "a") as file:
            for line in lines:
                line = line.decode().strip()
                file.write(f"{line}, {hashlib.md5(line.encode()).hexdigest()}\n")


    def build_brute_table() -> None:
        characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*()'
        with open("rainbow_brute_small.txt", "a") as file:
            for r in range(1, 4):
                for combo in product(characters, repeat=r):
                    file.write(f"{''.join(combo)}, {hashlib.md5(''.join(combo).encode()).hexdigest()}\n")


    def main():
        print("enter 1 to build the dictionary rainbow table")
        print("enter 2 to build the brute force rainbow table")
        choice = input(">> ")
        if choice.strip() == "1":
            build_dict_table()
        elif choice.strip() == "2":
            build_brute_table()
        else:
            print("invalid option")
            main()


    main()
