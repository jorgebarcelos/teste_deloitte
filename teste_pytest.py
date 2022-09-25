import requests

class TestEscola:
    headers = {
        'Authorization': 'Token eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY0MDc2NTEwLCJpYXQiOjE2NjQwNzYyMTAsImp0aSI6IjkwZjA5ZjE0NmRhZjQ2NTI4YjFmY2ZjOWMzNTJmNWM4IiwidXNlcl9pZCI6Mn0.hN4GXm-M7x_ZZuZKQR1Io2rhBNcUJkOByn6HZwWPDI4'
        }
    url_escola = 'http://127.0.0.1:8000/escola/'

    def test_get_escola(self):
        escola = requests.get(url=self.url_escola, headers=self.headers)
        assert escola.status_code == 200

    def test_get_aluno(self):
        aluno = requests.get(url=f'{self.url_escola}/aluno/', headers=self.headers)
        assert aluno.status_code == 200


    def test_post_aluno(self):
        novo_aluno = {
            "nome": "Eduardo",
            "email": "eduardo@eduardo.com",
            "data_nascimento": "1985-01-12"
        }

        resultado = requests.post(url=f'{self.url_escola}/aluno/', headers=self.headers, data=novo_aluno)
        assert resultado.status_code == 201