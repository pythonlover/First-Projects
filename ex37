''' Keywords '''
a = 12 # this is global by default
def BigGlobal():
    def Global():
        global b
        b = a * 2
        c = a * 4
        print b, c
    Global()
    print b, c # c won't print because it's not global

def Break(): #read up more in the python documentation
    for n in range(2,10):
        for x in range(2,n):
                if n%x == 0:
                        print n, '=', x, '*', n/x
                        break
        else:
                print n, "is a prime number"

def Continue():#read up more in the python documentation
    for num in range(2,10):
        if num % 2 == 0:
            print "Found an even number:", num
            continue
        print "Found a number", num
 
def Pass():
    while True:
        pass # Busy wait for keyboard interrupt (Ctrl+C)

# This function is for the sake of doing it like the others, just try the lines below in the interpreter        
def Lambda(): 
    f = lambda x: x + 1
    f(3) # = 4

def Yield():
    def f():
        a = [1, 2, 3]
        for num in a:
            yield num
    list = f()

def Assert(): #read up more in the python documentation
    assert True #this returns True
    assert False, "You have a False assertion" #this returns an error
    assert 2/0, ZeroDivisionError #this raises ZeroDivisionError
    
def Exec():
    exec 'print hey'
    exec 'print hey' in {'bye':1, 'selam':2, 'hey':3} # this prints 3
    exec 'print open(hey, "r").read()' in {'bye':'ex1.py', 'py':'ex37.py', 'hey':'test.txt'}
    file = open('ex36.py', 'r')
    exec file #this will execute ex36.py as if I was clearing the shell then running python ex36.py
    tuple = ('import os', "os.listdir('.')") #I don't understand how to do this
    exec tuple #I don't understand how to do this

def Exceptions():
    import os
    from time import sleep
    all = os.listdir('.')
    try:
        for thing in all:
            print open(thing, 'r').read()
    except IOError:
        print "Can't read this file/folder"
        sleep(3)
    except KeyboardInterrupt:
        print "This was a KeyboardInterrupt"
        sleep(3)
    #this runs if there is an exception in try but it's not the ones cited before: IOError and KeyboardInterrupt in this e.g.
    #try it with dir as '../' and change IOError to something unlikely like BytesWarning
    except: 
        print "Unknown Error"
        sleep(3)
        raise #this raises the error no matter what, after the finally statement
        # Because I didn't write what error it will print the real one if I add an error (like KeyboardInterrupt)
        # after 'raise' then that's what will be shown
    else: #when there is no exception (like when the dir is '.') this is run
        print "No errors at all"
        sleep(3)
    finally: #this is run no matter what even if there's an exception then this is run then the exception/error is showed
        print "Goodbye world!"
        
def With():
    with open('ex37.py', 'r') as f:
        print f.read()
    print f.read() #This will give me an error because the file is cleaned-up (meaning closed)
    print f #This will just say that it's closed, i.e. f is still the file object
    
def Is():
    print 4 is 4 #True
    print 4 is not 5 #True
    print 4 is 5 #False
    print 4 is not 4#False
    a = 15
    b = 'a'#None #or 1 or 2 or 'a' or anything
    b is a
    print a #15, although this won't work in the interpreter
    return
    
    
    
''' String Escape Sequences '''
def StringEscapeSequences():
    print "\\b backspace:"
    print "Hello\\b", '\t:\t', "Hello\b"
    print "Hello\\bMate", '\t:\t', "Hello\bMate"
    print "Hello \\bMate", '\t:\t', "Hello \bMate"
    print '\n'
    print "\\r carriage return:"
    print "Hey\\r", '\t:\t', "Hey\r"
    print "Hey\\rBob", '\t:\t', "\nHey\rBob"
    print "Hey \\rBob", '\t:\t', "\nHey \rBob"
    print "Bonjourno\\rAman", '\t:\t', "\nBonjourno\rAman"
    print "Bonjourno \\rAman", '\t:\t', "\nBonjourno \rAman"
    return
    
    
    
''' String Formats '''
def StringFormats():
    print "'\%d'\%5", '\t:\t', "%d"%5
    print "'\%i'\%5", '\t:\t', "%i"%5
    print "'\%o'\%5", '\t:\t', "%o"%5
    print "'\%u'\%5", '\t:\t', "%u"%5
    print "'\%x'\%5", '\t:\t', "%x"%5
    print "'\%X'\%5", '\t:\t', "%X"%5
    print "'\%e'\%5", '\t:\t', "%e"%5
    print "'\%E'\%5", '\t:\t', "%E"%5
    print "'\%f'\%5", '\t:\t', "%f"%5
    print "'\%F'\%5", '\t:\t', "%F"%5
    print "'\%g'\%5", '\t:\t', "%g"%5
    print "'\%G'\%5", '\t:\t', "%G"%5
    print "'\%c'\%5", '\t:\t', "%c"%5
    print "'\%r'\%5", '\t:\t', "%r"%5
    print "'\%s'\%5", '\t:\t', "%s"%5
    print "'\%%'\%5", '\t:\t', "%%"%.5
    return
   

   
''' Operators '''
def At(): #read up more in the python documentation
    def decorator(func):
        return func
        
    @decorator
    def some_func():
            return
