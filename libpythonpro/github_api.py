import requests


def buscar_avatar(usuario):
    """
    Buscar o avatar de um usuario no Github
    :param usuario: str com o nome de usuario no github
    :return: str com o link do avatar
    """
    url = f'https://api.github.com/users/{usuario}'
    r = requests.get(url)
    return r.json()['avatar_url']
