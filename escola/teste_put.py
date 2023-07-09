import requests


headers = {'Authorization': 'Token 566a1c738ed0c2d2e32fb4866dec5ddd9dd829b6'}
url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_av = 'http://localhost:8000/api/v2/avaliacoes/'

curso_att = {
    "titulo": "Gerencia de projetos ATT",
    "url": "http://www.gerenciaATT.com"
}

# cruso14 = requests.get(f'{url_base_cursos}14/', headers=headers)
# assert cruso14.status_code == 200

resultado = requests.put(
    url=f'{url_base_cursos}14/', 
    headers=headers, 
    data=curso_att
    )

# testando codigo HTTP
assert resultado.status_code == 200

# testando titulo 
assert resultado.json()['titulo'] == curso_att['titulo']