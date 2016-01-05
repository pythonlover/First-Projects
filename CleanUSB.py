#This script is meant to work on a windows PC with only 2 USB ports.
#Maybe I'll expand it to be more general later, but for now this is what I need.
from sys import exit
from subprocess import call
from os.path import exists
from time import sleep
from msvcrt import getch

#find a module that shows active usb drives, until then
#------------------------------------------------------
drives = []
if exists('E:'):
    drives.append('E')
if exists('F:'):
    drives.append('F')
#------------------------------------------------------
#find a module that shows active usb drives, until then

#print USB drives
print drives

drive = raw_input('Which drive do you want to unhide? ')

def unhide():
    cmd = 'attrib -r -s -h /s /d'
    call(['powershell','cd %s:\n'%drive, cmd])

def abort():
	print "Goodbye."
	sys.exit(0)
    
print "About to do:\n\tpowershell\n\tcd %s:\n\t%s" %(drive, cmd)
print "Press ENTER to continue or CTRL-C to abort."
c = getch()
if c == '\r':
    unhide()
if c == '\x03':
    abort()


#add a function or 2 and organize all of this
