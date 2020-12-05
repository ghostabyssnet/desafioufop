from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('alunos', views.alunos, name='alunos'),
    path('externo', views.externo, name='externo'),
    path('success', views.success, name='success'),
    path('registrar', views.registrar, name='registrar'),
    path('login', views.login, name='login'),
    path('servidores', views.servidores, name='servidores'),
]