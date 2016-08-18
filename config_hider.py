from os import listdir
files = listdir(".") # листинг текущей директории
LogFilesNames = filter(lambda x: x.endswith('.properties'), files) # отобрать все properties файлы
print('Files:',len(LogFilesNames))
lc=0
ListOfPars=[
	'smppadapter_smpp_password_r=',
	'smppadapter_smpp_password_t='
]
for n in LogFilesNames:    # цикл по именам файлов
    f = open(n,'r+').readlines() # читаем строки каждого файла
    print('File: ',n,'Lines: ',len(f)) 
    for i in range(len(f)): # цикл по номерам строк
        for m in range(len(ListOfPars)): #цикл по сиску параметров ListOfPars
            if 'pte_deleted' in f[i]:
                pass
            elif ListOfPars[m] in f[i]: # условие сравнения
                if f[i][0]=='#':
                    f[i]=('#'+ListOfPars[m]+'*pte_deleted@serebrennikovn*\n') # правка строк в файле
                    lc+=1
                else:
                    f[i]=(ListOfPars[m]+'*pte_deleted@serebrennikovn*\n') # правка строк в файле
                    lc+=1
    with open(n,'w') as F:
        F.writelines(f) # применение изменений в файле
        print('Edited lines: ',lc) # вывод числа отредактированных строк
        print('Applying in file: ',F.name) # вывод имени обработанного файла
