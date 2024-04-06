from django.shortcuts import render, get_object_or_404

# Create your views here.
from personas.models import Persona, Domicilio


def detallePersona(request, id):
    #persona = Persona.objects.get(pk=id)
    persona = get_object_or_404(Persona, pk=id)
    return render(request, 'personas/detalle.html', {'persona': persona})

def detalleDomicilio(request, id):
    domicilio = get_object_or_404(Persona, pk=id)
    return render(request, 'personas/detalleDomicilio.html', {'domicilio': domicilio})
