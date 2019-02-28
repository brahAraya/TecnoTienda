from blog.models import Tienda, Producto, Venta, Vendedor
from rest_framework import serializers

class TiendaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tienda
        fields = ('nombre', 'direccion', 'region', 'ciudad', 'telefono', 'email', 'encargado')

class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = ('nombre_producto', 'foto', 'descripcion', 'precio', 'tipo_producto', 'tienda', 'oferta', 'precio_oferta', 'porcentaje_desc')

class VendedorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vendedor
        fields = ('id', 'sucursal')

class VentaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Venta
        fields = ('producto', 'fecha_venta', 'cantidad', 'sucursal', 'vendedor')
