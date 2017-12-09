from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.shortcuts import render
from app_base.forms import *
from app_atendimento.models import *

def apresenta_atendimento(request):

    obj_dias = Dias.objects.all()
    obj_esca = Escala.objects.all()
    obj_agdo = Agenda_Odonto.objects.all()

    obj_agps = Agenda_Psico.objects.all()

    data_escala = "Sem dado"
    data_Agodo ="Sem dado"

    page = request.GET.get('page',1)
    paginator = Paginator(obj_agdo,10)
    try:
        p_data_agodo = paginator.page(page)
    except PageNotAnInteger:
        p_data_agodo = paginator.page(1)
    except EmptyPage:
        p_data_agodo = paginator.page(paginator.num_pages)
    return render(request, "index2.html",{"agenda_odonto":p_data_agodo})

def apresenta_atendimento_Nutri(request):

    obj_agnt = Agenda_Nutri.objects.all()
    page = request.GET.get('page',1)
    paginator = Paginator(obj_agnt,10)
    try:
        p_data_agnt = paginator.page(page)
    except PageNotAnInteger:
        p_data_agnt = paginator.page(1)
    except EmptyPage:
        p_data_agnt = paginator.page(paginator.num_pages)
    return render(request,"index3.html",{"agenda_nutri": p_data_agnt})

def apresenta_atendimento_Psico(request):

    obj_agps = Agenda_Psico.objects.all()
    page = request.GET.get('page',1)
    paginator = Paginator(obj_agps,10)
    try:
        p_data_agps = paginator.page(page)
    except PageNotAnInteger:
        p_data_agps = paginator.page(1)
    except EmptyPage:
        p_data_agps = paginator.page(paginator.num_pages)
    return render(request,"index3.html",{"agenda_psico": p_data_agps})