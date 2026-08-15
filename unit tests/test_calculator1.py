from calculator import square
def main():
    test_square()
def test_square():
    assert square(2) == 4 #In Python, assert is used to check that something is true.
    #If the condition is false, Python raises an AssertionError.
    """assert is mainly for debugging and tests.
    Don’t use it for important runtime validation like passwords, permissions, or user input, 
    because Python can disable assertions when run with optimization mode: python -O."""
    assert square(3) == 9
if __name__ == "__main__":
    main()