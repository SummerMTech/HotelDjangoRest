from django.db import models

# Create your models here.
class Habitacion (models.Model):
	codigo = models.IntegerField(primary_key = True)
	tipo = models.CharField(max_length = 200, default ='doble')
	costo = models.FloatField()
	banioPrivado = models.BooleanField(default = True)
	def __str__(self):
		return "{}, {}, {}, {} ".format(self.codigo, self.tipo, self.costo, self.banioPrivado)
	

class Cliente(models.Model):
	nombre  = models.CharField(primary_key = True, max_length = 200)
	ci = models.IntegerField(default = 0)
	celular = models.IntegerField(default = 0)
	correo = models.CharField(max_length = 200)