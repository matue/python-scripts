'''

Скрипт берет все файлы с расширением *.log из текущей директории
и преобразует все последовательности цифр длиной 16 знаков к виду:

1234 **** **** 1234

'''

import os
import re


def get_logs():  # функция, возвращающая список лог файлов
    files = os.listdir(".")  # листинг текущей директории
    m = []
    for i in files:
        if i.endswith('.log'):
            m.append(i)
    return m
pattern = r'\D(\d{4})\d{8}(\d{4})\D'
mask = r' \1 **** **** \2 '
for n in get_logs():  # цикл по именам файлов
    f = open(n, 'r')
    f_text = f.read()  # инициируем переменную f_text и помещаем в нее текстовое содержимое файла
    f_new_text = re.sub(pattern, mask, f_text)  # в f_new_text пишем обработанный текст
    with open(n, 'w') as f:
        f.write(f_new_text)
