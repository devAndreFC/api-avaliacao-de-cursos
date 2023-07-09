import requests


headers = {'Authorization': 'Token 566a1c738ed0c2d2e32fb4866dec5ddd9dd829b6'}
url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_av = 'http://localhost:8000/api/v2/avaliacoes/'

resultado = requests.delete(url=f'{url_base_cursos}14/', headers=headers)

# testando codigo http
assert resultado.status_code == 204

# testando se o tamanho do conteúdo do retorno é == 0
assert len(resultado.text) == 0

