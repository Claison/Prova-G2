from django.shortcuts import render
from urna.models import Eleicao,Eleitor,Vaga,Votar,Candidato,Resultado
from rest_framework import viewsets
from django.contrib.auth.models import User
from urna.serializers import UserSerializer,EleicaoSerializer,EleitorSerializer,VagaSerializer,VotarSerializer,CandidatoSerializer,ResultadoSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class EleicaoViewSet(viewsets.ModelViewSet):
    queryset=Eleicao.objects.all()
    serializer_class=EleicaoSerializer

class EleitorViewSet(viewsets.ModelViewSet):
    queryset=Eleitor.objects.all()
    serializer_class=EleitorSerializer

class VagaViewSet(viewsets.ModelViewSet):
    queryset=Vaga.objects.all()
    serializer_class=VagaSerializer

class VotarViewSet(viewsets.ModelViewSet):
    queryset=Votar.objects.all()
    serializer_class=VotarSerializer

class CandidatoViewSet(viewsets.ModelViewSet):
    queryset=Candidato.objects.all()
    serializer_class=CandidatoSerializer

class ResultadoViewSet(viewsets.ModelViewSet):
    queryset=Resultado.objects.all()
    serializer_class=ResultadoSerializer