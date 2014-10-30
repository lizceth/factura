from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    ruc=models.CharField(max_length=11)
    razon_social=models.CharField(max_length=100)
    direccion=models.CharField(max_length=200)
    def __unicode__(self):
        return U"%s-%s" %(self.ruc,self.razon_social)

class Producto(models.Model):
    CATEGORIA=(
        ('A','afecto'),
        ('I','inafecto'),
    )

    codigo=models.CharField(max_length=10)
    nombre=models.CharField(max_length=50)
    precio_unit=models.FloatField()
    categoria=models.CharField(max_length=1, choices=CATEGORIA)
    def __unicode__(self):
        return U"%s"%self.nombre

class Factura(models.Model):
    serie=models.CharField(max_length=3)
    numero=models.CharField(max_length=6, unique=True)
    cliente=models.ForeignKey(Cliente)
    fecha=models.DateTimeField(auto_now_add=True)
    igv_total=models.FloatField()
    total=models.FloatField()
    subtotal=models.FloatField()
    usuario=models.ForeignKey(User)
    def __unicode__(self):
        return U"%s" %self.numero

class Detalle(models.Model):
    producto=models.ForeignKey(Producto)
    cantidad=models.IntegerField()
    importe=models.FloatField()
    registro=models.ForeignKey(Factura)
    igv=models.FloatField()
    base_imponible=models.FloatField()

