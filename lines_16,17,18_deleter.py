import codecs, os
files = os.listdir(".") # листинг текущей директории
LogFilesNames = filter(lambda x: ('.log' in x), files) # отобрать все лог файлы
print'Files in a directory:',len(LogFilesNames)
for n in LogFilesNames:    # цикл по именам фалов
    f = codecs.open(n,'r+','utf_8_sig').readlines() # читаем строки каждого файла
    try: 
	for i in [15,16,17]: # цикл по номерам строк
	    if 'pte_deleted' in f[i]: # если уже удалены
                pass
            else:
                f[i]='-- pte_deleted@serebrennikovn --\n' # правим 16 17 18 строки в файле
                with codecs.open(n,'w','utf_8_sig') as F:
                    F.writelines(f) # применение изменений в файле
                    print'Applying in file: ',F.name # вывод имени обработанного файла
    except IndexError: # исключение для пустого файла
	print'Skip empty file: ',n
