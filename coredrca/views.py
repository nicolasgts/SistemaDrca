from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import RequestContext , loader

# Create your views here.
from coredrca.models import Aluno

def home(request):
    template = loader.get_template('index.html')
    context = RequestContext(request)
    return  HttpResponse(template.render(context))

def alunos(request):
    alunos = Aluno.objects.all()
    template = loader.get_template('alunos.html')
    context = RequestContext(request,{'alunos': alunos})
    return  HttpResponse(template.render(context))

