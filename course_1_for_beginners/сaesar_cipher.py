'''
Описание проекта: требуется написать программу, способную шифровать и дешифровать текст в соответствии с алгоритмом Цезаря.
Она должна запрашивать у пользователя следующие данные:

направление: шифрование или дешифрование;
язык алфавита: русский или английский;
шаг сдвига (со сдвигом вправо).
Примечание 1. Считайте, что в русском языке 32 буквы (буква ё отсутствует).

Примечание 2. Неалфавитные символы — знаки препинания, пробелы, цифры — не меняются.

Примечание 3. Сохраните регистр символов. Например, текст: "Умом Россию не понять" при сдвиге на одну позицию вправо будет преобразован в: "Фнпн Спттйя ож рпоауэ".

Составляющие проекта:

Целые числа (тип int);
Модульная арифметика;
Переменные;
Ввод / вывод данных (функции input() и print());
Условный оператор (if/elif/else);
Цикл for/while;
Строковые методы.

y=(x+k) mod n, 
x=(y−k) mod n, где 

x — символ открытого текста, 
y — символ шифрованного текста, 
n — мощность алфавита (количество символов), а k — ключ.

Под операцией mod подразумевается операция нахождения остатка. В языке Python для нахождения остатка от деления двух чисел, мы используем оператор %.
 '''
 
 # Шифрование
 
lat_low = 'abcdefghijklmnopqrstuvwxyz'
lat_up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
 
cyr_low = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
cyr_up = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

def decypher(line, lang_cypher, k): #  x = (y - k) % n
    decyphered_line = []
    if lang_cypher == 1:
        n = 32
        for el_r in line:
            if el_r in cyr_low:
                char = (cyr_low.index(el_r) - k) % n
                decyphered_line.append(cyr_low[char])
            elif el_r in cyr_up:
                char = (cyr_up.index(el_r) - k) % n
                decyphered_line.append(cyr_up[char])
            else:
                char = line.index(el_r)
                decyphered_line.append(el_r)
    elif lang_cypher == 2:
        n = 26
        for el_r in line:
            if el_r in lat_low:
                char = (lat_low.index(el_r) - k) % n
                decyphered_line.append(lat_low[char])
            elif el_r in lat_up:
                char = (lat_up.index(el_r) - k) % n
                decyphered_line.append(lat_up[char])
            else:
                decyphered_line.append(el_r)
    print(''.join(decyphered_line)) 
   
   
def cypher(line, lang_cypher, k):  
    cyphered_line = []
    if lang_cypher == 1:
        n = 32
        for el_r in line:
            if el_r in cyr_low:
                char = (cyr_low.index(el_r) + k) % n
                cyphered_line.append(cyr_low[char])
            elif el_r in cyr_up:
                char = (cyr_up.index(el_r) + k) % n
                cyphered_line.append(cyr_up[char])
            else:
                cyphered_line.append(el_r)
    elif lang_cypher == 2:
        n = 26
        for el_r in line:
            if el_r in lat_low:
                char = (lat_low.index(el_r) + k) % n
                cyphered_line.append(lat_low[char])
            elif el_r in lat_up:
                char = (lat_up.index(el_r) + k) % n
                cyphered_line.append(lat_up[char])
            else:
                cyphered_line.append(el_r)
    print(''.join(cyphered_line)) 
    
    
 
what_to_do = int(input('Выберите режим работы программы. Нажмите 1, если хотите зашифровать послание, или 2 - если нужно расшифровать его\n'))

lang_cypher = int(input('Выберите язык шифрования / дешифрования: 1 - если русский, 2 - если английский\n'))

k = int(input('Укажите шаг сдвига\n'))
 
s = input('Введите свое сообщение для шифрования / дешифрования\n')

if what_to_do == 1:
     cypher(s, lang_cypher, k)
elif what_to_do == 2:
    decypher(s, lang_cypher, k)
    







 


