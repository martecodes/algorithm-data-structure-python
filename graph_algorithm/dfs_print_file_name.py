from os import listdir
from os.path import isfile, join

def print_names(dir):
    for file in sorted(listdir(dir)):
        fullpath = join(dir, file)
        if isfile(fullpath):
            print(file)
        else:
            print_names(fullpath)


print_names('/Users/marte/Desktop/algorithm-data-structure-python')