#This is version 2
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
        for item in filesordirs: #some items are strings(dirs, I think) others lists(files, I think)
            if item == list(item):
                for n in item:
                    files.append(n)
            else:
                files.append(item)
    return files
    
def absfiles(dir):
    '''
    This one lists their absolute path.
    '''
    path = abspath(dir)
    files_dirs = list(walk(path))
    files = []
    for filesordirs in files_dirs:
        for item in filesordirs:
            if item == list(item):
                for n in item:
                    files.append(n)
            else:
                files.append(item)
    
    index_of_dir = []
    for thing in files:
        # If thing is a path index the position.
        if findall(r'C:.+', thing): #This technique means it's not platform independent so I will change it.
            index_of_dir.append(files.index(thing))
    
    absfiles = []
    for num in index_of_dir:
        path = files[num]
        
        try:
            next_dir_index = index_of_dir[index_of_dir.index(num)+1]
        except IndexError:
            next_dir_index = None
        
        first_file_index = num + 1
        # I take the files between one directory and the one after it.
        # Those are the files for which their path is the first directory.
        for file in files[first_file_index: next_dir_index]:
            pathname = join(path, file)
            absfiles.append(pathname)
    return absfiles
    
def main():
    args = argv
    dir = args[1]
    absfiles(dir)
    # Need to set things up to work with both functions
    # with different usage forms: script {-files -absfiles} dir
    
if __name__ == '__main__':
    main()
