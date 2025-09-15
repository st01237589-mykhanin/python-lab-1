def print_string(text):
    if not isinstance(text, str):
        raise TypeError("Аргумент має бути рядком")
    print(text)

def check_case(text):
    if not isinstance(text, str):
        raise TypeError("Аргумент має бути рядком")
    if not text:
        return "Порожній рядок"
    if text.isupper():
        return "Усі літери великі"
    elif text.islower():
        return "Усі літери малі"
    else:
        return "Літери змішані"

def word_to_upper_list(word):
    if not isinstance(word, str):
        raise TypeError("Аргумент має бути рядком")
    return [char.upper() for char in word]
