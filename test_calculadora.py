def test_sum():
    assert 3 + 2 == 5
    assert sum([i for i in range(4)]) == 6

def test_len():
    assert len([i for i in range(4)]) == 4

def test_min():
    assert min([i for i in range(4)]) == 0

def test_max():
    assert max([i for i in range(4)]) == 3