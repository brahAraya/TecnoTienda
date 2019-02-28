from blog.models import Tienda, Producto, Venta, Vendedor
from rest_framework import viewsets
from blog.quickstart.serializers import TiendaSerializer, ProductoSerializer, VendedorSerializer, VentaSerializer

class TiendaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Tienda.objects.all()
    serializer_class = TiendaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class VendedorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Vendedor.objects.all()
    serializer_class = VendedorSerializer

class VentaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer