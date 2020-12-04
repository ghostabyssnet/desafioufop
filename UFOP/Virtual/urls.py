from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('alunos', views.alunos, name='alunos'),
    path('externo', views.externo, name='externo'),
]