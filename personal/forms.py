from django import form as forms

class contactForm(request):
    nombre = forms.CharField()
    email = forms.EmailField(required = true)
    asunto = forms.CharField()
    mensaje = forms.CharField(widget = forms.Textarea())