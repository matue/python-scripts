'''

Скрипт берет все файлы с расширением *.log из текущей директории
и преобразует все последовательности цифр длиной 16 знаков к виду:

1234 **** **** 1234

'''

import os
import re
def GetLogs(x):
    m=[]
    for i in x:
        if i.endswith('.log'):
            m.append(i)
    return m
files = os.listdir(".") # листинг текущей директории
LogFilesNames=GetLogs(files) # отобрать все лог файлы
print'Files:',len(LogFilesNames)
Pattern=r'\D(\d{4})\d{8}(\d{4})\D' 
Mask=r' \1 **** **** \2 ' 
for n in LogFilesNames:    # цикл по именам файлов
    f = open(n,'r') 
    f_text=f.read()  # инициируем переменную f_text и помещаем в нее текстовое содержимое файла
    f_new_text = re.sub(Pattern, Mask, f_text) # в f_new_text пишем обработанный с помощью регулярного выражения текст
    with open(n, 'w') as f: 
        print'Applying in file: ',n # вывод имени обработанного файла
        f.write(f_new_text) 
