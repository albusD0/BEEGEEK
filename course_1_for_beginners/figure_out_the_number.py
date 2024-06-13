import random

def set_num_and_input(): # функция для ввода и вывода диапазона, угадываемого числа и считывания числа с клавиатуры
    right_range = int(input('Введите число, которое станет верхней точкой диапазона: '))
    n = random.randint(1, right_range)
    s = input(f"Введите число от 1 до {right_range}: ")
    return n, s, right_range


def is_valid(s):
    return s.isdigit() and right_range >= int(s) > 0

malo = 'Ваше число меньше загаданного, попробуйте еще разок'
mnogo = 'Ваше число больше загаданного, попробуйте еще разок'
youre_lucky = 'Вы угадали, поздравляем!'

print('Добро пожаловать в числовую угадайку!')

n, s, right_range = set_num_and_input()

quit_the_game = 'q'
tries = 0
while quit_the_game != 'q' or quit_the_game != 'й':
    if not is_valid(s):
        print(f"А может быть все-таки введем целое число от 1 до {right_range}?")
        s = input('Введите число от 1 до 100: ')
    if int(s) < n:
        print(f"{malo}")
        s = input('> ')
        tries += 1
    elif int(s) > n:
        print(f"{mnogo}")
        s = input('> ')
        tries += 1
    elif int(s) == n:
        tries += 1
        print('{} Число попыток, которое вы потратили на угадывание: {}'.format(youre_lucky, tries))
        quit_the_game = input('Нажмите любую клавишу, если хотите продолжить, или q, чтобы завершить > ').lower()
        if quit_the_game == 'q' or quit_the_game == 'й': # реализуем алгоритм продолжения игры
            break
        else:
            n, s, right_range = set_num_and_input()
            tries = 0

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')