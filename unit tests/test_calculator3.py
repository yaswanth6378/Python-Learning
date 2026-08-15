from calculator import square
def test_square():
    try:
        assert square(2)==4
    except AssertionError:
        print("2 square was not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 sqaure was not 4")
    try:
        assert square(-2) == 4
    except AssertionError:
        print("-2 square was not 4")
    try:
        assert square(-3) == 9
    except AssertionError:
        print("-3 square was not 9")
    try:
        assert square(0) == 0
    except AssertionError:
        print("0 was not 0")