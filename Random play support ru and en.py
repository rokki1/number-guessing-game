import random

print("Введите ваш язык ниже, ру/ru - если русский")
print("<>" * 30)
print("Enter your language below, en - if English")
print()

lang = input("Вот здесь / Here --  ").lower()
if lang in ('en',):
    la = True
    print("\nExcellent, your language is English.")
elif lang in ('ru', 'ру'):
    la = False
    print("\nОтлично, ваш язык - Русский.")
else:
    print("\nПожалуйста, введите корректный язык / Please enter correct language.")
    lang = input().lower()
    la = lang not in ('ru', 'ру')

def rules():
    if not la:
        print("""
Приветствую вас на угадайке чисел 😎
↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
1. Вводимое число должно быть целым и положительным.
2. Ты сам выбираешь верхнюю границу диапазона (например, 1–50).
3. Не вводи одно и то же число дважды.
4. Веселись и не сдавайся!
        """)
    else:
        print("""
Welcome to the number guessing game 😎
↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
1. The number must be a positive integer.
2. You choose the upper limit yourself (for example, 1–50).
3. Don't enter the same number twice.
4. Have fun and don't give up!
        """)

rules()

def play_game():
    while True:
        if la:
            n = input("\nEnter the upper limit (must be > 1): ")
        else:
            n = input("\nВведи верхнюю границу (больше 1): ")

        if n.isdigit() and int(n) > 1:
            n = int(n)
            break
        else:
            print("Некорректное значение!" if not la else "Invalid value!")

    rand_num = random.randint(1, n)
    tried_numbers = set()
    attempts = 0

    if la:
        print(f"\nI've thought of a number between 1 and {n}. Try to guess it!")
    else:
        print(f"\nЯ загадал число от 1 до {n}. Попробуй его угадать!")

    while True:
        guess = input("\n> ")

        if not guess.isdigit():
            print("Введите целое число!" if not la else "Please enter an integer!")
            continue

        guess = int(guess)

        if guess < 1 or guess > n:
            print(f"Число должно быть от 1 до {n}!" if not la else f"The number must be between 1 and {n}!")
            continue

        if guess in tried_numbers:
            print("Ты уже вводил это число!" if not la else "You've already tried that number!")
            continue

        tried_numbers.add(guess)
        attempts += 1

        if guess == rand_num:
            if not la:
                print(f"\nТы угадал число за {attempts} попыток! 🎉")
            else:
                print(f"\nYou guessed the number in {attempts} tries! 🎉")
            break
        elif guess < rand_num:
            if not la:
                print("Маловато, попробуй больше.")
                if abs(rand_num - guess) < n * 0.1:
                    print("Ооохх, ты рядом!")
            else:
                print("Too low, try higher.")
                if abs(rand_num - guess) < n * 0.1:
                    print("Oh, you're close!")
        else:
            if not la:
                print("Многовато, попробуй меньше.")
                if abs(rand_num - guess) < n * 0.1:
                    print("Близко, почти угадал!")
            else:
                print("Too high, try lower.")
                if abs(rand_num - guess) < n * 0.1:
                    print("Close, almost got it!")

    while True:
        again = input("\nСыграем ещё раз? (да/нет) " if not la else "\nPlay again? (yes/no) ").lower()
        if again in ('да', 'yes'):
            play_game()
            return
        elif again in ('нет', 'no'):
            print("Пока!" if not la else "Goodbye!")
            return
        else:
            print("Пиши 'да' или 'нет'" if not la else "Please type 'yes' or 'no'")

play_game()

