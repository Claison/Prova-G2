
from rest_framework import  serializers, viewsets
from django.contrib.auth.models import User
from urna.models import Eleicao,Eleitor,Vaga,Votar,Candidato,Resultado


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=User
        fields=('username','email','is_staff')

class EleicaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Eleicao
        fields=('nome','dataInicio','dataFinal')

class EleitorSerializer(serializers.HyperlinkedModelSerializer):
    #horario=HorarioSerializer(many=False)
    class Meta:
        model=Eleitor
        fields=('nome','cargo','setor','usuario')

class VagaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Vaga
        fields=('cargo',)

class VotarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Votar
        fields=('eleicao','candidato','status',)
    def update(self, instance, validated_data):
        instance.candidato= validated_data.get('quantidade', instance.candidato)
        instance.save()
        return instance

class CandidatoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Candidato
        fields=('candidato','vaga')
        
class ResultadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Resultado
        fields=('candidato','votosBrancos')