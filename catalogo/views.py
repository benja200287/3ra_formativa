from django.shortcuts import render
from .forms import PedidoForm
from .models import Juego, Categoria, Pedido

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

def pedido(request, juego_id):
    juego = Juego.objects.get(id=juego_id)
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = Pedido(
                juego=juego,
                nombre_cliente=form.cleaned_data['nombre_cliente'],
                email_cliente=form.cleaned_data['email_cliente'],
                telefono_cliente=form.cleaned_data['telefono_cliente'],
                cantidad=form.cleaned_data['cantidad']
            )
            pedido.save()
            return render(request, 'catalogo/pedido_exitoso.html', {'pedido': pedido})
    else:
        form = PedidoForm()
    return render(request, 'catalogo/pedido.html', {'form': form, 'juego': juego})
