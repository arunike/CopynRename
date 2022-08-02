import os, datetime
import shutil

print('Enter the keyword of the files you want to copy: ', end = '')
keyword = input()

print('Enter the general location of where the files is store: ', end = '')
source_folder = input()

print('Enter a location to where you would like to store you files: ', end = '')
dst_folder = input()

for path, subdirs, files in os.walk(source_folder):
    for name in files:
        if(name.startswith(keyword) & name.endswith(".pptx")):
            filetime = datetime.datetime.fromtimestamp(os.path.getmtime(os.path.join(path, name)))
            new_location = shutil.copy(os.path.join(path, name), dst_folder)