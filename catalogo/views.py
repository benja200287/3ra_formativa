from django.shortcuts import render
from .models import Juego, Categoria

# Create your views here.
def inicio(request):
    nombre = request.GET.get('nombre', '').strip()
    juegos = Juego.objects.filter(disponible=True)
    categorias = request.GET.get('categoria')
    if categorias:
        juegos = juegos.filter(categoria_id=categorias)

    if nombre:
        juegos = juegos.filter(nombre__icontains=nombre)
    return render(request, 'catalogo/inicio.html', {
        'juegos': juegos,
        'nombre': nombre,
        'categorias': Categoria.objects.all(),
        'categoria_seleccionada': categorias or '',
    })

def detalle(request, juego_id):
    juego = Juego.objects.get(id=juego_id)
    return render(request, 'catalogo/detalle.html', {'juego': juego})
