from generator_utils import even_odd_generator

def main():
    # Тестування генератора
    gen = even_odd_generator()
    for _ in range(5):
        print(next(gen))


if __name__ == "__main__":
    main()