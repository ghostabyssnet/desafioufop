from django.shortcuts import redirect
from django.urls import path
# This file handles all sorts of datababase management.
# I know it isn't as organized as it could be, more so if we consider bigger projects.
# However, this isn't one of those, so it should do the trick.
# Also, let's be honest: Python is terrible at handling files.

from .models import Pessoa
from .tests import debug
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

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

# creates a new user in the database
def CreateAccount(login, password, email):
    if login is not None and password is not None and email is not None:
        user = User.objects.create_user(login, email, password)
        user.save()
        debug('Creating a new user named ' + str(login) + '.')
        return True
    else:
        return False

# logs in to our system
def Login(request, _login, _password):
    user = authenticate(username=_login, password=_password)
    if user is not None:
        request.session['username'] = _login
        return True
    else:
        return False
