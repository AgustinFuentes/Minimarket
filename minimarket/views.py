from django.shortcuts import render, redirect
from .models import *
from .forms import ProductoForm
from django.http import JsonResponse

def index(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'minimarket/index.html', context)

def ver_carrito(request):
    carrito = request.session.get('carrito', {})
    productos = []

    total = 0

    for producto_id, cantidad in carrito.items():
        producto = Producto.objects.get(id=producto_id)
        subtotal = producto.precio * cantidad
        total += subtotal

        productos.append({
            'producto': producto,
            'cantidad': cantidad,
            'subtotal': subtotal
        })

    context = {
        'productos': productos,
        'total': total
    }

    return render(request, 'minimarket/ver_carrito.html', context)

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductoForm()
    return render(request, 'minimarket/agregar_producto.html', {'form': form})

def agregar_al_carrito(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    carrito = request.session.get('carrito', {})
    cantidad = carrito.get(str(producto_id), 0)
    if cantidad < producto.cantidad:
        carrito[str(producto_id)] = cantidad + 1
        producto.disminuir_cantidad()
        request.session['carrito'] = carrito
        request.session.modified = True

        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'message': 'No hay suficiente cantidad disponible.'})
    
def eliminar_producto(request, producto_id):
    if request.method == 'POST':
        carrito = request.session.get('carrito', {})
        if str(producto_id) in carrito:
            del carrito[str(producto_id)]
            request.session['carrito'] = carrito
    return redirect('ver_carrito')