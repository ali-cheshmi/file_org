
import os
import glob

# make a list of files in current directory
my_files=glob.glob('*')
#print(my_files)
#create a empty set
ext_set=set()

#get extention of files in move to set
for i in my_files:
    try:
        ext=i.split('.')[1]
        ext_set.add(ext)
    except:
        pass

#create folder foe each extention
def create_folder():
    for i in ext_set:
        if i=='py':
            continue
        try:
            os.makedirs(i+'_files')

        except:
            pass

#move files to folders that created
def move_file():
    for i in my_files:
        exte=i.split('.')[1]
        try:
            os.rename(i,exte+ '_files/'+i)
        except:
            pass
                    
                      
#call functions
create_folder()
move_file()