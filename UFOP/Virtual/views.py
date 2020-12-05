from django.shortcuts import render, redirect
from django.http import HttpResponse,Http404,HttpRequest
from Virtual.system.formhandler import HandleForm
from .apiconnector import CreatePerson, CreateAccount, CreateStudent, Login, ShowStudents


# If this project was bigger, I'd split this in multiple files.
# Organization isn't too relevant right now as I'm running out of time.

def index(request):
    return render(request, 'index.html')

# this is wildly incomplete ('externo' is as well), look into the models to check out what I was planning to add
def alunos(request):
    _nome = ''
    _sobrenome = ''
    _data_nascimento = ''
    _telefone = ''
    _email = ''
    _payload = ()
    if request.method == 'POST':
        _nome= request.POST.get('nome')
        _sobrenome= request.POST.get('sobrenome')
        _telefone= request.POST.get('telefone')
        _data_nascimento= request.POST.get('data_nascimento')
        _email= request.POST.get('email')
        _payload= (_nome, _sobrenome, _telefone, _data_nascimento, _email)
        if HandleForm(_payload): # We could use try-catch (except) or any other error handling here.
            if CreatePerson(_payload):
                return redirect('./success')
        else:
            print('As I\'ve commented, we\'d use error handling in this block.')
    return render(request, 'alunos.html')

def success(request):
    return render(request, 'success.html')

# This is where it gets kinda bad. For some reason, you can't redirect outside of the views.py file
# unless you use some hacky (and possibly buggy) methods. Took me a few hours, and it ruins the program flow.
# There doesn't seem to be any alternative whatsoever.

def registrar(request):
    _username= ''
    _password= ''
    _email= ''
    if request.method == 'POST':
        _username= request.POST.get('login')
        _password= request.POST.get('password')
        _email= request.POST.get('email')
        if CreateAccount(_username, _password, _email):
            return redirect('./success')
    return render(request, 'registrar.html')

def login(request):
    _username= ''
    _password= ''
    if request.method == 'POST':
        _username= request.POST.get('login')
        _password= request.POST.get('password')
        if Login(request, _username, _password):
            request.session['username'] = _username
            return redirect('./servidores')
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
        _telefone= request.POST.get('telefone')
        _data_nascimento= request.POST.get('data_nascimento')
        _email= request.POST.get('email')
        _payload= (_nome, _sobrenome, _data_nascimento, _telefone, _email)
        if HandleForm(_payload): # We could use try-catch (except) or any other error handling here.
            if CreatePerson(_payload):
                return redirect('./success')
        else:
            print('As I\'ve commented, we\'d use error handling in this block.')
        return render(request, 'externo.html')

# staff page
# It's 21:45 -- last day -- right now. I'd put pagination and stuff in here but it's too late
# ...you get the idea. X results per page, Y pages: based on the amount of entries. There's a ton of
# implementations around the web.
def servidores(request):
    alunos = []
    alunos = ShowStudents()
    username='test'
    username = request.session['username']
    context={'alunos': alunos, 'username': username}
    if alunos is None:
        # generate some entries
        _nome="aaa"
        _sobrenome="bbb"
        _data_nascimento=''
        _telefone='31993651646'
        _email='aaa@aaa.com'
        _payload= (_nome, _sobrenome, telefone, _data_nascimento, _email)
        pessoa = CreatePerson(_payload)
        CreateStudent(pessoa, 1924073)
    return render(request, 'servidores.html')