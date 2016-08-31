'''

Скрипт берет все файлы с расширением *.log из текущей директории
и преобразует все последовательности цифр длиной 16 знаков к виду:

1234 **** **** 1234

'''

import os, re
files = os.listdir(".") # листинг текущей директории
LogFilesNames = filter(lambda x: x.endswith('.log'), files) # отобрать все лог файлы
print'Files:',len(LogFilesNames)
Pattern=r'\D(\d{4})\d{8}(\d{4})\D' #паттерн 
Mask=r' \1 **** **** \2 ' #маска
for n in LogFilesNames:    # цикл по именам файлов
    f = open(n,'r').readlines() # читаем строки файла
    print'File: ',n,'\nLines: ',len(f)
    f_text=''.join(f)  # инициируем переменную f_text и помещаем в нее текстовое содержимое файла
    f_new_text = re.sub(Pattern, Mask, f_text) # в f_new_text пишем обработанный с помощью регулярного выражения текст
    f = open(n, 'w') #открытие файла для записи
    print'Applying in file: ',n # вывод имени обработанного файла
    f.write(f_new_text) #запись в файл преобразованного текста
    f.close() #закрытие файла

    



