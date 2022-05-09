import pytest as pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize('remetente',
                         ['jairo@python.com.br', 'foooba@foll.com.br']
                         )
def test_remetente(remetente):
    enviador = Enviador()
    res = enviador.enviar(
        remetente,
        'renzo@pythonpro.com.br',
        'Curso Pytools',
        'Atualização Curso Pytools'
    )
    assert res == remetente


@pytest.mark.parametrize('remetente',
                         ['', 'foooba']
                         )
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'renzo@pythonpro.com.br',
            'Curso Pytools',
            'Atualização Curso Pytools'
        )
