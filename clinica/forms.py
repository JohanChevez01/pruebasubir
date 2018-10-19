from django.forms import ModelForm 
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm

class PacienteForm(ModelForm):
	class Meta:
		model = Paciente
		fields= '__all__'
		widgets={
				'direccion': forms.Textarea(attrs={
					'class': 'form-control',
					'autofocus':'autofocus'
					}),
				'correo': forms.EmailInput(attrs={
					'class': 'form-control',
					'autofocus':'autofocus'
					}),
				'fechanacimiento': forms.DateInput(format=('%d-%m-%Y'),attrs={
					'class': 'form-control',
					'autofocus':'autofocus',
					'type':'date'
					}),

		}

class EmpleadoForm(ModelForm):
	class Meta:
		model = Empleado
		fields= '__all__'
		widgets={
				'direccion': forms.Textarea(attrs={
					'class': 'form-control',
					'autofocus':'autofocus'
					}),
				'correo': forms.EmailInput(attrs={
					'class': 'form-control',
					'autofocus':'autofocus'
					}),
				'fechanacimiento': forms.DateInput(format=('%d-%m-%Y'),attrs={
					'class': 'form-control',
					'autofocus':'autofocus',
					'type':'date'
					}),
				'fechacontratacion': forms.DateInput(format=('%d-%m-%Y'),attrs={
					'class': 'form-control',
					'autofocus':'autofocus',
					'type':'date'
					}),
				'estado': forms.CheckboxInput(attrs={
					'class': 'form-control',
					'autofocus':'autofocus',
					'type':'date'
					}),

		}

class CargoForm(ModelForm):
	class Meta:
		model = Cargo
		fields= '__all__'
		widgets={
				'cargo': forms.TextInput(attrs={
					'class': 'form-control',
					'autofocus':'autofocus'
					}),

		}

class ProveedorForm(ModelForm):
	class Meta:
		model = Proveedor
		fields= '__all__'
		widgets={
				'direccion': forms.Textarea(attrs={
					'class': 'form-control',
					'autofocus':'autofocus'
					}),
				'correo': forms.EmailInput(attrs={
					'class': 'form-control',
					'autofocus':'autofocus'
					}),
			}

class ProfesionForm(ModelForm):
	class Meta:
		model = Profesion
		fields= '__all__'
		widgets={
			}

class MedicamentoForm(ModelForm):
	class Meta:
		model = Medicamento
		fields= '__all__'
		widgets={
			'fechaelaboracion': forms.DateInput(format=('%d-%m-%Y'),attrs={
					'class': 'form-control',
					'autofocus':'autofocus',
					'type':'date'
					}),
			'fechaVencimiento': forms.DateInput(format=('%d-%m-%Y'),attrs={
					'class': 'form-control',
					'autofocus':'autofocus',
					'type':'date'
					}),
			}

class EspecialidadForm(ModelForm):
	class Meta:
		model = Especialidad
		fields= '__all__'
		widgets={

		}

class DiagnosticoForm(ModelForm):
	class Meta:
		model = Diagnostico
		fields= '__all__'
		widgets={

		}

class ConfiguracionForm(ModelForm):
	class Meta:
		model= Configuracion
		fields= '__all__'
		widgets={
			'logo': forms.FileInput(attrs={
				'class':'form-control',
				'autofocus':'autofocus'
				}),
			'ubicacion': forms.Textarea(attrs={
				'class':'form-control',
				'autofocus':'autofocus'
				}),
			'correo': forms.EmailInput(attrs={
					'class': 'form-control',
					'autofocus':'autofocus'
					}),

		}

class LocalForm(ModelForm):
	class Meta:
		model = Local
		fields= '__all__'
		widgets={
		
		}

class PrescripcionForm(ModelForm):
	class Meta:
		model = Prescripcion
		fields= '__all__'
		widgets={
			'diagnostico':forms.HiddenInput(attrs={}),
		}

class UsuarioForm(UserCreationForm):
	class Meta:
		model =User
		fields= ['username','first_name', 'last_name', 'password1', 'password2']


class VentaMedicamentoForm(ModelForm):
	empleado=forms.ModelChoiceField(queryset=Empleado.objects.filter(cargo=Cargo.objects.get(pk=4)))
	class Meta:
		model = VentaMedicamento
		fields= '__all__'
		widgets={
		
		}

class DetalleVentaForm(ModelForm):
	class Meta:
		model = DetalleVenta
		fields= '__all__'
		widgets={
		
		}
		