from django.shortcuts import render, redirect, get_object_or_404
from .models import Variables


def lista_variables(request):
    variables = Variables.objects.all()
    return render(request, 'lista_variables.html', {'variables': variables})

def agregar_variables(request):
    if request.method == 'POST':
        temperatura = request.POST.get('temperatura')
        humedad = request.POST.get('humedad')
        luz = request.POST.get('luz')
        Variables.objects.create(temperatura=temperatura, humedad=humedad, luz=luz)
        return redirect('gestionar_variables')
    return render(request, 'agregar_variables.html')

def eliminar_variable(request, variable_id):
    variable = get_object_or_404(Variables, id=variable_id)
    variable.delete()
    return redirect('gestionar_variables')

def modificar_variable(request, variable_id):
    variable = get_object_or_404(Variables, id=variable_id)
    if request.method == 'POST':
        variable.temperatura = request.POST.get('temperatura')
        variable.humedad = request.POST.get('humedad')
        variable.luz = request.POST.get('luz')
        variable.save()
        return redirect('gestionar_variables')
    return render(request, 'modificar_variable.html', {'variable': variable})

def gestionar_variables(request):
    if request.method == 'POST':
        temperatura = request.POST.get('temperatura')
        humedad = request.POST.get('humedad')
        luz = request.POST.get('luz')
        Variables.objects.create(temperatura=temperatura, humedad=humedad, luz=luz)
        return redirect('gestionar_variables')

    variables = Variables.objects.all()
    return render(request, 'gestionar_variables.html', {'variables': variables})
