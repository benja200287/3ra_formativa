from django.contrib import admin
from .models import Categoria, Juego, Pedido

# Register your models here.
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)

@admin.register(Juego)
class JuegoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'cantidad_jugadores', 'edad_minima', 'disponible', 'stock', 'precio')
    list_filter = ('categoria', 'disponible')
    search_fields = ('nombre',)

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'juego', 'nombre_cliente', 'email_cliente', 'telefono_cliente', 'cantidad', 'fecha_pedido')
    search_fields = ('codigo', 'nombre_cliente', 'email_cliente')

