from django import forms
from .models import Producto, Proveedor

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'stock', 'modelo', 'imagen_producto', 'proveedor'] # ¡Añadir imagen_producto!
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4}),
            'precio': forms.NumberInput(attrs={'step': '0.01'}),
        }
class ProveedorForm(forms.ModelForm): # ¡NUEVA CLASE!
    class Meta:
        model = Proveedor
        fields = ['nombre', 'contacto', 'telefono', 'direccion']
        widgets = {
            'direccion': forms.Textarea(attrs={'rows': 3}), # Por ejemplo, un textarea para la dirección
        }