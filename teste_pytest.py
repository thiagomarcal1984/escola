import requests

class TestCurso:
    headers = { 'Authorization' : 'Token e5d64d3685fe983b97e02a0be3ef6d89ccb765f4'}
    url_base_cursos = 'http://localhost:8000/api/v2/cursos/'

    def test_get_cursos(self):
        resposta = requests.get(url=self.url_base_cursos, headers=self.headers)

        assert resposta.status_code == 200

    def test_get_curso(self):
        resposta = requests.get(url=f'{self.url_base_cursos}9/', headers=self.headers)

        assert resposta.status_code == 200

    def test_post_curso(self):
        novo = {
            "titulo" : "Curso de Programação com Ruby",
            "url" : "http://www.geekuniversity.com/cpr",
        }
        resposta = requests.post(url=self.url_base_cursos, headers=self.headers, data=novo)

        assert resposta.status_code == 201
        assert resposta.json()['titulo'] == novo['titulo']

    def test_put_curso(self):
        atualizado = {
            "titulo" : "Novo Curso de Ruby",
            "url" : "http://www.geekuniversity.com/ncr",
        }
        resposta = requests.put(url=f'{self.url_base_cursos}9/', headers=self.headers, data=atualizado)

        assert resposta.status_code == 200
        assert resposta.json()['titulo'] == atualizado['titulo']
        
    def test_put_titulo_curso(self):
        atualizado = {
            "titulo" : "Novo Curso de Ruby 2",
            "url" : "http://www.geekuniversity.com/ncr2",
        }
        resposta = requests.put(url=f'{self.url_base_cursos}9/', headers=self.headers, data=atualizado)

        assert resposta.json()['titulo'] == atualizado['titulo']

    def test_delete_curso(self):
        resposta = requests.delete(url=f'{self.url_base_cursos}9/', headers=self.headers)

        assert resposta.status_code == 204 and len(resposta.text) == 0
