from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UnidadeViewSet, PlanoViewSet, AlunoViewSet, 
    FichaTreinoViewSet, RegistroAcessoViewSet
)


router = DefaultRouter()
router.register(r'unidades', UnidadeViewSet)
router.register(r'planos', PlanoViewSet)
router.register(r'alunos', AlunoViewSet)
router.register(r'fichas', FichaTreinoViewSet)
router.register(r'acessos', RegistroAcessoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]