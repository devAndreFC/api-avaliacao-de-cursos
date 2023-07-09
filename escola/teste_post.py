import requests


headers = {'Authorization': 'Token 566a1c738ed0c2d2e32fb4866dec5ddd9dd829b6'}
url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_av = 'http://localhost:8000/api/v2/avaliacoes/'

novo_curso = {
    "titulo": "Gerencia de projetos 3",
    "url": "http://www.gerencia3.com"
}

resultado = requests.post(
    url=url_base_cursos, 
    headers=headers, 
    data=novo_curso
    )

# testando o codigo de status http 201
assert resultado.status_code == 201

# testando se titulo do curso criado é o mesmo do informado
assert resultado.json()['titulo'] == novo_curso['titulo']