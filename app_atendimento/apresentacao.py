from django.shortcuts import render
from app_base.forms import *
from app_atendimento.models import *

def apresenta_atendimento(request):
    obj_dias = Dias.objects.all()
    obj_esca = Escala.objects.all()
    obj_agdo = Agenda_Odonto.objects.all()
    obj_agnt = Agenda_Nutri.objects.all()
    obj_agps = Agenda_Psico.objects.all()

    data_escala = "Sem dado"
    data_Agodo ="Sem dado"
    if len(obj_esca)==0:
        data_escala = 0
    elif len(obj_esca)>0:
        data_escala = Escala.objects.get(pk=1)

    if len(obj_agdo)==0:
        data_Agodo= 0
    elif len(obj_agdo)>0:
        data_Agodo = Agenda_Odonto.objects.get(pk=1)

    return render(request, "index2.html",{"ago":data_Agodo.day_of_service.days_of_service})
