import requests


class TestEscola:
    payload = {"username": "admin", "password": "admin"}
    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY0MTIzNzQ1LCJpYXQiOjE2NjQxMjM0NDUsImp0aSI6ImU5OWExZmMwYjdmMTRlYmQ4ZmI5OTdkZjc5ZTVjMjIzIiwidXNlcl9pZCI6Mn0.kmOC-DHDx8T635MYlT0D-WCtnvEM4aHJsgpLDwcbL5k"
    }
    url_login = "http://127.0.0.1:8000/escola/token/"
    url_escola = "http://127.0.0.1:8000/escola/"
    url_aluno = "http://127.0.0.1:8000/escola/aluno/"

    def test_post_login(self):
        login = requests.post(url=self.url_login, data=self.payload)
        assert login.status_code == 200

    def test_get_escola(self):
        escola = requests.get(url=self.url_escola)
        assert escola.status_code == 200

    def test_get_aluno(self):
        alunos = requests.get(url=self.url_aluno, headers=self.headers)
        assert alunos.status_code == 200

    def test_cria_aluno(self):
        payload = {
            "nome": "Eduardo",
            "email": "eduardo@eduardo.com",
            "data_nascimento": "1985-01-12"
        }

        cria_aluno  = requests.post(url=self.url_aluno, json=payload, headers=self.headers)
        assert cria_aluno.status_code == 201


    def test_deleta_aluno(self):
        id = 6
        exclui_aluno = requests.delete(url=f'{self.url_aluno}{id}', headers=self.headers)
        assert exclui_aluno.status_code == 204


