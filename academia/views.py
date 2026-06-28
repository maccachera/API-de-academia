from django.shortcuts import render
from rest_framework import viewsets
from .models import Unidade, Plano, Aluno, FichaTreino, RegistroAcesso
from .serializers import (
    UnidadeSerializer, PlanoSerializer, AlunoSerializer, 
    FichaTreinoSerializer, RegistroAcessoSerializer
)

class UnidadeViewSet(viewsets.ModelViewSet):
    queryset = Unidade.objects.all()
    serializer_class = UnidadeSerializer

class PlanoViewSet(viewsets.ModelViewSet):
    queryset = Plano.objects.all()
    serializer_class = PlanoSerializer

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class FichaTreinoViewSet(viewsets.ModelViewSet):
    queryset = FichaTreino.objects.all()
    serializer_class = FichaTreinoSerializer

class RegistroAcessoViewSet(viewsets.ModelViewSet):
    queryset = RegistroAcesso.objects.all()
    serializer_class = RegistroAcessoSerializer
