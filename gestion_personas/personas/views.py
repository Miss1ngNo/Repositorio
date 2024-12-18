from django.shortcuts import render, redirect
from .models import Persona

def lista_personas(request):
    personas = Persona.objects.all()
    return render(request, 'lista_personas.html', {'personas': personas})

def agregar_persona(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        edad = request.POST['edad']
        Persona.objects.create(nombre=nombre, edad=edad)
        return redirect('lista_personas')
    return render(request, 'agregar_persona.html')

def eliminar_persona(request, persona_id):
    persona = Persona.objects.get(id=persona_id)
    persona.delete()
    return redirect('lista_personas')

def modificar_persona(request, persona_id):
    persona = Persona.objects.get(id=persona_id)
    if request.method == 'POST':
        persona.nombre = request.POST['nombre']
        persona.edad = request.POST['edad']
        persona.save()
        return redirect('lista_personas')
    return render(request, 'modificar_persona.html', {'persona': persona})