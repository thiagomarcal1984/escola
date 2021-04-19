import requests

headers = {'Authorization' : 'Token e5d64d3685fe983b97e02a0be3ef6d89ccb765f4'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'


resultado = requests.delete(url=f'{url_base_cursos}10/', headers=headers)

# Testando o código de status HTTP 204
assert resultado.status_code == 204

# Testando se o tamanho do conteúdo retornado é 0.
assert len(resultado.text) == 0
