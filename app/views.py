# -*- coding: utf-8 -*-
# Create your views here.
from django.core.context_processors import csrf
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template.loader import get_template
from django.template import RequestContext
from django.template import Context
from django.shortcuts import render_to_response
from forms import contactForm
from django.utils import simplejson
from django.core.mail import EmailMultiAlternatives
from models import contact as contactModel


def index_view(request):
	current = 'inicio'
	title = "Madrid S.A."
	description = "Desarrollo de sistemas y aplicaciones web, servicios TI y consultoria para todo tipo de empresas."
	return render_to_response('index.html', locals())

def inicio(request):
	current = 'inicio'
	title = "Madrid S.A."
	description = "Desarrollo de sistemas y aplicaciones web, servicios TI y consultoria para todo tipo de empresas."
	return render_to_response('index.html', locals())

def contact(request):
	current = 'contacto'
	contacto = "Contáctame"
	form = contactForm()
	title = "Contacto Madrid S.A."
	description = "Cotiza tu proyecto, contactame para desarrollar tu sistema."
	return render_to_response('contact.html', locals())

def nosotrosView(request):
	current = 'nosotros'
	title = "Nosotros Madrid S.A."
	description = "Madrid creado por Edgar Muñoz Madrid, empresa destinada al desarrollo web en la region, maipu, Chile."
	return render_to_response('us.html', locals())

def proyectosView(request):
	current = 'proyectos'
	title = "Proyectos Madrid S.A."
	description = "Proyectos realizados en el tiempo para terceros como piedra azul o clinica davila y sistemas propios como foodmovil."
	return render_to_response('proyects.html', locals())

def serviceView(request):
	current = 'servicios'
	title = "Servicios Madrid S.A."
	description = "Madrid ofrece los mejores servicio TI de la región, desarrollo de aplicaciones web en php o django, ademas de css3 y html5."
	return render_to_response('service.html', locals())	

def serviceApp(request):
	current = 'servicios'
	active = 'app'
	title = "Servicios | Aplicaciones Madrid S.A."
	description = "Desarrollos de aplicaciones web con responsive design y app mobile."
	return render_to_response('service.html', locals())	

def serviceMarketing(request):
	current = 'servicios'
	active = 'marketing'
	title = "Servicios | Marketing Madrid S.A."
	description = "Diseños web de calidad, incluyendo responsive design e interfaces limpias y usables."
	return render_to_response('service.html', locals())	

def serviceMantencion(request):
	current = 'servicios'
	active = 'mantencion'
	title = "Servicios | Mantenciones Madrid S.A."
	description = "Mantenciones de sistemas web, basados en php puro o realizados con un framework."
	return render_to_response('service.html', locals())	

def serviceSolucion(request):
	current = 'servicios'
	active = 'solucion'
	title = "Servicios | Soluciones TI Madrid S.A."
	description = "Soluciones TI para todo tipo de empresas."
	return render_to_response('service.html', locals())	

def contactValid(request):
	if request.method == 'POST':
		form = contactForm(request.POST)

		if form.is_valid():

			nombre = form.cleaned_data['nombre']
			email = form.cleaned_data['email']
			telefono = form.cleaned_data['telefono']
			asunto = form.cleaned_data['asunto']
			mensaje = form.cleaned_data['mensaje']

			contacto = contactModel()
			contacto.con_name = nombre
			contacto.con_email = email
			contacto.con_number = telefono
			contacto.con_subject = asunto
			contacto.con_message = mensaje

			context_text = 'E-mail de TheMadrid.cl Nombre : ' + nombre  + ' E-mail : ' + email + ' Telefono : ' + str(telefono) + ' Asunto : ' + asunto + ' Mensaje : ' + mensaje
			html_content = 'E-mail de TheMadrid.cl <br />Nombre : ' + nombre  + '<br />E-mail : ' + email + '<br />Telefono : ' + str(telefono) + '<br />Asunto : ' + asunto + '<br />Mensaje : ' + mensaje

			if request.is_ajax():
				errores_form = {'errors' : 'errors'}
				json = simplejson.dumps(errores_form)
				
				subject, from_email, to = 'Contact From TheMadrid Service', 'contacto@themadrid.cl', 'm.madrid@themadrid.cl'
				
				msg = EmailMultiAlternatives(subject, context_text, from_email, [to])
				msg.attach_alternative(html_content, "text/html")
				msg.send()
				contacto.save()
			
				return HttpResponse(json)
				
			return render_to_response('contact.html', locals())

		else:
			errores_form = {'error' : 'error'}
			json = simplejson.dumps(errores_form)
			return render_to_response('contenido/contacto.html', locals())
			# return HttpResponse(json)
	else:
		form = contactForm()
		return render_to_response('contenido/contacto.html', locals())

def mantenimiento(request):
	return render_to_response('mantenimiento.html', locals())

def contact_mantenimiento(request):
	
	contacto = contactModel()
	nombre = request.POST['nombre']
	email = request.POST['email']
	asunto = request.POST['asunto']
	mensaje = request.POST['mensaje']
	contacto.con_name = nombre
	contacto.con_email = email
	contacto.con_subject = asunto
	contacto.con_message = mensaje
	
	if contacto.save():
		errores_form = {'contacto' : 'ok'}
	else:
		errores_form = {'contacto' : 'not'}

	json = simplejson.dumps(errores_form)

	return HttpResponse(json)
	# return render_to_response('mantenimiento.html',locals())

def sitemap(request):
	return render_to_response('sitemap.xml')
