
#security app
from django.shortcuts import render
from django.contrib.auth import login, logout , authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User


def home(request):
	return render(request,'home.html')

def log_out(request):
	logout(request)
	return HttpResponseRedirect(reverse('home'))

def log_in(request):
	if request.method == 'POST':
		form =AuthenticationForm(data=request.POST)

		if form.is_valid():
			u= request.POST['username']
			p= request.POST['password']
			user = authenticate(username= u, password= p) 

			if user is not None:
				if user.is_active:
					login(request,user)

					acceso=User.objects.get(id=request.user.id)

					if str(acceso.empleado.cargo) == "Medico":
						return HttpResponseRedirect(reverse('clinica:medi'))

					elif str(acceso.empleado.cargo) == "Cajero":
						return HttpResponseRedirect(reverse('clinica:cajero'))

					elif str(acceso.empleado.cargo) == "Administrador":
						return HttpResponseRedirect(reverse('clinica:admin'))

					elif str(acceso.empleado.cargo) == "Farmaceutico":
						return HttpResponseRedirect(reverse('clinica:farma'))
					else:
						return HttpResponseRedirect(reverse('home'))
				else:
					return HttpResponseRedirect(reverse('clinica:login_form'))
		else: 
			return render(request, 'login_form.html',{'form': form})
			#return HttpResponse('Formulario invalido')
	else:
		return HttpResponse('Debes utilizar el metodo POST')

def login_form(request):
	# si el usuario no esta logueados
	if not request.user.is_authenticated():
		form=AuthenticationForm()
		return render(request, 'login_form.html',{'form': form})
	else: # estamos loguead
		acceso=User.objects.get(id=request.user.id)

		if str(acceso.empleado.cargo) == "Medico":
			return HttpResponseRedirect(reverse('clinica:medico'))

		elif str(acceso.empleado.cargo) == "Cajero":
			return HttpResponseRedirect(reverse('clinica:cajero'))

		elif str(acceso.empleado.cargo) == "Administrador":
			return HttpResponseRedirect(reverse('clinica:admin'))

		elif str(acceso.empleado.cargo) == "Farmaceutico":
			return HttpResponseRedirect(reverse('clinica:farma'))

