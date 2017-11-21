from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Eleicao(models.Model):
    nome=models.CharField(max_length=100)
    dataInicio=models.DateTimeField(blank=True,null=True)
    dataFinal=models.DateTimeField(blank=True,null=True)
    def __str__(self):
        return self.nome


class Eleitor(models.Model):
    nome=models.CharField(max_length=100)
    cargo=models.CharField(max_length=100)
    setor=models.CharField(max_length=100)
    usuario=models.ForeignKey(User,null=True, blank=False )
    def __str__(self):
        return self.nome

class Vaga(models.Model):
    cargo=models.CharField(max_length=100)
    def __str__(self):
        return self.cargo

class Candidato(models.Model):
    candidato=models.ForeignKey(Eleitor,null=True, blank=False )
    vaga=models.ForeignKey(Vaga,null=True, blank=False )
    quantidade=models.IntegerField(null=True, blank=False)
    def __str__(self):
        return self.nome

class Resultado(models.Model):
    candidato=models.ForeignKey(Candidato,null=True, blank=False )
    votosBrancos=models.IntegerField(null=True, blank=False)
    def __str__(self):
        return self.candidato.nome

class Votar(models.Model):
    eleicao=models.ForeignKey(Eleicao,null=True, blank=True )
    candidato=models.ForeignKey(Eleitor,null=True, blank=True )
    status=models.CharField(max_length=20,choices=(('Valido','Votou'),('branco','Voto em Branco')),default='votou')
    def __str__(self):
        return self.status

