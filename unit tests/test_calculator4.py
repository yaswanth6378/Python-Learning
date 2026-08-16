from calculator import square
def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0
    """instead of having one bif function like def test_square ,lets break down my function into different catogireies
    separating big function intpo multiplesmall  functions gives us more clues clues"""
    # go check test_calculator5.py to know  how it works