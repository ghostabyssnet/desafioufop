from django.shortcuts import redirect
from django.urls import path
# This file handles all sorts of datababase management.
# I know it isn't as organized as it could be, more so if we consider bigger projects.
# However, this isn't one of those, so it should do the trick.
# Also, let's be honest: Python is terrible at handling files.

from .models import Pessoa, Aluno
from .tests import debug
from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

# creates a new Pessoa in the database
def CreatePerson(payload):
    person= Pessoa(
        nome= payload[0],
        sobrenome= payload[1],
        telefone= payload[2],
        data_nascimento= payload[3],
        email= payload[4]
    )
    person.save()
    debug('Adding a Pessoa named [' + str(payload[0]) + '] to our database.')
    return True

# same for student (Aluno)
def CreateStudent(_pessoa, _matricula):
    aluno= Aluno(
        pessoa = _pessoa,
        matricula = _matricula,
        mobilidade = None
    )
    aluno.save()
    debug('Adding an Aluno named [' + pessoa.nome + '] to our database.')
    return True

# creates a new user in the database
def CreateAccount(login, password, email):
    if login is not None and password is not None and email is not None:
        user = User.objects.create_user(login, email, password)
        user.save()
        debug('Creating a new user named ' + str(login) + '.')
        return True
    else:
        return False

# handles user login
def Login(request, _login, _password):
    user = authenticate(username=_login, password=_password)
    if user is not None:
        request.session['username'] = _login
        return True
    else:
        return False

# shows all Alunos (alumni) stored in our database.
# if I had more time, this would be repeated for every query type
# OR (quite probably):
# we'd throw which type we wish to return as a parameter
def ShowStudents():
    result = []
    result = Aluno.objects.all()
    return result
