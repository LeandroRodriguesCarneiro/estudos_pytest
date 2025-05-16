import pytest
from database_manager import DatabaseManager, Cliente

@pytest.fixture
def make_conection():
    test_db_path = 'users.db'
    db_manager = DatabaseManager(test_db_path)
    yield db_manager


@pytest.mark.parametrize(
    "Cliente",[
        Cliente("John Doe", "", "", "", "", "", "", "", ""),
        Cliente("", "johndoe@example.com", "", "", "", "", "", "", ""),
        Cliente("", "", "1234567890", "", "", "", "", "", ""),
        Cliente("", "", "", "1234 Elm Street", "", "", "", "", ""),
        Cliente("", "", "", "", "Springfield", "", "", "", ""),
        Cliente("", "", "", "", "", "SP", "", "", ""),
        Cliente("", "", "", "", "", "", "12345-678", "", ""),
        Cliente("", "", "", "", "", "", "", "2023-03-15", ""),
        Cliente("", "", "", "", "", "", "", "", "1990-01-01"),
        Cliente("John Doe", "johndoe_example.com", "", "", "", "", "", "", ""),
        Cliente("John Doe", "johndoe@example.com", "", "", "", "", "", "", ""),
        Cliente("John Doe", "johndoe@example.com", "1234567890", "", "", "", "", "", ""),
        Cliente("John Doe", "johndoe@example.com", "1234567890", "1234 Elm Street", "", "", "", "", ""),
        Cliente("John Doe", "johndoe@example.com", "1234567890", "1234 Elm Street", "Springfield", "", "", "", ""),
        Cliente("John Doe", "johndoe@example.com", "1234567890", "1234 Elm Street", "Springfield", "SP", "", "", ""),
        Cliente("John Doe", "johndoe@example.com", "1234567890", "1234 Elm Street", "Springfield", "SP", "12345-678", "", ""),
        Cliente("John Doe", "johndoe@example.com", "1234567890", "1234 Elm Street", "Springfield", "SP", "12345-678", "2023-03-15", ""),
    ]
)
def test_cliente_flaha_com_dados_invalidos(make_conection, Cliente):
    resultado = make_conection.incluir_cliente(Cliente)
    assert resultado == "Falha na validação dos dados do cliente."

def test_cliente_existente(make_conection):
    resultado = make_conection.validar_id(1)
    assert resultado == True

def test_cliente_existente(make_conection):
    resultado = make_conection.validar_id(999)
    assert resultado == False

@pytest.mark.parametrize(
        'id, campo, valor_novo',
        [
            (1, 'email', 'johndoe@gmail.com')
        ]
)
def test_atualizar_cliente(make_conection, id, campo, valor_novo):
    resultado = make_conection.atualizar_cliente(id, campo, valor_novo)
    assert resultado > 0