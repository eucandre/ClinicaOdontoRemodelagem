from django.shortcuts import render
from .forms import *

def InsereDias(request):
    if request.method =="POST":
        form = FormDias(request.POST)
        if form.is_valid():
            item= form.save(commit=False)
            item.user= request.user
            item.save()
    else:
        form = FormDias()
    return render(request, "forms_app_atendimento/Cadastra_Dias.html", {"form":form})

def InsereEscala(request):
    if request.method =="POST":
        form = FormEscala(request.POST)
        if form.is_valid():
            item= form.save(commit=False)
            item.user= request.user
            item.save()
    else:
        form = FormEscala()
    return render(request, "forms_app_atendimento/Cadastra_Escala.html", {"form":form})

def InsereAgendaOdonto(request):
    if request.method =="POST":
        form = FormAgendaOdonto(request.POST)
        if form.is_valid():
            item= form.save(commit=False)
            item.user= request.user
            item.save()
    else:
        form = FormAgendaOdonto()
    return render(request, "forms_app_atendimento/Cadastra_Agenda_Odonto.html", {"form":form})

def InsereAgendaPsico(request):
    if request.method =="POST":
        form = FormAgendaPsico(request.POST)
        if form.is_valid():
            item= form.save(commit=False)
            item.user= request.user
            item.save()
    else:
        form = FormAgendaPsico()
    return render(request, "forms_app_atendimento/Cadastroa_Agenda_Psico.html", {"form":form})

def InsereAgendaNutri(request):
    if request.method =="POST":
        form = FormAgendaNutri(request.POST)
        if form.is_valid():
            item= form.save(commit=False)
            item.user= request.user
            item.save()
    else:
        form = FormAgendaNutri()
    return render(request, "forms_app_atendimento/Cadastra_Agenda_Nutri.html", {"form":form})
