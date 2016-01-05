import sys, re, glob, os

def renamer(files, pattern, replacement):
	# this gives me the immediate path and filename (I used in the command line)
	# e.g. ../../file.txt instead of c:/users/file.txt --> abspath or just 
	# file.txt(if that's what I used) instead of c:/users/file.txt
    for pathname in glob.glob(files):
        filename = os.path.basename(pathname) # this gives me just the filename, ie. without the path
        new_filename = re.sub(pattern, replacement, filename) # substitute pattern with replacement in the fileename
        if new_filename != filename: # check if renaming is actually necessary
            os.rename(pathname, os.path.join(os.path.dirname(pathname), new_filename)) # rename

def main():
	args = sys.argv[:]
	script = args[0]#sys.argv[0]
	args.pop(0)
	if len(args) == 3:
		renamer(args[0], args[1], args[2])
	else:
		print 'usage: %s files pattern replacement' %script
		sys.exit(1)

if __name__ == "__main__":
	main()
