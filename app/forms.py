# -*- coding: utf-8 -*-
from django.forms.widgets import Input
from django import forms
from django.core.validators import email_re

class Html5EmailInput(Input):
    input_type = 'email'

class Html5TelInput(Input):
    input_type = 'tel'


class contactForm(forms.Form):
    nombre = forms.CharField( label = 'Nombre  (*)' , 
    							required = True, 
    							widget= forms.TextInput(attrs={'placeholder' : 'Nombre',
    															'required' : '1'}))
    email = forms.EmailField( label = 'E-mail  (*)' ,
    							required = True, 
    							widget=Html5EmailInput(attrs={'placeholder' : 'ejemplo@ejemplo.cl',
    															'required' : '1'}))
    telefono = forms.IntegerField( label = 'Teléfono (Opcional)' , 
    								widget=Html5TelInput(attrs={'placeholder' : '1234 567'}))
    
    asunto = forms.CharField( label = 'Asunto  (*)' , 
                                required = True, 
                                widget = forms.TextInput(attrs={'placeholder' : 'Presupuesto',
                                                        'required' : '1'}))

    mensaje = forms.CharField( label = 'Mensaje  (*)' , 
                                widget = forms.Textarea(attrs={'placeholder' : 'Escriba su mensaje aqui',
                                                                'required' : '1'}), 
                                required = True)

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        words = len(nombre.strip())
        if words == 0:
            raise forms.ValidationError('No ingrese espacios en blanco')
        elif words < 3:
            raise forms.ValidationError('Ingresar Nombre superior a 3 caracteres')
        return nombre

    def clean_mensaje(self):
        mensaje = self.cleaned_data['mensaje']
        words = len(mensaje.strip())
        if words == 0:
            raise forms.ValidationError('No ingrese espacios en blanco')
        elif words < 10:
            raise forms.ValidationError('Ingresar mas de 10 caracteres')
        return mensaje

    def clean_email(self):
        email = self.cleaned_data['email']
        if self.is_valid_email(email) == False:
            raise forms.ValidationError('E-mail debe ser valido')
        return email

    def is_valid_email(request, email):
        encontrado = False
        if email_re.match(email):
            encontrado = True
        return encontrado

    def clean_telefono(self):
        telefono = self.cleaned_data['telefono']
        tel = int(telefono)
        words = len(str(tel).strip())
        if words < 7:
            raise forms.ValidationError('Debe ingresar número de teléfono mayor a 6 dígitos')
        return telefono

    def clean_asunto(self):
        asunto = self.cleaned_data['asunto']
        words = len(asunto.strip())
        if words == 0:
            raise forms.ValidationError('Debe ingresar el asunto')
        elif words < 3:
            raise forms.ValidationError('Ingresar más de 3 caracteres')
        return asunto        