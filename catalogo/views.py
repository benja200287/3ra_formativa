from django.shortcuts import render
from .models import Juego

# Create your views here.
def inicio(request):
    nombre = request.GET.get('nombre', '').strip()
    juegos = Juego.objects.filter(disponible=True)
    if nombre:
        juegos = juegos.filter(nombre__icontains=nombre)
    return render(request, 'catalogo/inicio.html', {'juegos': juegos, 'nombre': nombre})