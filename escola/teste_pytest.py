import requests


class TestCursos:
    headers = {'Authorization': 'Token 566a1c738ed0c2d2e32fb4866dec5ddd9dd829b6'}
    url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
    
    def test_get_cursos(self): # passou
        resposta = requests.get(url=self.url_base_cursos, headers=self.headers)
        
        assert resposta.status_code == 200
        
    def test_get_curso(self): # corrigido
        resposta = requests.get(url=f'{self.url_base_cursos}10/', headers=self.headers)
        
        assert resposta.status_code == 200

    def test_post_curso(self): # passou
        novo = {
            "titulo": "Curso de testesess",
            "url": "http://testesess.com"
        }
        resposta = requests.post(
            url=self.url_base_cursos,
            headers=self.headers,
            data=novo
            )

        assert resposta.status_code == 201
        assert resposta.json()['titulo'] == novo['titulo']
    
    def test_put_curso(self): # corrigido
        att = {
            "titulo": "Curso de testes atts",
            "url": "http://www.testeatts.com"
        }
        resposta = requests.put(
            url=f'{self.url_base_cursos}10/',
            headers=self.headers,
            data=att
            )
        
        assert resposta.status_code == 200
    
    def test_put_titulo_curso(self): # corrigido
        att = {
            "titulo": "Curso de testes att de novo",
            "url": "http://testeattdenovo.com"
        }
        resposta = requests.put(
            url=f'{self.url_base_cursos}11/',
            headers=self.headers,
            data=att
            )
        
        assert resposta.json()['titulo'] == att['titulo']

    def test_delete_curso(self): # corrigido
        resposta = requests.delete(
            url=f'{self.url_base_cursos}15/',
            headers=self.headers
            )
        assert resposta.status_code == 204 and len(resposta.text) == 0

    