
password = input("Enter a md5 >> ")

with open("rainbow_dict.txt", "r") as file:
    lines = file.read().split("\n")
    for line in lines:
        if line.split(", ")[1] == password:
            print(f"The password is: {line.split(', ')[0]}")
            break
        elif line.split(", ")[0] == "":
            print("no matches found")
