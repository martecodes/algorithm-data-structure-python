from os import listdir
from os.path import isfile, join
from collections import deque

def print_names(start_dir):
    search_deque = deque()
    search_deque.append(start_dir)
    
    while search_deque:
        dir = search_deque.popleft()   
        for file in sorted(listdir(dir)):
            fullpath = join(dir, file)
            if isfile(fullpath):
                print(file)
            else:
                search_deque.append(fullpath)


print_names('/Users/marte/Desktop/algorithm-data-structure-python')