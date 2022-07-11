from django.shortcuts import render
from .models import Noticia
from .models import Periodista
from django.http import HttpResponse


# Create your views here.

def home(request):

    noticias = Noticia.objects.all()
    lista = []
    for noticia in noticias:
        noticia.foto_noticia =  'media/' + str(noticia.foto_noticia)
    


    datos = {
        'noticias' : noticias
    }
    print(datos)

    return render(request, 'core/home.html', datos)




def login(request):
    return render(request, 'core/login.html')


def registro(request):
    return render(request, 'core/registro.html')


def horoscopo(request):
    return render(request, 'core/horoscopo.html')




def periodista(request):
    periodistas = Periodista.objects.all()
    lista = []
    for periodista in periodistas:
        periodista.foto_periodista = 'media/' + str(periodista.foto_periodista)

    datos = {
        'periodistas' : periodistas
    }

    return render(request, 'core/periodista.html', datos)