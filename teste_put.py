import requests

headers = {'Authorization' : 'Token e5d64d3685fe983b97e02a0be3ef6d89ccb765f4'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

curso_atualizado = {
    "titulo" : "Novo Curso de Scrum 2",
    "url" : "http://www.geekuniversity.com/scrum2"
}

# Buscando o curso com o ID 10
# curso = requests.get(url=f'{url_base_cursos}10/', headers=headers)
# print(curso.json())

resultado = requests.put(url=f'{url_base_cursos}10/', headers=headers, data=curso_atualizado)

# Testando o código de status HTTP 200
assert resultado.status_code == 200

# Testando se o título do curso retornado é o mesmo do informado
assert resultado.json()['titulo'] == curso_atualizado['titulo']

