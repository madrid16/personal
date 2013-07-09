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

			if request.is_ajax():
				errores_form = {'errores' : 'errores'}
				json = simplejson.dumps(errores_form)
				return HttpResponse(json)
				# return render_to_response('contenido/contacto.html', locals())

			#return HttpResponseRedirect('http://www.google.cl')
			return render_to_response('contact.html', locals())

		else:
			errores_form = {'errores' : 'errores'}
			json = simplejson.dumps(errores_form)
			return render_to_response('contenido/contacto.html', locals())
			# return HttpResponse(json)
	else:
		form = contactForm()
		return render_to_response('contenido/contacto.html', locals())

# tatianahpppp  tatiana sanches avala

# karla.herrera47