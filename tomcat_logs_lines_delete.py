from os import listdir
files = listdir(".") # листинг текущей директории
LogFilesNames = filter(lambda x: x.endswith('.log'), files) # отобрать все лог файлы
print('Files:',len(LogFilesNames))
lc=0
for n in LogFilesNames:    # цикл по именам файлов
    f = open(n,'r+').readlines() # читаем строки каждого файла
    print('File: ',n,'Lines: ',len(f)) 
    for i in range(len(f)): # цикл по номерам строк
        if 'pte_deleted' in f[i]:
            pass
        elif 'c.s.s.c.jdbc.query.ScriptQuery - pan'  in f[i]:# условие сравнения 
            f[i]='-- c.s.s.c.jdbc.query.ScriptQuery - pan: pte_deleted@serebrennikovn --\n' # правка строк в файле
            lc+=1
        elif 'c.s.s.c.jdbc.query.ScriptQuery - contractNumber'  in f[i]: 
            f[i]='-- c.s.s.c.jdbc.query.ScriptQuery - contractNumber: pte_deleted@serebrennikovn --\n'
            lc+=1
    with open(n,'w') as F:
        F.writelines(f) # применение изменений в файле
        print('Edited lines: ',lc) # вывод числа отредактированных строк
        print('Applying in file: ',F.name) # вывод количества обработанных файлов
        






