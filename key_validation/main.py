from hashlib import sha256


def get_keys() -> list:
    keys = []

    with open("keys", "r") as key_file:
        for key in key_file.readlines():
            key = key.replace('\n', '')
            keys.append(key)

    return keys


def validate_key(key: str) -> bool:
    hashed_key = sha256(key.encode()).hexdigest()

    if hashed_key in get_keys():
        return True

    return False


def main() -> None:
    input_key = input("Enter Your Key >> ")
    print(validate_key(input_key))


if __name__ == "__main__":
    main()
