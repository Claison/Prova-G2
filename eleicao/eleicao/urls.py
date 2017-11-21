"""eleicao URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from urna.views import UserViewSet,EleicaoViewSet,EleitorViewSet,VagaViewSet,VotarViewSet,CandidatoViewSet,ResultadoViewSet
from rest_framework import routers, viewsets

router=routers.DefaultRouter()
router.register(r'User',UserViewSet)
router.register(r'Eleicao',EleicaoViewSet)
router.register(r'Eleitor',EleitorViewSet)
router.register(r'Vaga',VagaViewSet)
router.register(r'Votar',VotarViewSet)
router.register(r'Candidato',CandidatoViewSet)
router.register(r'Resultado',ResultadoViewSet)
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework'))
]