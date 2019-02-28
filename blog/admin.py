from django.contrib import admin
from .models import Tienda, Producto, Venta, Vendedor

# Register your models here.
admin.site.register(Tienda)
admin.site.register(Producto)
admin.site.register(Venta)
admin.site.register(Vendedor)
