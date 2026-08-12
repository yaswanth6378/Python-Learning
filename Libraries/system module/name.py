import sys
try:
    print("hello my name is", sys.argv[1])#prints the first command-line argument passed to the script,
    #which is expected to be the user's name
except IndexError:
    print("Please provide your name as a command-line argument.")