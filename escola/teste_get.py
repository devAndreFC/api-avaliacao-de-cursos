import requests


headers = {'Authorization': 'Token 566a1c738ed0c2d2e32fb4866dec5ddd9dd829b6'}
url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_av = 'http://localhost:8000/api/v2/avaliacoes/'

resultado = requests.get(url=url_base_cursos, headers=headers)
# print(resultado.json())

# testando se endpoint está correto
assert resultado.status_code == 200

# testando quantidade de registros
assert resultado.json()['count'] == 4

#testando o título do 1 elemento está correto
assert resultado.json()['results'][0]['titulo'] == 'Curso legal'