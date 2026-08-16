from hello import hello
def test_argument():
    for name in ["yash","ram","prasanna"]:
        assert hello(name) == f"hello to,{name}"