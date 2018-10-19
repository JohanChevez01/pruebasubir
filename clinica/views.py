from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.db.models import Q
from django.db.models import Sum

@login_required()
def admin(request):
	paciente=Paciente.objects.all().count()
	empleado=Empleado.objects.all().count()
	diagnostico=Diagnostico.objects.all().count()
	return render(request,'admin.html',{'paciente':paciente, 'empleado':empleado,'diagnostico':diagnostico})

@login_required()
def medi(request):
	paciente=Paciente.objects.all().count()
	empleado=Empleado.objects.all().count()
	diagnostico=Diagnostico.objects.all().count()
	return render(request,'medi.html',{'paciente':paciente})
	
@login_required()
def cajero(request):
	paciente=Paciente.objects.all().count()
	empleado=Empleado.objects.all().count()
	diagnostico=Diagnostico.objects.all().count()
	return render(request,'cajero.html')

@login_required()
def farma(request):
	paciente=Paciente.objects.all().count()
	empleado=Empleado.objects.all().count()
	diagnostico=Diagnostico.objects.all().count()
	return render(request,'farma.html')

@login_required()
def configuracion(request):
	form=ConfiguracionForm()
	return render(request,'configuracion.html', {'form':form})



#=============PACIENTE=============================================
@login_required()
def paciente(request):
	paciente= Paciente.objects.all()
	form=PacienteForm()
	for field in form.fields:
		form.fields[field].widget.attrs={
			'class': 'form-control',
			# 'style':'bdhsfdkjsnflk'
		}
	return render(request,'paciente.html',{'paciente':paciente,'form':form})

@login_required()
def editarpaciente(request,id):
	editarpaciente= Paciente.objects.get(pk=id)

	if request.method=='GET':
		form=PacienteForm(instance=editarpaciente)
		for field in form.fields:
			form.fields[field].widget.attrs['class']='form-control'
	else:
		form=PacienteForm(request.POST,instance=editarpaciente)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('clinica:paciente'))
	return render(request,'editarpaciente.html',{'form':form})

@login_required()
def nuevopaciente(request):
	if request.method == 'POST' :
		form = PacienteForm(request.POST)

		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('clinica:paciente'))
		else:
			paciente=Paciente.objects.all()
			return render(request,'paciente.html',{'paciente':paciente})
	else:
		return HttpResponse("Utilice el metodo POST")

@login_required
def buscarpaciente(request):
	valor=request.GET['valor']
	paciente= Paciente.objects.filter(Q(identidad__icontains=valor.strip()) | 
									Q(nombre__icontains=valor.strip()) | 
									Q(apellido__icontains=valor.strip()))

	text=""
	index = 0

	if str(request.GET['valor'].strip()) == '':
		paciente= Paciente.objects.all()
	for p in paciente:
		# index += 1
		text+='''<tr>
						<td><strong>{}</strong></td>
						<td>{} {}</td>
						<td>{}<strong> / </strong>{}</td>
						<td>{}</td>
						<td>
						<div class="btn-group" role="group" style="color:orange">
		    				<button id="btnGroupDrop1" type="button" class="btn btn-secondary dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" >
								<img src="/static/media/accion.png" alt="img" style="margin: auto;width:20px; align:right" >
		    				</button>
					    	<div class="dropdown-menu" aria-labelledby="btnGroupDrop1">
					    		<a class="dropdown-item" href="/clinica/paciente/{}/">
					    			<img src="/static/media/editar.png" alt="img" style="margin: auto;width:20px; align:right" ><strong>  Editar</strong>
					    		</a>
					      		<a class="dropdown-item" href="#">
					      			<img src="/static/media/historial.png/" alt="img" style="margin: auto;width:20px; align:right" ><strong>  Historial</strong>
					      		</a>
					    	</div>
					  	</div>
					</td>

					</tr>'''.format( str(p.identidad), str(p.nombre), str(p.apellido), str(p.celular), str(p.telcasa), str(p.correo), str(p.id) )
	return JsonResponse({'listado': text})
	

#======================================================================================		
#=============================================MEDICO===================================
#======================================================================================

@login_required()
def medico(request):
	cargo=Cargo.objects.get(pk='1')
	medico= Empleado.objects.filter(cargo=cargo)
	form=EmpleadoForm()
	for field in form.fields:
		form.fields[field].widget.attrs={
			'class': 'form-control',
			# 'style':'bdhsfdkjsnflk'
		}
	locales_ocupados = []
	for m in medico:
		locales_ocupados.append(int(m.local.id))
	form.fields['local'].queryset = Local.objects.exclude(id__in = locales_ocupados)
	return render(request,'medico.html',{'medico':medico,'form':form})

@login_required()
def editarmedico(request,id):
	editarmedico= Empleado.objects.get(pk=id)
	
	if request.method=='GET':
		form=EmpleadoForm(instance=editarmedico)
	else:
		form=EmpleadoForm(request.POST,instance=editarmedico)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('clinica:medico'))
	return render(request,'editarmedico.html',{'form':form})

@login_required()
def nuevomedico(request):
	if request.method == 'POST' :
		form = EmpleadoForm(request.POST)

		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('clinica:medico'))
		else:
			empleado=Empleado.objects.all()
			return render(request,'medico.html',{'empleado':empleado})
	else:
		return HttpResponse("Utilice el metodo POST")

@login_required
def buscarmedico(request):
	valor=request.GET['valor']
	cargo=Cargo.objects.get(pk=1)
	medico= Empleado.objects.filter(Q(nombre__icontains=valor.strip()) | 
									Q(apellido__icontains=valor.strip()), cargo = cargo)

	text=""
	index = 0

	if str(request.GET['valor'].strip()) == '':
		medico= Empleado.objects.filter(cargo = cargo)
	for m in medico:
		index += 1
		text+='''<tr>
							<td>{}</td>
							<td>{} {}</td>
							<td>{}<strong> / </strong>{}</td>
							<td>{}</td>
							<td>
								<div class="btn-group" role="group" style="color:orange">
		    						<button id="btnGroupDrop1" type="button" class="btn btn-secondary dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" >
										<img src="/static/media/accion.png/" alt="img" style="margin: auto;width:20px; align:right" >
		    						</button>
							    	<div class="dropdown-menu" aria-labelledby="btnGroupDrop1">
							    		<a class="dropdown-item" href="/clinica/editarmedico/{}/">
					    					<img src="/static/media/editar.png/" alt="img" style="margin: auto;width:20px; align:right" ><strong>  Editar</strong>
					    				</a>
							    	</div>
							  	</div>
							</td>

						</tr>'''.format(str(index), str(m.nombre), str(m.apellido), str(m.celular), str(m.telcasa), str(m.correo), str(m.id) )
	return JsonResponse({'listado': text})



#======================================================================================		
#=============================================EMPLEADO===================================

@login_required()
def empleado(request):
	empleado=Empleado.objects.exclude(cargo=Cargo.objects.get(pk=1))

	form=EmpleadoForm()
	for field in form.fields:
		form.fields[field].widget.attrs={
			'class': 'form-control',
			# 'style':'bdhsfdkjsnflk'
		}

	locales_ocupados = []
	for e in empleado:
		locales_ocupados.append(int(e.local.id))
	form.fields['local'].queryset = Local.objects.exclude(id__in = locales_ocupados)

	return render(request,'empleado.html',{'empleado':empleado,'form':form})

@login_required()
def editarempleado(request,id):
	editarempleado= Empleado.objects.get(pk=id)
	
	if request.method=='GET':
		form=EmpleadoForm(instance=editarempleado)
	else:
		form=EmpleadoForm(request.POST,instance=editarempleado)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('clinica:empleado'))
	return render(request,'editarempleado.html',{'form':form})

@login_required()
def nuevoempleado(request):
	if request.method == 'POST' :
		form = EmpleadoForm(request.POST)

		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('clinica:empleado'))
		else:
			empleado=Empleado.objects.all()
			return render(request,'empleado.html',{'empleado':empleado})
	else:
		return HttpResponse("Utilice el metodo POST")


@login_required
def buscarempleado(request):
	valor=request.GET['valor']
	empleado= Empleado.objects.filter(Q(nombre__icontains=valor.strip()) | 
									Q(apellido__icontains=valor.strip()), cargo = cargo)
	
	text=""
	index = 0

	if str(request.GET['valor'].strip()) == '':
		empleado= Empleado.objects.all()
	for e in empleado:
		# index += 1
		text+='''<tr>
							<td>{} {}</td>
							<td>{}<strong> / </strong>{}</td>
							<td>{}</td>
							<td>
								<div class="btn-group" role="group" style="color:orange">
		    						<button id="btnGroupDrop1" type="button" class="btn btn-secondary dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" >
										<img src="/static/media/accion.png/" alt="img" style="margin: auto;width:20px; align:right" >
		    						</button>
							    	<div class="dropdown-menu" aria-labelledby="btnGroupDrop1">
							    		<a class="dropdown-item" href="/clinica/editarempleado/{}/">
					    					<img src="/static/media/editar.png/" alt="img" style="margin: auto;width:20px; align:right" ><strong>  Editar</strong>
					    				</a>
							    	</div>
							  	</div>
							</td>

						</tr>'''.format(str(e.nombre), str(e.apellido), str(e.celular), str(e.telcasa), str(e.correo), str(e.id) )
	return JsonResponse({'listado': text})

#================================================================
#=============CARGO==============================================
#================================================================
@login_required()
def cargo(request):
	cargo= Cargo.objects.all()
	form=CargoForm()
	for field in form.fields:
		form.fields[field].widget.attrs={
			'class': 'form-control',
			# 'style':'bdhsfdkjsnflk'
		}
	return render(request,'cargo.html',{'cargo':cargo,'form':form})

@login_required()
def editarcargo(request,id):
	editarcargo= Cargo.objects.get(pk=id)
	

	if request.method=='GET':
		form=CargoForm(instance=editarcargo)
		for field in form.fields:
			form.fields[field].widget.attrs['class']='form-control'
	else:
		form=CargoForm(request.POST,instance=editarcargo)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('clinica:cargo'))
	return render(request,'editarcargo.html',{'form':form})

@login_required()
def nuevocargo(request):
	if request.method == 'POST' :
		form = CargoForm(request.POST)

		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('clinica:cargo'))
		else:
			cargo=Cargo.objects.all()
			return render(request,'cargo.html',{'cargo':cargo})
	else:
		return HttpResponse("Utilice el metodo POST")

#================================================================
#=============ESPECIALIDAD=======================================
#================================================================
@login_required()
def especialidad(request):
	especialidad= Especialidad.objects.all()
	form=EspecialidadForm()
	for field in form.fields:
		form.fields[field].widget.attrs={
			'class': 'form-control',
			# 'style':'bdhsfdkjsnflk'
		}
	return render(request,'especialidad.html',{'especialidad':especialidad,'form':form})

@login_required()
def editarespecialidad(request,id):
	editarespecialidad= Especialidad.objects.get(pk=id)
	

	if request.method=='GET':
		form=EspecialidadForm(instance=editarespecialidad)
		for field in form.fields:
			form.fields[field].widget.attrs['class']='form-control'
	else:
		form=EspecialidadForm(request.POST,instance=editarespecialidad)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('clinica:especialidad'))
	return render(request,'editarespecialidad.html',{'form':form})

@login_required()
def nuevoespecialidad(request):
	if request.method == 'POST' :
		form = EspecialidadForm(request.POST)

		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('clinica:especialidad'))
		else:
			especialidad=Especialidad.objects.all()
			return render(request,'especialidad.html',{'especialidad':especialidad})
	else:
		return HttpResponse("Utilice el metodo POST")

#==================================================================
#================LOCAL=============================================
#==================================================================
@login_required()
def local(request):
	local= Local.objects.all()
	form=LocalForm()
	for field in form.fields:
		form.fields[field].widget.attrs={
			'class': 'form-control',
			# 'style':'bdhsfdkjsnflk'
		}
	return render(request,'local.html',{'local':local,'form':form})

@login_required()
def editarlocal(request,id):
	editarlocal= Local.objects.get(pk=id)

	if request.method=='GET':
		form=LocalForm(instance=editarlocal)
		for field in form.fields:
			form.fields[field].widget.attrs['class']='form-control'
	else:
		form=LocalForm(request.POST,instance=editarlocal)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('clinica:local'))
	return render(request,'editarlocal.html',{'form':form})

@login_required()
def nuevolocal(request):
	if request.method == 'POST' :
		form = LocalForm(request.POST)

		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('clinica:local'))
		else:
			local=Local.objects.all()
			return render(request,'local.html',{'local':local})
	else:
		return HttpResponse("Utilice el metodo POST")


#==================================================================
#================PROVEEDOR=========================================
#==================================================================
@login_required()
def proveedor(request):
	proveedor= Proveedor.objects.all()
	form=ProveedorForm()
	for field in form.fields:
		form.fields[field].widget.attrs={
			'class': 'form-control',
			# 'style':'bdhsfdkjsnflk'
		}
	return render(request,'proveedor.html',{'proveedor':proveedor,'form':form})

@login_required()
def editarproveedor(request,id):
	editarproveedor= Proveedor.objects.get(pk=id)

	if request.method=='GET':
		form=ProveedorForm(instance=editarproveedor)
		for field in form.fields:
			form.fields[field].widget.attrs['class']='form-control'
	else:
		form=ProveedorForm(request.POST,instance=editarprofesion)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('clinica:proveedor'))
	return render(request,'editarproveedor.html',{'form':form})

@login_required()
def nuevoproveedor(request):
	if request.method == 'POST' :
		form = ProveedorForm(request.POST)

		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('clinica:proveedor'))
		else:
			proveedor=Proveedor.objects.all()
			return render(request,'proveedor.html',{'proveedor':proveedor})
	else:
		return HttpResponse("Utilice el metodo POST")


#==================================================================
#================PROFESION=========================================
#==================================================================
@login_required()
def profesion(request):
	profesion= Profesion.objects.all()
	form=ProfesionForm()
	for field in form.fields:
		form.fields[field].widget.attrs={
			'class': 'form-control',
			# 'style':'bdhsfdkjsnflk'
		}
	return render(request,'profesion.html',{'profesion':profesion,'form':form})

@login_required()
def editarprofesion(request,id):
	editarprofesion= Profesion.objects.get(pk=id)

	if request.method=='GET':
		form=ProfesionForm(instance=editarprofesion)
		for field in form.fields:
			form.fields[field].widget.attrs['class']='form-control'
	else:
		form=ProfesionForm(request.POST,instance=editarprofesion)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('clinica:profesion'))
	return render(request,'editarprofesion.html',{'form':form})

@login_required()
def nuevoprofesion(request):
	if request.method == 'POST' :
		form = ProfesionForm(request.POST)

		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('clinica:profesion'))
		else:
			profesion=Profesion.objects.all()
			return render(request,'profesion.html',{'profesion':profesion})
	else:
		return HttpResponse("Utilice el metodo POST")


#======================================================================================		
#=================================MEDICAMENTO==========================================
#======================================================================================

@login_required()
def medicamento(request):
	medicamento= Medicamento.objects.all()
	form=MedicamentoForm()
	for field in form.fields:
		form.fields[field].widget.attrs={
			'class': 'form-control',
			# 'style':'bdhsfdkjsnflk'
		}
	return render(request,'medicamento.html',{'medicamento':medicamento,'form':form})

@login_required()
def editarmedicamento(request,id):
	editarmedicamento= Medicamento.objects.get(pk=id)

	if request.method=='GET':
		form=MedicamentoForm(instance=editarmedicamento)
		for field in form.fields:
			form.fields[field].widget.attrs['class']='form-control'
	else:
		form=MedicamentoForm(request.POST,instance=editarmedicamento)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('clinica:medicamento'))
	return render(request,'editarmedicamento.html',{'form':form})

@login_required()
def nuevomedicamento(request):
	if request.method == 'POST' :
		form = MedicamentoForm(request.POST)

		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('clinica:medicamento'))
		else:
			medicamento=Medicamento.objects.all()
			return render(request,'medicamento.html',{'medicamento':medicamento})
	else:
		return HttpResponse("Utilice el metodo POST")

#===========================================================================
#=============consultas medicas=============================================
#===========================================================================
@login_required()
def diagnostico(request):
	consulta= Diagnostico.objects.all()
	form=DiagnosticoForm()
	cargo = Cargo.objects.get(cargo="Medico")
	form.fields['empleado'].queryset = Empleado.objects.filter(cargo=cargo)
	for field in form.fields:
		form.fields[field].widget.attrs={
			'class': 'form-control',
			# 'style':'bdhsfdkjsnflk'
		}
	return render(request,'consultamedica.html',{'consulta':consulta,'form':form})

@login_required()
def editardiagnostico(request,id):
	editardiagnostico= Diagnostico.objects.get(pk=id)
	

	if request.method=='GET':
		form=DiagnosticoForm(instance=editardiagnostico)
		for field in form.fields:
			form.fields[field].widget.attrs['class']='form-control'
	else:
		form=DiagnosticoForm(request.POST,instance=editardiagnostico)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('clinica:diagnostico'))
	return render(request,'editardiagnostico.html',{'form':form})

@login_required()
def nuevodiagnostico(request):
	if request.method == 'POST' :
		form = DiagnosticoForm(request.POST)

		if form.is_valid():
			d=form.save()
			pc =PagoConsulta(paciente=d.paciente, empleado=d.empleado, precio="250", estado="False")
			pc.save()
			return HttpResponseRedirect(reverse('clinica:diagnostico'))
		else:
			diagnostico=Diagnostico.objects.all()
			return render(request,'consultamedica.html',{'diagnostico':diagnostico})
	else:
		return HttpResponse("Utilice el metodo POST")

#===========================================================================
#=======================PRESCRIPCION========================================
#===========================================================================
@login_required()
def prescripcion(request, id):
	diagnostico = Diagnostico.objects.get(pk = id)
	form=PrescripcionForm(initial={'diagnostico': diagnostico})
	for field in form.fields:
		form.fields[field].widget.attrs={
			'class': 'form-control',
			# 'style':'bdhsfdkjsnflk'
		}
	return render(request,'prescripcion.html',{'form':form})

#===========================================================================
#===========================USUARIO=========================================
#===========================================================================

@login_required()
def usuario(request):
	user = User.objects.all()
	form = UsuarioForm()
	for field in form.fields:
		form.fields[field].widget.attrs={
			'class': 'form-control',
			# 'style':'bdhsfdkjsnflk'
		}
	return render(request,'usuario.html',{'user':user,'form':form})

@login_required()
def nuevousuario(request):
	if request.method == 'POST' :
		form = UsuarioForm(request.POST)

		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('clinica:usuario'))
		else:
			user=User.objects.all()
			return render(request,'paciente.html',{'user':user})
	else:
		return HttpResponse("Utilice el metodo POST")

@login_required()
def historial(request,id):
	paciente=Paciente.objects.get(pk=id)
	diagnostico=Diagnostico.objects.filter(paciente=paciente)
	prescripcion=Prescripcion.objects.filter(diagnostico=diagnostico)

	data={
		'paciente':paciente,
		'diagnostico':diagnostico,
		'prescripcion':prescripcion,
	}

	return render(request, 'historial.html', data)


@login_required()
def addprescripcion(request):
	if request.method == 'POST' :
		form = PrescripcionForm(request.POST)

		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('clinica:diagnostico'))
	

#===========================================================================
#===========================Pago de Citas===================================
#===========================================================================

@login_required()
def listacobro(request):
	cobrar=PagoConsulta.objects.filter(estado=False)

	ctx={
		'cobros':cobrar
	}

	return render(request, 'pagoconsulta.html', ctx)

@login_required()
def pago(request,id):
	cobrar=PagoConsulta.objects.get(pk=id)

	cobrar.estado=True
	cobrar.save()

	return HttpResponseRedirect(reverse('clinica:recibo', args=(id)))

@login_required()
def recibo(request, id):
	recibo=PagoConsulta.objects.get(pk=id)

	ctx={
		'recibo':recibo,
	}
	
	return render(request, 'recibo.html', ctx)

#===========================================================================
#============================ Venta ========================================
#===========================================================================

def venta(request):
	venta= VentaMedicamento.objects.all()
	form=VentaMedicamentoForm()
	for field in form.fields:
		form.fields[field].widget.attrs={
			'class': 'form-control',
			# 'style':'bdhsfdkjsnflk'
		}
	return render(request,'venta.html',{'venta':venta,'form':form})

@login_required()
def nuevoventa(request):
	
	if request.method == 'POST':
		form = VentaMedicamentoForm(request.POST)

		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('clinica:venta'))
		else:
			venta=VentaMedicamento.objects.all()
			return render(request,'venta.html',{'venta':venta})
	else:
		return HttpResponse("Utilice el metodo POST")

#===========================================================================
#========================Detalle de Venta===================================
#===========================================================================

@login_required()
def detalle(request,id):
	venta=VentaMedicamento.objects.get(id=id)
	detalle= DetalleVenta.objects.filter(ventamedicamento=venta)
	form=DetalleVentaForm(initial={'ventamedicamento':venta})

	form.fields['medicamento'].label='Seleccione el Medicamento'
	form.fields['medicamento'].queryset=Medicamento.objects.filter()

	subtotalt=DetalleVenta.objects.filter(ventamedicamento=venta).aggregate(Sum('subtotal'))

	subtotalt=subtotalt['subtotal__sum']


	if subtotalt is None:
		subtotalt=0.00

	isv =0.00
	isv=float(subtotalt)*0.15
	total=(float(subtotalt)+float(isv))

	data={

		'venta': venta,
		'detalle':detalle, 
		'form':form,
		'subtotalt':subtotalt,
		'isv':isv,
		'total':total
	}
	return render(request,'detalle.html',data)

@login_required()
def nuevodetalle(request, id):
	idV=request.POST['ventamedicamento']
	if request.method == 'POST' :
		form = DetalleVentaForm(data=request.POST)

		if form.is_valid():
			c=form.save()
			return HttpResponseRedirect(reverse('clinica:detalle',args=(id,)))
	else:
		return HttpResponse("Utilice el metodo POST")

