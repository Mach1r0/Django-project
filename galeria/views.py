from django.shortcuts import render
from django.http import HttpResponse 

dados = {
    1: {"nome": "Nebulosa de carina",
        "legenda": "webbtelecope.org / NASA / James webb"},
    2: {"nome": "Galaxia NGC 1079",
        "legenda": "nasa.org  / ORG",}
}

def index(request): 
    return render(request, 'galeria/index.html', {"cards": dados})

def imagem(request):
    return render(request, 'galeria/imagem.html')