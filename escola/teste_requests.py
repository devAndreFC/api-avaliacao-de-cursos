import requests


#GET avaliações
# avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')

# print(f'Acessando avaliações: {avaliacoes.status_code}')

# print(f'Acessando dados das av : \n{avaliacoes.json()}')
# print(f'Acessando quantidade de registros: {avaliacoes.json()["count"]}')
# print(f'Acessando resultados das avaliações:\n {avaliacoes.json()["results"]}')
# print(f'Acessando 1º resultado das avaliações:\n {avaliacoes.json()["results"][0]}')
# print(f'Acessando ultimo resultado das avaliações:\n {avaliacoes.json()["results"][-1]}')
# print(f'Acessando nome do ultimo resultado das avaliações:\n {avaliacoes.json()["results"][-1]["nome"]}')

# GET Avaliação
# avaliacao = requests.get('http://localhost:8000/api/v2/avaliacoes/1')
# print(f'Acessando av 7: {avaliacao.status_code}')

# GET Curso
headers = {'Authorization': 'Token 566a1c738ed0c2d2e32fb4866dec5ddd9dd829b6'}
cursos = requests.get(url='http://localhost:8000/api/v2/cursos/', headers=headers)
print(cursos.status_code)
print(cursos.json())