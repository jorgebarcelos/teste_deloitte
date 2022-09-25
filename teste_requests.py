import requests

headers = {
    'username': 'admin',
    'password':'admin',
    'Authorization': 'Token eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY0MDYzMDQwLCJpYXQiOjE2NjQwNjI3NDAsImp0aSI6ImU0MzliOGNjY2IyMTQ3ZTdhNjYzNjEwZjdkYzE3YTE1IiwidXNlcl9pZCI6Mn0.VRRCXH3VWrT746eKMDtJlXIixjO_kD-23iPmshdvuN4'
}
alunos = requests.get(url='http://127.0.0.1:8000/escola/aluno/', headers=headers)

print(alunos.json())