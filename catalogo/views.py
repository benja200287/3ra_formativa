from django.db import transaction
from django.shortcuts import get_object_or_404, render
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
    juego = get_object_or_404(Juego, id=juego_id)
    return render(request, 'catalogo/detalle.html', {'juego': juego})

def pedido(request, juego_id):
    juego = get_object_or_404(Juego, id=juego_id)
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            cantidad = form.cleaned_data['cantidad']
            with transaction.atomic():
                juego = get_object_or_404(
                    Juego.objects.select_for_update(),
                    id=juego_id,
                )
                if not juego.disponible or cantidad > juego.stock:
                    if not juego.disponible:
                        form.add_error(None, 'Este juego no está disponible para pedidos.')
                    else:
                        form.add_error(
                            'cantidad',
                            f'Solo quedan {juego.stock} unidades disponibles.',
                        )
                else:
                    pedido = Pedido.objects.create(
                        juego=juego,
                        nombre_cliente=form.cleaned_data['nombre_cliente'],
                        email_cliente=form.cleaned_data['email_cliente'],
                        telefono_cliente=form.cleaned_data['telefono_cliente'],
                        cantidad=cantidad,
                    )

                    total_precio = pedido.juego.precio * pedido.cantidad
                    juego.stock -= cantidad
                    if juego.stock == 0:
                        juego.disponible = False
                    juego.save(update_fields=['stock', 'disponible'])
                    return render(request, 'catalogo/pedido_exitoso.html', {'pedido': pedido, 'total_precio': total_precio})
                
                  
    else:
        form = PedidoForm()
    return render(request, 'catalogo/pedido.html', {'form': form, 'juego': juego})
