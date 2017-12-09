# coding=utf-8
from django import forms
from .models import *
from app_base.models import *


DIAS = ((u'Segunda-feira','Segunda-feira'), (u'Terça-feira','Terca-feira'), (u'Quarta-feira','Quarta-feira'), (u'Quinta-feira','Quinta-feira')
        , (u'Sexta-feira','Sexta-feira'), (u'Sábado','Sabado'))
PERIODO= ((u'Manha', 'Manha'), (u'Tarde', 'Tarde'), (u'Manha e Tarde','Manha_e_Tarde'))

class FormDias(forms.ModelForm):
    dia = forms.ChoiceField(choices=DIAS, label="Dias",widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = Dias
        fields = ('dia',)

class FormEscala(forms.ModelForm):
    professional = forms.ModelChoiceField(label="Profissional",queryset=Profissional.objects.all(),widget=forms.Select(attrs={'class': 'form-control'}))
    days_of_service = forms.ModelMultipleChoiceField(label='Dias de Serviços',queryset=Dias.objects.all(),widget=forms.Select(attrs={'class': 'form-control'}))
    period = forms.ChoiceField(label="Período",choices=PERIODO,widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = Escala
        fields = ("professional","days_of_service","period")

class FormAgendaOdonto(forms.ModelForm):
    client = forms.ModelChoiceField(label="Cliente", queryset=Contrato_Odontologico.objects.all(),widget=forms.Select(attrs={'class': 'form-control'}))
    day_of_service = forms.ModelChoiceField(label="Dias de Serviço",queryset=Escala.objects.all(),widget=forms.Select(attrs={'class': 'form-control'}))
    date_to_service = forms.DateField(label="Data para o atendimento", widget=forms.DateInput(attrs={"type":"date"}))
    hour_to_service = forms.TimeField(widget=forms.TimeInput(attrs={'type':'time','class':"form-control"}))

    class Meta:
        model = Agenda_Odonto
        fields = ("client","day_of_service","hour_to_service")

class FormAgendaPsico(forms.ModelForm):
    client = forms.ModelChoiceField(label="Cliente",queryset=Contrato_Psicologicos.objects.all(),
                                    widget=forms.Select(attrs={'class': 'form-control'}))
    day_of_service = forms.ModelChoiceField(label="Dias de Serviço",queryset=Escala.objects.all(),
                                             widget=forms.Select(attrs={'class': 'form-control'}))
    hour_to_service = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time','class': "form-control"}))

    class Meta:
        model = Agenda_Psico
        fields = ("client","day_of_service","hour_to_service")

class FormAgendaNutri(forms.ModelForm):
    client = forms.ModelChoiceField(label="Cliente",queryset=Contrato_Nutricional.objects.all(),
                                    widget=forms.Select(attrs={'class': 'form-control'}))
    day_of_service = forms.ModelChoiceField(label="Dias de Serviço",queryset=Escala.objects.all(),
                                             widget=forms.Select(attrs={'class': 'form-control'}))
    hour_to_service = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time','class': "form-control"}))

    class Meta:
        model = Agenda_Nutri
        fields = ("client","day_of_service","hour_to_service")

