from django.forms import modelform_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from personas.forms import PersonaForm
from personas.models import Persona


def bienvenido(request):
    no_personas_var = Persona.objects.count()
    personas = Persona.objects.all()
    return render(request, 'bienvenido.html', {'no_personas': no_personas_var, 'personas': personas})


#PersonaForm = modelform_factory(Persona, exclude=[])


def nuevaPersona(request):
    if request.method == 'POST':
        formaPersona = PersonaForm(request.POST)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('inicio')
    else:
        formaPersona = PersonaForm()

    return render(request, 'personas/nuevo.html', {'formaPersona': formaPersona})
