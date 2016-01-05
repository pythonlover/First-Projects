''' 
I wrote this function to help me list all directories, 
subdirectories and files in these directories and subdirectories.
'''
from os.path import abspath
from os import walk
from os.path import join
from re import findall
from sys import argv

def files(dir):
    path = abspath(dir)
    dirs = list(walk(path))
    files = []
    for dir in dirs:
        for item in dir:
            if item == list(item):
                for n in item:
                    files.append(n)
            else:
                files.append(item)
    return files
    
def absfiles(dir):
    path = abspath(dir)
    dirs = list(walk(path))
    files = []
    for dir in dirs:
        for item in dir:
            if item == list(item):
                for n in item:
                    files.append(n)
            else:
                files.append(item)
    l = len(files)
    listofdir = []
    for n in range(l):
        if findall(r'C:.+', files[n]): 
        # If it's a path index the position.
            listofdir.append(n)

    d = {}
    for k in listofdir:
        d[k] = files[k]
        
    absfiles = []
    for num in listofdir:
        path = d.get(num)
        d.pop(num)

        try:
            for file in files[num+1:sorted(d.keys())[0]]:
                pathname = join(path, file)
                absfiles.append(pathname)
        except IndexError:
            #print "IndexError: because %r" %d.items()
            pass
    return absfiles
    
def main():
    args = argv
    dir = args[1]
    files(dir)
    # Need to set things up to work with both functions
    # with different usage forms: script {-files -absfiles} dir
    
if __name__ == '__main__':
    main()
