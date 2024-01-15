import random

from typing import Tuple


class Game:
    """
    Класс игры.
    """
    desired_number: int  # загаданное число
    winner: str  # победитель
    attempts_count: int = 0  # количество попыток

    def __init__(self, min_value: int, max_value: int):
        """
        Конструктор игры.
        :param min_value: минимально возможный правильный ответ
        :param max_value: максимально возможный правильный ответ
        """
        if min_value > max_value:
            self.desired_number = random.randint(max_value, min_value)
        else:
            self.desired_number = random.randint(min_value, max_value)

    def guess(self, guess_number: int) -> bool:
        """
        Метод, позволяющий узнать, отгадано ли число.
        :param guess_number: число, предложенное в качестве «отгадки»
        :return: True, если число отгадано.
        """
        self.attempts_count += 1
        return guess_number == self.desired_number

    def start(self) -> None:
        """
        Метод, начинающий игру.
        :return: None
        """
        while True:
            # догадка вводится с клавиатуры
            guess_number_str = input("Введите вашу догадку: ")
            # проверка формата
            if not guess_number_str.isdigit():
                print("Нужно ввести число.")
                continue
            # упаковка
            guess_number = int(guess_number_str)

            # число угадано
            if self.guess(guess_number):
                self.winner = input("Как тебя зовут, победитель?")
                self.congratulate()
                break
            # число не угадано
            if self.desired_number < guess_number:
                print("Загаданное число меньше.")
                continue
            if self.desired_number > guess_number:
                print("Загаданное число больше.")

    def congratulate(self) -> None:
        """
        Метод, выводящий на экран консоли поздравление победителя.
        :return: None
        """
        print(f"Поздравляем, {self.winner} угадал число {self.desired_number} за {self.attempts_count} попыток!")


def get_numbers_from_user() -> Tuple[int, int]:
    """
    Метод, получающий числа от пользователя с помощью ввода из командной строки
    :return: Кортеж двух чисел.
    """
    desired_numbers = ()
    # будем опрашивать пользователя до тех пор, пока не получим ожидаемый результат
    while len(desired_numbers) != 2:
        numbers_str = input('Привет! Задай диапазон чисел в формате: a, b\n')
        # разбиваем строку и каждую подстроку освобождаем от лидирующих и концевых пробелов
        numbers_str_list = [x.strip() for x in numbers_str.split(',')]

        # некорректное количество
        if len(numbers_str_list) != 2:
            print("Должно быть ровно два числа")
            continue

        # проверка каждой подстроки на то, является ли она числом
        is_all_numbers = True
        for number_str in numbers_str_list:
            if not number_str.isdigit():
                print(f"{number_str} — это не число :(")
                is_all_numbers = False

        if not is_all_numbers:
            # если хотя бы одна подстрока не число — опрашиваем ещё раз
            continue

        # упаковка в кортеж
        desired_numbers = tuple(int(x) for x in numbers_str_list)

    return desired_numbers


def main():
    desired_numbers = get_numbers_from_user()
    game = Game(*desired_numbers)
    game.start()


if __name__ == '__main__':
    main()
