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
	return render_to_response('index.html', locals())

def inicio(request):
	return render_to_response('contenido/content.html', locals())

def contact(request):
	contacto = "Contáctame"
	form = contactForm()
	return render_to_response('contenido/contacto.html', locals())

def nosotrosView(request):
	return render_to_response('contenido/nosotros.html', locals())

def proyectosView(request):
	return render_to_response('contenido/proyectos.html', locals())

def serviceView(request):
	return render_to_response('contenido/servicios.html', locals())	

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