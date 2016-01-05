#This is version 3
#On lines 17 of version 2 I write that I think strings are directories and lists are files.
#That's when I thought that if I was right. I could simplify absfiles() so I tried it and it works.
#I tested if the lists returned by the function absfiles in files2.py and files3.py were the same
#by importing files2 in here, and they are.
from os.path import abspath
from os import walk
from os.path import join
from re import findall
from sys import argv

def files(dir):
    ''' 
    I wrote this function to help me list all directories, 
    subdirectories and files in these directories and subdirectories.
    '''
    path = abspath(dir)
    files_dirs = walk(path) #files_dirs is an object
    files = []
    for filesordirs in files_dirs: #this gives me filesordirs, a tuple, with everything that was in files_dirs
        for item in filesordirs: #some items are strings(dirs, I know now) others lists(files, I know now)
            if item == list(item):
                for n in item:
                    files.append(n)
            else:
                files.append(item)
    return files
    
def absfiles(dir):
    '''
    This one lists them with their absolute path.
    '''
    path = abspath(dir)
    files_dirs = list(walk(path))
    absfiles = []
    for filesordirs in files_dirs:
        for item in filesordirs:
            if item == str(item): 
                path = item #since everything after a directory has it as its absolute path
            if item == list(item):
                for file in item:
                    absfiles.append(join(path, file)) #following the reasoning stated above
    return absfiles
    
def main():
    args = argv
    dir = args[1]
    absfiles(dir)
    # Need to set things up to work with both functions
    # with different usage forms: script [-files -absfiles] dir
    
if __name__ == '__main__':
    main()
