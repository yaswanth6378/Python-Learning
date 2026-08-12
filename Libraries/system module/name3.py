import sys
def main():

    if len(sys.argv) < 2 :
        sys.exit("too few arguments")
    for name in sys.argv[1:]:
        yash_red(name)
def yash_red(name):
    print("hello my name is ",name)
if __name__ == "__main__":
    main()