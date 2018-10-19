from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.


# CATALOGOS
@python_2_unicode_compatible
class Cargo(models.Model):
	cargo=models.CharField(max_length=25)

	def __str__(self):
		return self.cargo

@python_2_unicode_compatible
class Sexo(models.Model):
	sexo=models.CharField(max_length=25)

	def __str__(self):
		return self.sexo		

@python_2_unicode_compatible
class EstadoCivil(models.Model):
	estadocivil=models.CharField(max_length=25)

	def __str__(self):
		return self.estadocivil

@python_2_unicode_compatible
class Profesion(models.Model):
	profesion=models.CharField(max_length=25)

	def __str__(self):
		return self.profesion
# Transaccionales

@python_2_unicode_compatible
class Local(models.Model):
	nombre=models.CharField(max_length=5)
	ancho=models.FloatField()
	largo=models.FloatField()
	precio=models.DecimalField(max_digits=7, decimal_places=2)
	estado=models.BooleanField(default=True)
	
	def __str__(self):
		return self.nombre

@python_2_unicode_compatible
class Empleado(models.Model):
	nombre=models.CharField(max_length=50)
	apellido=models.CharField(max_length=50)
	direccion=models.TextField()
	celular=models.CharField(max_length=9)
	telcasa=models.CharField(max_length=9)
	correo=models.EmailField()
	fechanacimiento=models.DateField()
	fechacontratacion=models.DateTimeField()
	titulo=models.CharField(max_length=75)
	sexo=models.ForeignKey(Sexo)
	estadocivil=models.ForeignKey(EstadoCivil)
	cargo=models.ForeignKey(Cargo)
	local=models.ForeignKey(Local)
	user= models.OneToOneField(User, null=True)
	estado=models.BooleanField()

	def __str__(self):
		return self.nombre +' '+ self.apellido

@python_2_unicode_compatible
class Paciente(models.Model):
	identidad= models.CharField(max_length=15)
	nombre=models.CharField(max_length=50)
	apellido=models.CharField(max_length=50)
	direccion=models.TextField()
	celular=models.CharField(max_length=9, null=True)
	telcasa=models.CharField(max_length=9, null=True)
	correo=models.EmailField(null=True)
	fechanacimiento=models.DateTimeField()
	sexo=models.ForeignKey(Sexo)
	profesion=models.ForeignKey(Profesion)
	estadocivil=models.ForeignKey(EstadoCivil)


	def __str__(self):
		return self.nombre +' '+ self.apellido

@python_2_unicode_compatible
class Proveedor(models.Model):
	nombre=models.CharField(max_length=50)
	apellido=models.CharField(max_length=50)
	direccion=models.TextField()
	celular=models.CharField(max_length=9, null=True)
	correo=models.EmailField(null=True)
	sexo=models.ForeignKey(Sexo)
	empresa=models.CharField(max_length=50)
	

	def __str__(self):
		return self.nombre +' '+ self.apellido+': '+self.empresa

@python_2_unicode_compatible
class Medicamento(models.Model):
	nombre=models.CharField(max_length=50)
	descripcion=models.CharField(max_length=100)
	existencia=models.IntegerField()
	precio=models.DecimalField(max_digits=5, decimal_places=2)
	fechaelaboracion=models.DateField()
	fechaVencimiento=models.DateField()
	proveedor=models.ForeignKey(Proveedor)
	
	def __str__(self):
		return self.nombre

@python_2_unicode_compatible
class Configuracion(models.Model):
	nombre_empresa=models.CharField(max_length=70)
	logo=models.ImageField(upload_to='Logo')
	ubicacion=models.TextField()
	RTN=models.CharField(max_length=20)
	correo=models.EmailField()
	celular=models.CharField(max_length=9)

	def __str__(self):
		return self.nombre_empresa

@python_2_unicode_compatible
class Diagnostico(models.Model):
	paciente=models.ForeignKey(Paciente)
	empleado=models.ForeignKey(Empleado)
	fecha=models.DateField(auto_now_add=True)
	descripcion=models.TextField()

	def __str__(self):
		return self.descripcion		

@python_2_unicode_compatible
class Prescripcion(models.Model):
	diagnostico=models.ForeignKey(Diagnostico)
	medicamento=models.ForeignKey(Medicamento)
	dosis=models.CharField(max_length=50)
	tiempo=models.CharField(max_length=50)

	def __str__(self):
		return '{}: {}'.format(self.diagnostico, self.medicamento)

@python_2_unicode_compatible
class PagoConsulta(models.Model):
	fecha=models.DateField(auto_now_add=True)
	paciente=models.ForeignKey(Paciente)
	empleado=models.ForeignKey(Empleado)
	precio=models.DecimalField(max_digits=5, decimal_places=2)
	estado=models.BooleanField(default=False)

	def __str__(self):
		return'{}:{}'.format( str(self.fecha.strftime("%d/%m/%y")),self.paciente)

@python_2_unicode_compatible
class VentaMedicamento(models.Model):
	fecha=models.DateField(auto_now_add=True)
	empleado=models.ForeignKey(Empleado)
	paciente=models.ForeignKey(Paciente)
	
	def __str__(self):
		return '{}:{}'.format(str(self.fecha.strftime("%d/%m/%y")),self.paciente)

@python_2_unicode_compatible
class DetalleVenta(models.Model):
	ventamedicamento=models.ForeignKey(VentaMedicamento)
	medicamento=models.ForeignKey(Medicamento)
	cantidad=models.IntegerField()
	subtotal=models.FloatField(default=0,editable=False)
	
	def __str__(self):
		return '{}:{}'.format(self.ventamedicamento.paciente,self.medicamento)

	def save(self,*args,**kwargs):
		self.subtotal=(float(self.medicamento.precio)*float(self.cantidad))
		super(DetalleVenta,self).save(*args,**kwargs)

@python_2_unicode_compatible
class Especialidad(models.Model):
	empleado=models.ForeignKey(Empleado)
	especialidad=models.CharField(max_length=50)

	def __str__(self):
		return '{}: {}'.format(self.empleado,self.especialidad)




