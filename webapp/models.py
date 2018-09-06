from datetime import datetime

from django.db import models



Estado_Choices = (
    ('I','Iniciada'),
    ('C','Cancelada'),
    ('T','Terminada')
)
Estado_Puertos = (
    ('A','Abierto'),
    ('C','Cerrado')
)


class Consulta(models.Model):
    fecha = models.DateField(default=datetime.now , editable=False)
    hora = models.TimeField(default=datetime.now().strftime('%H:%M:%S'), blank=True)
    objetivo = models.GenericIPAddressField(max_length=40)
    iphost = models.GenericIPAddressField(null=True , blank=True)
    mascara = models.CharField(max_length=40,default='32')
    estado = models.CharField(max_length=40, choices=Estado_Choices, default='Iniciada')

    def __str__(self):
        return '{}'.format(self.id)

class DetalleConsulta(models.Model):
    consulta = models.ForeignKey(Consulta)
    fecha = models.DateField(default=datetime.now)
    hora = models.TimeField(default=datetime.now().strftime('%H:%M:%S'))
    mac = models.CharField(max_length=40)


class Puerto(models.Model):
    puerto = models.DecimalField(max_digits=14, decimal_places=12)
    estado = models.CharField(max_length=40, choices=Estado_Puertos, default='Cerrado')
    detalle_consulta = models.ForeignKey(DetalleConsulta)

    def __str__(self):
        return '{}'.format(self.puerto)


