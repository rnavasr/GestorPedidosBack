from django.db import models
from Administrador.models import Administrador
from Proveedores.models import Proveedores

# Create your models here.
class Compras(models.Model):
    id_compra = models.AutoField(primary_key=True)
    id_proveedor = models.ForeignKey(Proveedores, models.DO_NOTHING, db_column='id_proveedor')
    id_administrador = models.ForeignKey(Administrador, models.DO_NOTHING, db_column='id_administrador')
    fechaCompra = models.DateTimeField()
    id_procesamiento = models.ForeignKey(Procesamiento, models.DO_NOTHING, db_column='id_procesamiento')

    class Meta:
        managed = False
        db_table = 'compras'

class DetalleCompra(models.Model):
    id_detalleCompra = models.AutoField(primary_key=True)
    id_compra = models.ForeignKey(Compras, models.DO_NOTHING, db_column='id_compra')
    id_producto = models.ForeignKey(Producto, models.DO_NOTHING, db_column='id_producto', blank=True, null=True)
    id_componente = models.ForeignKey(Componente, models.DO_NOTHING, db_column='id_componente', blank=True, null=True)
    cantidad = models.DecimalField(max_digits=9, decimal_places=2)
    precio = models.DecimalField(max_digits=9, decimal_places=2)
    id_um = models.ForeignKey(Unidadmedida, models.DO_NOTHING, db_column='id_um')

    class Meta:
        managed = False
        db_table = 'detallecompra'