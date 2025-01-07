from django.shortcuts import render

# Create your views here.

def index(request):
    return render (request, 'index.html')

def contato(request):
    context = {
        'curso': 'Geek University'
    }
    return render (request, 'contato.html', context)