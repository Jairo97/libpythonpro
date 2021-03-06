from unittest.mock import Mock

import pytest
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Jairo', email='oliveirajairon10@gmail.com'),
            Usuario(nome='Jairo', email='oliveirajairon10@gmail.com')
        ],
        [
            Usuario(nome='Jairo', email='oliveirajairon10@gmail.com')
        ]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'oliveira@hotmail.com',
        'Curso de Python',
        'Modulos Fantasticos'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Jairon', email='oliveirajairon10@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'oliveira@hotmail.com',
        'Curso de Python',
        'Modulos Fantasticos'
    )
    enviador.assert_called_once_with = (
        'oliveira@hotmail.com',
        'oliveirajairon10@gmail.com',
        'Curso de Python',
        'Modulos Fantasticos'
    )
