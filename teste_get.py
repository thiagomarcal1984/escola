import requests

headers = {'Authorization' : 'Token e5d64d3685fe983b97e02a0be3ef6d89ccb765f4'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

resultado = requests.get(url=url_base_cursos, headers=headers)

# print(resultado.json())

# Testando se o endpoint está correto
assert resultado.status_code == 200

# Testando a quantidade de registros
assert resultado.json()['count'] == 4

# Testando se o título do primeiro curso está correto
assert resultado.json()['results'][0]['titulo'] == 'Programação com JavaScript'
