import pytest
from convert import convert
def test_conversation():
    assert convert(1) == 149597870700
    assert convert(50) == 7479893535000
def test_error():
    with pytest.raises(TypeError):
        convert("1")
def test_float_conversation():
    assert convert(0.0001) ==pytest.approx(14959787.07)