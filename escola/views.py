from rest_framework import viewsets
from .serializers import AlunoSerializer, DisciplinaSerializer, BoletimSerializer, NotasBoletimSerializer
from .models import Aluno, Disciplina, Boletim, NotasBoletim


class AlunoViewsSet(viewsets.ModelViewSet):
    serializer_class = AlunoSerializer
    queryset = Aluno.objects.all()


class DisciplinaViewSet(viewsets.ModelViewSet):
    serializer_class = DisciplinaSerializer
    queryset = Disciplina.objects.all()


class BoletimViewSet(viewsets.ModelViewSet):
    serializer_class = BoletimSerializer
    queryset = Boletim.objects.all()


class NotasViewSet(viewsets.ModelViewSet):
    serializer_class = NotasBoletimSerializer
    queryset = NotasBoletim.objects.all()
