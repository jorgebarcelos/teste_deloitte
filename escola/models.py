from django.db import models

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    data_nascimento = models.DateField()

    def __str__(self) -> str:
        return f'<{self.__class__.__name__}: {self.nome}>'


class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    carga_horaria = models.FloatField()

    def __str__(self) -> str:
        return f'<{self.__class__.__name__}: {self.nome}>'


class Boletim(models.Model):
    data_entrega = models.DateField()
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'<{self.__class__.__name__}: {self.aluno.nome}>'


class NotasBoletim(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    boletim = models.ForeignKey(Boletim, on_delete=models.CASCADE)
    nota = models.FloatField(max_length=10)

    def __str__(self) -> str:
        return f'<{self.__class__.__name__}: {self.nota}>'
    