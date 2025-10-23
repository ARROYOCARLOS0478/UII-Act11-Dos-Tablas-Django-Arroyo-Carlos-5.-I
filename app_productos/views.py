from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Producto, Proveedor
from .forms import ProductoForm, ProveedorForm # Importa ambos formularios

# --- Vistas para Productos ---

def listar_productos(request):
    productos = Producto.objects.all().order_by('nombre')
    # CORRECCIÓN 1: Ruta de plantilla corregida
    return render(request, 'listar_productos.html', {'productos': productos})

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    # CORRECCIÓN 1: Ruta de plantilla corregida
    return render(request, 'detalle_producto.html', {'producto': producto})

def crear_producto(request):
    if request.method == 'POST':
        # CORRECCIÓN 2: Pasa request.FILES para manejar la subida de la imagen
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('app_productos:listar_productos'))
    else:
        form = ProductoForm()
    # CORRECCIÓN 1: Ruta de plantilla corregida
    return render(request, 'formulario_producto.html', {'form': form, 'titulo': 'Crear Producto'})

def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        # CORRECCIÓN 2: Pasa request.FILES para manejar la subida de la imagen
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect(reverse('app_productos:detalle_producto', args=[producto.id]))
    else:
        form = ProductoForm(instance=producto)
    # CORRECCIÓN 1: Ruta de plantilla corregida
    return render(request, 'formulario_producto.html', {'form': form, 'titulo': 'Editar Producto'})

def borrar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect(reverse('app_productos:listar_productos'))
    # CORRECCIÓN 1: Ruta de plantilla corregida
    return render(request, 'confirmar_borrar_producto.html', {'producto': producto})


# --- Vistas para Proveedores ---

def listar_proveedores(request):
    proveedores = Proveedor.objects.all().order_by('nombre')
    # CORRECCIÓN 1: Ruta de plantilla corregida
    return render(request, 'listar_proveedores.html', {'proveedores': proveedores})

def detalle_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    # CORRECCIÓN 1: Ruta de plantilla corregida
    return render(request, 'detalle_proveedor.html', {'proveedor': proveedor})

def crear_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST) # No hay ImageField en Proveedor, así que no se necesita request.FILES aquí
        if form.is_valid():
            form.save()
            return redirect(reverse('app_productos:listar_proveedores'))
    else:
        form = ProveedorForm()
    # CORRECCIÓN 1: Ruta de plantilla corregida
    return render(request, 'formulario_proveedor.html', {'form': form, 'titulo': 'Crear Proveedor'})

def editar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor) # No hay ImageField en Proveedor, así que no se necesita request.FILES aquí
        if form.is_valid():
            form.save()
            return redirect(reverse('app_productos:detalle_proveedor', args=[proveedor.id]))
    else:
        form = ProveedorForm(instance=proveedor)
    # CORRECCIÓN 1: Ruta de plantilla corregida
    return render(request, 'formulario_proveedor.html', {'form': form, 'titulo': 'Editar Proveedor'})

def borrar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    if request.method == 'POST':
        proveedor.delete()
        return redirect(reverse('app_productos:listar_proveedores'))
    # CORRECCIÓN 1: Ruta de plantilla corregida
    return render(request, 'confirmar_borrar_proveedor.html', {'proveedor': proveedor})