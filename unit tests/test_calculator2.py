# I used assert to check whether the square function returns the correct value.
# If the expected value is not returned, AssertionError is handled using except
# and a custom error message is printed.




from calculator import square
def main():
    test_square()
def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("square of 2 was not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("square of 3 was not 9")
    try:
        assert square(-2) == 4
    except AssertionError:
            print("square of -2 was not 4 ")
    try:
        assert square(-3) == 9
    except AssertionError:
        print("square of -3 was not 9")
    try:
        assert square(0) == 0
    except AssertionError:
        print("square of 0 was not 0")
if __name__ == "__main__":
    main()
    
    """Like  this we cant write write this much bigcode every time to test 2 lines of function. 
    to solve easily we have third party library pytesr which we can install through pip install pytest 
    designed automate testing of our code
    """
    # go check test_calculator3.py to know how to use pytest