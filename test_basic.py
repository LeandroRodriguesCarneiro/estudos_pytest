import pytest

@pytest.fixture
def sample_list():
    return [i for i in range(6)]



def test_sum(sample_list):
    assert sum(sample_list) == 15

def test_lenght(sample_list):
    assert len(sample_list) == 6