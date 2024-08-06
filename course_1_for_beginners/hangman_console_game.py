import random
from string import ascii_uppercase

tries = 6  # количество попыток

words = ['Трансформер', 'Самолет', 'Книга', 'Человек', 'Барни']

def get_word(ws):
    w = random.choice(ws)
    return w.upper(), words.index(w)

# функция получения текущего состояния
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    print(stages[tries])


print('Давайте играть в угадайку слов!')

while True:
    word_with_index = get_word(words)

    word = word_with_index[0]

    guessed_letters = []

    all_input = []

    while True:
        while True:  # ввод только кириллических символов, никаких цифр
            sym = input('Введите букву (или слово целиком): ').upper()
            if sym in guessed_letters or sym in all_input:
                print('Такую букву (слово) вы уже вводили!')
                all_input.append(sym)
            else:
                if sym.isalpha() and sym not in ascii_uppercase:
                    break

        if sym == word: # если введено целое слово
            print('Поздравляем, вы угадали! Это слово', word.upper() + '. Вы победили!')
            break
        elif sym in word: # если только буква введена
            print('Верно!')
            for u in range(word.count(sym)): # если одинаковых символов несколько
                guessed_letters.append(sym)
            if len(guessed_letters) == len(word):
                print('Поздравляем, вы угадали! Это слово', word.upper() + '. Вы победили!')
                break
            for el in word: # вывод угаданных букв
                if el in guessed_letters:
                    print(el, end=' ')
                else:
                    print('*', end=' ')
            print()
        else: # если буквы нет в слове
            tries -= 1
            display_hangman(tries)
            if tries == 0: # если количество попыток закончилось
                display_hangman(0)
                print('Вы проиграли.\nБыло загадано слово:', word.upper())
                break

            print(f"Неверно. У вас еще {tries} попыток")

    one_more_time = input("Хотите сыграть еще? Нажмите 'y' или 'д', чтобы продолжить или любую другую клавишу, чтобы выйти: ")
    if one_more_time in ('y', 'н', 'д', 'l'):
        del words[word_with_index[1]]
        continue
    else:
        break
