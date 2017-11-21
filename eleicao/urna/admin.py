from django.contrib import admin
from urna.models import Eleicao,Eleitor,Vaga,Votar,Candidato,Resultado
# Register your models here.
admin.site.register(Eleicao)
admin.site.register(Eleitor)
admin.site.register(Vaga)
admin.site.register(Votar)
admin.site.register(Candidato)
admin.site.register(Resultado)