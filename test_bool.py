def is_positive(num):
    return num > 0

def test_is_positive():
    assert is_positive(5) is True
    assert is_positive(-5) is False