from distutils import extension
import os
import shutil
from_dir= "C:/Users/dell/Downloads"
to_dir="C:/Users/dell/Documents/Document_Files"
list_of_files=os.listdir(from_dir)
#print(list_of_files)
for checkeachfilename in list_of_files:
    name,extension=os.path.splitext(checkeachfilename)
    if extension == '':
        continue
    if extension in['.png','.jpg','.gif','.jpeg','.jfif']:
        p1=from_dir + '/'+ checkeachfilename
        p2=to_dir + '/' + "Images"
        p3=to_dir + '/' + "Images" + '/' + checkeachfilename
        print(p1)
        print(p3)
    