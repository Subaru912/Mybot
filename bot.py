
import random

print("Добро пожаловать в игру 'Угадай число'!")
number = random.randint(1, 100)
attempts = 0

while True:
    guess = input("Угадай число от 1 до 100: ")
    attempts += 1

    if not guess.isdigit():
        print("Введите целое число.")
        continue

    guess = int(guess)
    if guess < number:
        print("Слишком маленькое.")
    elif guess > number:
        print("Слишком большое.")
    else:
        print(f"Поздравляю! Ты угадал число {number} за {attempts} попыток.")
        break
