import keyboard


down = True
while True:
    key = keyboard.read_key(suppress=True)
    if len(key) > 1 and down:
        keyboard.send(key)
        down = False
    elif key and down:
        keyboard.write(f"{format(ord(key), 'b')} ")
        down = False
    elif not down:
        down = True

