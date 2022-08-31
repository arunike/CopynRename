## Imports
import os
import shutil

## Copy Function
def Copy(): 

    ## User Input
    print('Enter the search keyword: ', end = '')
    keyword = input()

    print('Enter the general location of where the files are stored: ', end = '')
    source_folder = input()

    print('Enter a location to where you save the output file: ', end = '')
    dst_folder = input()

    ## Search for files
    for path, files in os.walk(source_folder):
        for name in files:
            if(name.startswith(keyword) & name.endswith(".pptx")):

                shutil.copy(os.path.join(path, name), dst_folder) ## Copy file to destination folder

    print('Done!')

Copy()
