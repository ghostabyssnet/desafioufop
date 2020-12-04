from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpRequest
from Virtual.system.formhandler import HandleStudentForm
from .apiconnector import CreatePerson
# static

# I know it could be 

def index(request):
    return render(request, 'index.html')

def alunos(request):
    return render(request, 'alunos.html')

def externo(request):
    _nome= request.POST.get('nome')
    _sobrenome= request.POST.get('sobrenome')
    _data_nascimento= request.POST.get('data_nascimento')
    _telefone= request.POST.get('telefone')
    _email= request.POST.get('email')
    _payload= (_nome + _sobrenome + _data_nascimento + _telefone + _email)
    if HandleStudentForm(_payload): # We could use try-catch (except) or any other error handling here.
        CreatePerson(_payload)
    else:
        print('As I\'ve commented, we\'d use error handling in this block.')
    return render(request, 'externo.html')