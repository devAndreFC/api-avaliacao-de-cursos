import requests
import jsonpath


avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')
# resultados = jsonpath.jsonpath(avaliacoes.json(), 'results')
# print(resultados)

# primeiro = jsonpath.jsonpath(avaliacoes.json(), 'results[0]')
# print(primeiro)

# nome = jsonpath.jsonpath(avaliacoes.json(), 'results[0].nome')
# print(nome)

# nota = jsonpath.jsonpath(avaliacoes.json(), 'results[0].nota')
# print(nota)

# curso_id = jsonpath.jsonpath(avaliacoes.json(), 'results[0].curso')
# print(curso_id)

# todos os nomes das pessoas que avaliaram o curso
# nomes = jsonpath.jsonpath(avaliacoes.json(), 'results[*].nome')
# print(nomes)

# todos as notas das pessoas que avaliaram o curso
notas = jsonpath.jsonpath(avaliacoes.json(), 'results[*].nota')
print(notas)