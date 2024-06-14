import random

chars_full = ['0123456789', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz', '!#$%&*+-=?@^_.', 'il1Lo0O']

questions = ['Включать ли цифры 0123456789? > ', 'Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? > ', 'Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? > ',
'Включать ли символы !#$%&*+-=?@^_? > ', 'Исключать ли неоднозначные символы il1Lo0O?']

chars = ''

def yes_no(num): # функция для запроса настроек генерации паролей
    print(questions[num])
    answer = input('д - Да / н - Нет ( y / n как вариант) > ').lower()
    if answer == 'н' or answer == 'n':
        return False
    else:
        return True

def generate_password(length, chars): # сам генератор паролей
    passwords = []
    for k in range(passw_quant):
        safe_passwords = []
        safe_symbols = []
        for l in range(length):
            safe_symbols.append(random.choice(chars))
            safe_passwords = ''.join(safe_symbols)
        passwords.append(safe_passwords)
    print('\nВаши безопасные пароли:', *passwords)

def purge_for_new_cycle(): # сброс данных перед началом новой генерации
    passw_quant = 0
    passw_len = 0
    answers = []


print("Программа 'Генератор паролей' поможет вам подобрать безопасные пароли.\nОтветьте на несколько вопросов, чтобы настроить программу\n")

while True:

    passw_quant = int(input('Количество паролей > ' ))
    passw_len = int(input('Длина одного пароля > '))

    answers = [] # создание списка с разрешенными символами
    for i in range(5):
        if yes_no(i):
            answers.append(chars_full[i])

    chars = ''.join(answers) # перевод списка с разрешенными символами в строку
    excl_syms = 'il1Lo0O'
    if excl_syms in answers: # при наличии сомнительных символов в строке, они убираются из нее
        chars = chars.replace(excl_syms, '')
        for jj in excl_syms:
            chars = chars.replace(jj, '')

    if chars == '': # если пользователь на всё ответил "нет"
        nothing_picked = input('\nНичего не выбрали. Попробуем еще? > д / н ( y / n ) > ').lower()
        if nothing_picked == 'н' or nothing_picked == 'n':
            break
        else:
            purge_for_new_cycle()
            continue

    generate_password(passw_len, chars)

    # перезапуск генератора или выход из программы
    s = input('\nХотите подобрать другие пароли? д / н ( y / n ) > ').lower()
    if s == 'н' or s == 'n':
        break
    else:
        purge_for_new_cycle()
        continue
