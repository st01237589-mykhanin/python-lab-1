from string_utils import print_string, check_case, word_to_upper_list
from generator_utils import even_odd_generator

def main():
    # Тестування функцій з рядками
    try:
        print_string("Print String")
        print(check_case("CHECK CASE"))
        print(check_case("check case"))
        print(check_case("cHeCk CaSe"))
        print(word_to_upper_list("smogtether"))
    except TypeError as e:
        print(f"Помилка: {e}")

    # Тестування генератора
    gen = even_odd_generator()
    for _ in range(5):
        print(next(gen))


if __name__ == "__main__":
    main()