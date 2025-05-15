import pytest

def verificar_idade(idade:int):
    if idade < 18:
        raise ValueError("Acesso negado para menore de 18 anos")
    return "Acesso perimitido"

def division(a:int, b:int):
    if b == 0:
        raise ZeroDivisionError("Não é possível dividir por zero")
    return a / b

def test_verifica_idade_erro():
    with pytest.raises(ValueError):
        verificar_idade(17)

def test_verifica_idade():
    assert verificar_idade(18) == "Acesso perimitido"

def test_dision_for_zero():
    with pytest.raises(ZeroDivisionError):
        division(0,0)

def test_division_for_zero2():
    with pytest.raises(ZeroDivisionError) as exec_info:
        division(0, 0)
    assert "Não é possível dividir por zero" in str(exec_info.value)
