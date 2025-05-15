import pytest
from time import sleep

@pytest.mark.lento
def test_soma_lenta():
    sleep(2)
    assert 1 + 1 == 2

@pytest.mark.rapido
def test_soma():
    assert 1 + 1 == 2

@pytest.mark.lento
def test_multi_lenta():
    sleep(2)
    assert 1 * 1 == 1

@pytest.mark.rapido
def test_multi():
    assert 1 * 1 == 1

@pytest.mark.rapido
@pytest.mark.lento
def test_soma_mista():
    sleep(1)
    assert 1+2 == 3

def test_exponential():
    assert 2 ** 2 == 4