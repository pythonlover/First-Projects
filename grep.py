import sys

def grep(*matches):
    """Returns a generator function that operates on an iterable:
        filters items in the iterable that match any of the patterns.

    match: a callable returning a True value if it matches the item

    >>> import re
    >>> input = ["alpha\n", "beta\n", "gamma\n", "delta\n"]
    >>> list(grep(re.compile('b').match)(input))
    ['beta\n']
    """
    def _do_grep_wrapper(*matches):
        def _do_grep(lines):
            for line in lines:
                for match in matches:
                    if match(line):
                        yield line
                        break
        return _do_grep
    return _do_grep_wrapper(*matches)

args = sys.argv
if len(args) <= 1:
    print "Usage: [python] grep.py filename whatever-you-are-looking-for"
    print "If there is nothing in place of whatever-you-are-looking-for the script acts like the cat command"
    sys.exit(1)
else:
    filename = args[1]
    file = open(filename, 'r')
    patterns = args[2:]
    patt = ''
    for pattern in patterns:
        patt = patt + ' ' + pattern
    pattern = patt[1:].lower()
    print "Looking for %r in %r." %(pattern, filename)
    grepper = grep(lambda line: pattern in line.lower())
    matched = grepper(file)
    text = ''
    for line in list(matched):
        text += line
    print text [1:]   
