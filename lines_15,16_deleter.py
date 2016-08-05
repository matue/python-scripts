import codecs #импорт библиотеки
from os import listdir
files = listdir(".") # листинг текущей директории
LogFilesNames = filter(lambda x: x.endswith('.log'), files) # отобрать все лог файлы
print('Number of files:',len(LogFilesNames))
for n in LogFilesNames:    # цикл по именам фалов
    f = codecs.open(n,'r+','utf_8_sig').readlines() # читаем строки каждого файла
    for i in [15,16]: # цикл по номерам строк
        f[i]='-- pte_deleted@serebrennikovn --\n' # правим 16 и 17 строки в файле
    with codecs.open(n,'w','utf_8_sig') as F:
        F.writelines(f) # применение изменений в файле
        print('Applying in file: ',F.name) # вывод имени обработанного файла









