# import the modules
from sys import argv

# get the command line arguments
script, filename = argv

# open the file
txt = open(filename)

# prints the contents of the file to the screen
print "Here's your file %r:" %filename
print txt.read()

# get filename from the user
print "Type the filename again:"
file_again = raw_input("> ")

# open the filename
txt_again = open(file_again)

# prints the contents of the file to the screen
print txt_again.read()