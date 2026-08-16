from hello import hello
def test_hello():
    assert hello ("yaswanth") == "hello to,yaswanth"
    assert hello() == "hello to,world"