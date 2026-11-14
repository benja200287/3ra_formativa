from django import forms

class PedidoForm(forms.Form):
    nombre_cliente = forms.CharField(label='Nombre', max_length=100)
    email_cliente = forms.EmailField(label='Email')
    telefono_cliente = forms.CharField(label='Teléfono', max_length=20)
    cantidad = forms.IntegerField(label='Cantidad', min_value=1, max_value=5)
