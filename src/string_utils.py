def print_string(text):
    if not isinstance(text, str):
        raise TypeError("Аргумент має бути рядком")
    print(text)

