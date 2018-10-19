from django.conf.urls import url
from . import views

# /clinica/

app_name='clinica'

urlpatterns =[

	url(r'^$', views.cajero, name='cajero'),
	url(r'^admin/$', views.admin, name='admin'),
	url(r'^medic/$', views.medi, name='medi'),
	url(r'^farmaceutico/$', views.farma, name='farma'),
	
	url(r'^configuracion/$', views.configuracion, name='configuracion'),

	url(r'^paciente/$', views.paciente, name='paciente'),
	url(r'^paciente/(?P<id>\d+)/$', views.editarpaciente, name='editarpaciente'),
	url(r'^paciente/nuevo/$', views.nuevopaciente, name='nuevopaciente'),
	url(r'^paciente/buscar/$', views.buscarpaciente, name='buscarpaciente'),

	url(r'^medico/$', views.medico, name='medico'),
	url(r'^medico/(?P<id>\d+)/$', views.editarmedico, name='editarmedico'),
	url(r'^medico/nuevo/$', views.nuevomedico, name='nuevomedico'),
	# url(r'^medico/buscar/$', views.buscarmedico, name='buscarmedico'),

	url(r'^empleado/$', views.empleado, name='empleado'),
	url(r'^empleado/(?P<id>\d+)/$', views.editarempleado, name='editarempleado'),
	url(r'^empleado/nuevo/$', views.nuevoempleado, name='nuevoempleado'),
	url(r'^empleado/buscar/$', views.buscarempleado, name='buscarempleado'),

	url(r'^cargo/$', views.cargo, name='cargo'),
	url(r'^cargo/(?P<id>\d+)/$', views.editarcargo, name='editarcargo'),
	url(r'^cargo/nuevo/$', views.nuevocargo, name='nuevocargo'),

	url(r'^especialidad/$', views.especialidad, name='especialidad'),
	url(r'^especialidad/(?P<id>\d+)/$', views.editarespecialidad, name='editarespecialidad'),
	url(r'^especialidad/nuevo/$', views.nuevoespecialidad, name='nuevoespecialidad'),

	url(r'^usuario/$', views.usuario, name='usuario'),
	url(r'^usuario/nuevo/$', views.nuevousuario, name='nuevousuario'),

	url(r'^local/$', views.local, name='local'),
	url(r'^local/(?P<id>\d+)/$', views.editarlocal, name='editarlocal'),
	url(r'^local/nuevo/$', views.nuevolocal, name='nuevolocal'),

	url(r'^proveedor/$', views.proveedor, name='proveedor'),
	url(r'^proveedor/(?P<id>\d+)/$', views.editarproveedor, name='editarproveedor'),
	url(r'^proveedor/nuevo/$', views.nuevoproveedor, name='nuevoproveedor'),

	url(r'^profesion/$', views.profesion, name='profesion'),
	url(r'^profesion/(?P<id>\d+)/$', views.editarprofesion, name='editarprofesion'),
	url(r'^profesion/nuevo/$', views.nuevoprofesion, name='nuevoprofesion'),

	url(r'^medicamento/$', views.medicamento, name='medicamento'),
	url(r'^medicamento/(?P<id>\d+)/$', views.editarmedicamento, name='editarmedicamento'),
	url(r'^medicamento/nuevo/$', views.nuevomedicamento, name='nuevomedicamento'),

	url(r'^diagnostico/$', views.diagnostico, name='diagnostico'),
	url(r'^diagnostico/(?P<id>\d+)/$', views.editardiagnostico, name='editardiagnostico'),
	url(r'^diagnostico/nuevo/$', views.nuevodiagnostico, name='nuevodiagnostico'),

	url(r'^prescripcion/(?P<id>\d+)/$', views.prescripcion, name='prescripcion'),
	url(r'^prescripcion/add/$', views.addprescripcion, name='addprescripcion'),

	url(r'^historial/(?P<id>\d+)/$', views.historial, name='historial'),
	
	url(r'^pago/$', views.listacobro, name='listacobro'),
	url(r'^pago/(?P<id>\d+)/$', views.pago, name='pago'),
	url(r'^pago/recibo/(?P<id>\d+)/$', views.recibo, name='recibo'),

	url(r'^venta/$', views.venta, name='venta'),
	url(r'^venta/nuevo/$', views.nuevoventa, name='nuevoventa'),

	url(r'^venta/(?P<id>\d+)/detalle/$', views.detalle, name='detalle'),
	url(r'^detalle/nuevo/(?P<id>\d+)/$', views.nuevodetalle, name='nuevodetalle'),



	

]