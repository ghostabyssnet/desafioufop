from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpRequest
# static
def index(request):
    return render(request, 'index.html')

def alunos(request):
    return render(request, 'alunos.html')