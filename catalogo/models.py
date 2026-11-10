from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Juego(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    cantidad_jugadores = models.PositiveIntegerField()
    edad_minima = models.PositiveIntegerField()
    disponible = models.BooleanField(default=True)
    stock = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='juegos/')

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    codigo = models.CharField(max_length=20, unique=True, blank=True)
    juego = models.ForeignKey(Juego, on_delete=models.CASCADE)
    nombre_cliente = models.CharField(max_length=100)
    email_cliente = models.EmailField()
    telefono_cliente = models.CharField(max_length=20)
    cantidad = models.PositiveIntegerField()
    fecha_pedido = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido {self.codigo} - {self.nombre_cliente}"

    def save(self, *args, **kwargs):
        if not self.codigo:
            ultimo = Pedido.objects.count() + 1
            self.codigo = f"PED-{ultimo:04d}"
        super().save(*args, **kwargs)
