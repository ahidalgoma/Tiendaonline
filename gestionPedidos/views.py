from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos
from django.core.mail import send_mail
from django.conf import settings
from gestionPedidos.forms import FormularioContacto

# Create your views here.

def busqueda_productos(request):

    return render(request, "busquedaproductos.html")

def buscar(request):

    if request.GET['prd']:

#        mensaje='Artículo buscado: %r ' %request.GET['prd']
        producto=request.GET['prd']
        if len(producto)>20:
            mensaje='Término de búsqueda demasiado largo'
        else:
            articulos=Articulos.objects.filter(nombre__icontains=producto)
            return render(request, 'resultados_busqueda.html', {"articulos":articulos, "query":producto})
    else:
        mensaje='Texto no introducido'

    return HttpResponse(mensaje)

def contacto(request):

    if request.method=='POST':

        miFormulario=FormularioContacto(request.POST)

        if miFormulario.is_valid():

            infForm=miFormulario.cleaned_data

#           send_mail(infForm['asunto'], infForm['mensaje'], infForm.get('email', ' '),['destinatario@gmail.com'])
           
# para enviar correos. Primero hay que declarar las variables de email en settings.py 
# y debemos importar 
# from django.core.mail import send_mail
# from django.conf import settings

#        subjet=request.POST['asunto']
#        message=request.POST['mensaje'] + ' ' + request.POST['email']
#        email_from=settings.EMAIL_HOST_USER
#        recipient_list=["destinatario@gmail.com"]
#        send_mail(subject, message, email_from, recipient_list)



            return render(request, 'gracias.html', {'asunto':infForm['asunto'], 'mensaje':infForm['mensaje']})
#    return render(request, 'contacto.html')
    else:
        miFormulario=FormularioContacto()
    return render(request, 'formulario_contacto.html', {"form":miFormulario})