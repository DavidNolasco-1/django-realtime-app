from django.shortcuts import render

# mi_app/views.py
from .models import Producto # Importamos el modelo Producto

def items_page(request):
    # Recupera todos los productos de la base de datos
    items = Producto.objects.all().order_by('-id')
    
    # Renderiza la plantilla HTML y pasa los datos
    return render(request, 'mi_app/items.html', {'items': items, 'mensaje': 'Datos listados correctamente'})
