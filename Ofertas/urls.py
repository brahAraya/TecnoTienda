from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from rest_framework import routers
from blog.quickstart import views

router = routers.DefaultRouter()
router.register(r'tiendas', views.TiendaViewSet)
router.register(r'productos', views.ProductoViewSet)
router.register(r'vendedores', views.VendedorViewSet)
router.register(r'ventas', views.VentaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    url('accounts/', include('allauth.urls')),  
    url('', include('pwa.urls')),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    # url(r'^registrate/$', SignUpView.as_view(), name='sign_up'),
]
