import pytest

@pytest.mark.parametrize('a, b, result', 
    [
        (1, 2, 3), (4, 5, 9), (10, 20, 30)    
    ]
)
def test_soma(a, b, result):
    assert sum([a, b]) == result