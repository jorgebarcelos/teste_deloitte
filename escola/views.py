from rest_framework import viewsets
from .serializers import AlunoSerializer, DisciplinaSerializer, BoletimSerializer, NotasBoletimSerializer
from .models import Aluno, Disciplina, Boletim, NotasBoletim
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class AlunoViewsSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = [JWTAuthentication]
    serializer_class = AlunoSerializer
    queryset = Aluno.objects.all()


class DisciplinaViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = [JWTAuthentication]
    serializer_class = DisciplinaSerializer
    queryset = Disciplina.objects.all()


class BoletimViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = [JWTAuthentication]
    serializer_class = BoletimSerializer
    queryset = Boletim.objects.all()


class NotasViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = [JWTAuthentication]
    serializer_class = NotasBoletimSerializer
    queryset = NotasBoletim.objects.all()
