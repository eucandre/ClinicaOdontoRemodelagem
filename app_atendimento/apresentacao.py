from django.shortcuts import render
from app_base.forms import *
from app_atendimento.models import *

def apresenta_atendimento(request):
    obj_dias = Dias.objects.all()
    obj_esca = Escala.objects.all()
    obj_agdo = Agenda_Odonto.objects.all()
    obj_agnt = Agenda_Nutri.objects.all()
    obj_agps = Agenda_Psico.objects.all()

    data_escala = 0
    if len(obj_esca)!=0:
        for i in range(1,len(obj_esca)):
            data_escala = Escala.objects.get(pk = i)


    return render(request,"index2.html",{"escala":data_escala})