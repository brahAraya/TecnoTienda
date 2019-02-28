from django.db import models
from django.utils import timezone
from PIL import Image, ImageOps
from django.utils.translation import ugettext as _
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.db.models.signals import post_delete
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.urls import reverse

class Tienda(models.Model):
    nombre = models.CharField(max_length = 100)
    direccion = models.TextField()

    # Esta parte es temporal, hasta que consigamos hacer los cbo dinámicos
    REGION = (
        ('estado_1', 'I Tarapaca'),
        ('estado_2', 'II Antofagasta'),
        ('estado_3', 'III Atacama'),
        ('estado_4', 'IV Coquimbo'),
        ('estado_5', 'V Valparaiso'),
        ('estado_6', 'VI Ohiggins'),
        ('estado_7', 'VII Maule'),
        ('estado_8', 'VIII Bio Bio'),
        ('estado_9', 'IX Araucania'),
        ('estado_10', 'X Los Lagos'),
        ('estado_11', 'XI Aisen'),
        ('estado_12', 'XII Magallanes y Antartica'),
        ('estado_13', 'XII Metropolitana'),
        ('estado_14', 'IVX Los Rios'),
        ('estado_15', 'XV Arica y Parinacota'),
    )
    region = models.CharField(max_length = 25, choices = REGION, default = 'region')

    CIUDAD = (
        ('1', 'Arica'),
        ('2', 'Alto Hospicio'),
        ('3', 'Iquique'),
        ('4', 'Pozo Almonte'),
        ('5', 'Caldera'),
        ('6', 'Chanaral'),
        ('7', 'Copiapo'),
        ('8', 'Diego de Almagro'),
        ('9', 'El Salvador    Huasco'),
        ('10', 'Tierra Amarilla'),
        ('11', 'Vallenar'),
        ('12', 'Andacollo'),
        ('13', 'Combarbala'),
        ('14', 'Coquimbo'),
        ('15', 'El Palqui'),
        ('16', 'Illapel'),
        ('17', 'La Serena'),
        ('18', 'Los Vilos'),
        ('19', 'Montepatria'),
        ('20', 'Ovalle'),
        ('21', 'Salamanca'),
        ('22', 'Vicuna'),
        ('23', 'Algarrobo'),
        ('24', 'Cabildo'),
        ('25', 'Calle Larga'),
        ('26', 'Cartagena'),
        ('27', 'Quilpue'),
        ('28', 'Valparaiso'),
        ('29', 'Villa Alemana'),
    )
    ciudad = models.CharField(max_length = 25, choices = CIUDAD, default = 'ciudad')
    # Aquí termina la parte temporal

    telefono = models.IntegerField()
    email = models.EmailField()
    encargado = models.TextField()

    def __str__(self):
        return '{}'.format(self.nombre)

class Producto(models.Model):
    nombre_producto = models.CharField(max_length = 100)
    foto = models.ImageField(blank = False)
    descripcion = models.TextField()
    precio = models.IntegerField()

    TIPO = (
        ('', 'Seleccione un tipo...'),
        ('1', 'Televisor'),
        ('2', 'Smartphone'),
        ('3', 'Notebook'),
        ('4', 'Audio'),
        ('5', 'Audífonos'),
        ('6', 'Reproductor DVD/Blu-Ray'),
        ('7', 'Consola de videojuegos'),
        ('8', 'Monitor'),
        ('9', 'Accesorios de computador'),
        ('10', 'Cámara'),
    )
    tipo_producto = models.CharField(max_length = 25, choices = TIPO, default = '0')
    tienda = models.ForeignKey(Tienda, null = True, blank = False, on_delete = models.CASCADE)
    oferta = models.BooleanField(default = False)
    precio_oferta = models.IntegerField(null = True, blank = True)
    porcentaje_desc = models.IntegerField(blank = True)

    def __str__(self):
        return '{}'.format(self.nombre_producto)


class Vendedor(models.Model):
    sucursal = models.OneToOneField(Tienda, null = True, blank = False, on_delete = models.CASCADE)

class Venta(models.Model):
    producto = models.OneToOneField(Producto, null = True, blank = False, on_delete = models.CASCADE)
    fecha_venta = models.DateTimeField(default = timezone.now)
    cantidad = models.IntegerField()
    sucursal = models.OneToOneField(Tienda, null = True, blank = False, on_delete = models.CASCADE)
    vendedor = models.OneToOneField(Vendedor, null = True, blank = False, on_delete = models.CASCADE)

class Perfil(models.Model):
        usuario = models.OneToOneField(User, on_delete=models.CASCADE)
        bio = models.CharField(max_length=255, blank=True)
        web = models.URLField(blank=True)

        def __str__(self):
            return self.usuario.username
    