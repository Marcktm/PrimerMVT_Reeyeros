from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context
from django.template import loader
from appFamilia.models import Familia
from appFamilia.forms import FamiliaForms

# Create your views here.

def list_familia(request):
    familia = Familia.objects.all()

    nombreL=[]
    fechaN=[]
    edadL=[]

    for n in familia:
        nombreL.append(n.nombre)
        fechaN.append(n.fNacimiento)
        edadL.append(n.edad)

    datos={"NOMBRE" : nombreL, "FechaNacimiento" : fechaN, "EDAD": edadL}
    plantilla = loader.get_template("listado_familiares.html")
    documento = plantilla.render(datos)

    return HttpResponse(documento)

def addFamiliar(request):

    if request.method == "POST":
        form = FamiliaForms(request.POST)

        if form.is_valid():
            nombre = form.cleaned_data['NOMBRE']
            fechaN = form.cleaned_data['FechaNacimiento']
            edad = form.cleaned_data['EDAD']

            Familia(nombre = nombre, Nacimiento= fechaN, edad = edad).save()

        return render(request, 'appFamilia/add_familiares.html', {'form': form})

    documento={}

    plantilla = loader.get_template("add_familiares.html")
    documento = plantilla.render()

    return HttpResponse(documento)

