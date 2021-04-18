import requests


# GET Avaliacoes

# avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes')

# Acessando o código de status HTTP.
# print(avaliacoes.status_code)

# Acessando os dados da resposta
# print(avaliacoes.json())
# print(type(avaliacoes.json())) # Tipo dict, não é JSON na verdade.

# Acessando a quantidade de registros
# print(avaliacoes.json()['count'])

# Acessando a próxima página de resultados
# print(avaliacoes.json()['next'])

# Acessando os resultados dessa página
# print(avaliacoes.json()['results'])
# print(type(avaliacoes.json()['results'])) # Tipo list, não é JSON na verdade.

# Acessando o primeiro elemento da lista de resultados
# print(avaliacoes.json()['results'][0])

# Acessando o último elemento da lista de resultados
# print(avaliacoes.json()['results'][-1])

# Acessando somente o nome da pessoa que fez a última avaliação
# print(avaliacoes.json()['results'][-1]['nome'])


#GET Avaliacao
# avaliacao = requests.get('http://localhost:8000/api/v2/avaliacoes/7')

# print(avaliacao.json())

headers = {'Authorization' : 'Token e5d64d3685fe983b97e02a0be3ef6d89ccb765f4'}

# GET Cursos
cursos = requests.get(url='http://localhost:8000/api/v2/cursos', headers=headers)
print(cursos.status_code)
print(cursos.json())
