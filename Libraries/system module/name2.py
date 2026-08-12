import sys
#check error in command line arguments
if len(sys.argv) < 2:
    sys.exit("to few arguments") #sys.exit() is used to exit the program with an error message
elif len(sys.argv) > 2:
    sys.exit("too many arguents")#sys.exit() stops the script rigth there
#print name tags
print("hello my name is ",sys.argv[1])