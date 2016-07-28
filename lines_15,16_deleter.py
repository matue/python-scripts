import codecs
from os import listdir
files = listdir(".") # listing of the current directory
logfilesnames = filter(lambda x: x.endswith('.log'), files) # select *.log files
for n in logfilesnames:    # by filename cycle
    f = codecs.open(n,'r+','utf_8_sig').readlines() #[n cycle] reading lines from each file
    for i in [15,16]: # line numbers cycle
        f[i]='--deleted--\n' # [cycle] edit 16 and 17 lines in the file
    with codecs.open(n,'w','utf_8_sig') as F:
        F.writelines(f) # [cycle] inscribing changes into the file 
        print('Been edited file: ',F.name) # [cycle] Displays the name of the edited file




