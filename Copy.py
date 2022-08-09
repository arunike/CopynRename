import os
import shutil

print('Enter the search keyword: ', end = '')
keyword = input()

print('Enter the general location of where the files are stored: ', end = '')
source_folder = input()

print('Enter a location to where you save the output file: ', end = '')
dst_folder = input()

for path, subdirs, files in os.walk(source_folder):
    for name in files:
        if(name.startswith(keyword) & name.endswith(".pptx")):

            new_location = shutil.copy(os.path.join(path, name), dst_folder)

print('Done!')