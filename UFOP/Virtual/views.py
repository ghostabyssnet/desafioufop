from django.shortcuts import render, redirect
from django.http import HttpResponse,Http404,HttpRequest
from Virtual.system.formhandler import HandleForm
from .apiconnector import CreatePerson, CreateAccount, Login


# If this project was bigger, I'd split this in multiple files.
# Organization isn't too relevant right now as I'm running out of time.

def index(request):
    return render(request, 'index.html')

def alunos(request):
    return render(request, 'alunos.html')

def success(request):
    return render(request, 'success.html')

def registrar(request):
    _username= ''
    _password= ''
    _email= ''
    if request.method == 'POST':
        _username= request.POST.get('login')
        _password= request.POST.get('password')
        _email= request.POST.get('email')
        if CreateAccount(_username, _password, _email):
            return redirect('/virtual/success')
    return render(request, 'registrar.html')

def login(request):
    _username= ''
    _password= ''
    if request.method == 'POST':
        _username= request.POST.get('login')
        _password= request.POST.get('password')
        if Login(request, _username, _password):
            return redirect('virtual/success')
        else:
            return redirect('virtual/')
    return render(request, 'login.html')

def externo(request):
    _nome = ''
    _sobrenome = ''
    _data_nascimento = ''
    _telefone = ''
    _email = ''
    _payload = ()
    if request.method == 'POST':
        _nome= request.POST.get('nome')
        _sobrenome= request.POST.get('sobrenome')
        _data_nascimento= request.POST.get('data_nascimento')
        _telefone= request.POST.get('telefone')
        _email= request.POST.get('email')
        _payload= (_nome, _sobrenome, _data_nascimento, _telefone, _email)
        if HandleForm(_payload): # We could use try-catch (except) or any other error handling here.
            if CreatePerson(_payload):
                return redirect('virtual/success')
        else:
            print('As I\'ve commented, we\'d use error handling in this block.')
        return render(request, 'externo.html')