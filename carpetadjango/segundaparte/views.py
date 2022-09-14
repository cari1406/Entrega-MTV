from django.shortcuts import render
from django.http import HttpResponse
from segundaparte.models import Familia
from django.template import loader

def familia(self):
    familia1 = Familia(nombre = "Sol", edad = 24, fecha_nac = "1998-1-15")
    familia1.save()

    familia2 = Familia(nombre = "Virginia", edad = 50, fecha_nac = "1972-2-03")
    familia2.save()

    familia3 = Familia(nombre = "Carlos", edad = 46, fecha_nac = "1976-11-20")
    familia3.save()

    diccionario = {
        "name1": familia1.nombre, "age1": familia1.edad, "birth1": familia1.fecha_nac,
        "name2": familia2.nombre, "age2": familia2.edad, "birth2": familia2.fecha_nac,
        "name3": familia3.nombre, "age3": familia3.edad, "birth3": familia3.fecha_nac,
        }
    
    plantilla = loader.get_template("familiamtv.html")
    document = plantilla.render(diccionario)

    return HttpResponse(document) 
