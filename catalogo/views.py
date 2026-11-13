from django.shortcuts import render
from .models import Juego

# Create your views here.
def inicio(request):
    juegos = Juego.objects.filter(disponible=True)
    return render(request, 'catalogo/inicio.html', {'juegos': juegos})