import sys

try:
    sys.exit("hello, my name is", sys.argv[1])
except IndexError:
    sys.exit("Too few arguments")
