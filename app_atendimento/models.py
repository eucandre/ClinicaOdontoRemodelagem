# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from datetime import time
from app_contrato.models import *
from app_base.models import *
from django.contrib.auth.models import *
from simple_history.models import HistoricalRecords

DIAS = ((u'Segunda-feira','Segunda-feira'), (u'Terça-feira','Terca-feira'), (u'Quarta-feira','Quarta-feira'), (u'Quinta-feira','Quinta-feira')
        , (u'Sexta-feira','Sexta-feira'), (u'Sábado','Sabado'))
PERIODO= ((u'Manha', 'Manha'), (u'Tarde', 'Tarde'), (u'Manha e Tarde','Manha_e_Tarde'))
"""
Este módulo contará com as movimentações no atendimento de caixa.
"""

class Dias(models.Model):
    dia = models.CharField(choices=DIAS, max_length=150)
    user = models.ForeignKey(User)

    history = HistoricalRecords()

    @property
    def _history_user(self):
        return self.user

    @_history_user.setter
    def _history_user(self, value):
        self.user = value

    def __unicode__(self):
        return self.dia

    class Meta:
        verbose_name_plural= 'Dias da Semana que a Clinica funciona'

class Escala(models.Model):
    """Classe para cadastro de escala de profissionais,servirá para agendamento de exames, consultas, etc."""
    professional = models.ForeignKey(Profissional)
    days_of_service = models.ManyToManyField(Dias)
    period = models.CharField(choices=PERIODO, max_length=150)
    user = models.ForeignKey(User)

    history = HistoricalRecords()

    @property
    def _history_user(self):
        return self.user

    @_history_user.setter
    def _history_user(self, value):
        self.user = value

    def __unicode__(self):
        return self.professional.__str__()

    class Meta:
        verbose_name_plural = 'Escala, classe para determinar os dias em que o profissional estará na clinica'

class Agenda_Odonto(models.Model):
    """Classe que registra o futuro atendimento para o usuário relacionado a determinado profissional 
    com sua especialidade."""
    client= models.ForeignKey(Contrato_Odontologico)
    day_of_service = models.ForeignKey(Escala)
    hour_to_service = models.TimeField()
    user = models.ForeignKey(User)

    history = HistoricalRecords()

    @property
    def _history_user(self):
        return self.user

    @_history_user.setter
    def _history_user(self, value):
        self.user = value

    def __unicode__(self):
        return self.client.__str__()

    class Meta:
        verbose_name_plural= 'Agenda para atendimentos odontológicos'


class Agenda_Psico(models.Model):
    """Classe que registra o futuro atendimento para o usuário relacionado a determinado profissional 
    com sua especialidade."""
    client = models.ForeignKey(Contrato_Psicologicos)
    day_of_service = models.ForeignKey(Escala)
    hour_to_service = models.TimeField()
    user = models.ForeignKey(User)

    history = HistoricalRecords()

    @property
    def _history_user(self):
        return self.user

    @_history_user.setter
    def _history_user(self, value):
        self.user = value

    def __unicode__(self):
        return self.client.__str__()

    class Meta:
        verbose_name_plural = 'Agenda para atendimentos Psicologicos'


class Agenda_Nutri(models.Model):
    """Classe que registra o futuro atendimento para o usuário relacionado a determinado profissional 
    com sua especialidade."""
    client = models.ForeignKey(Contrato_Nutricional)
    day_of_service = models.ForeignKey(Escala)
    hour_to_service = models.TimeField()
    user = models.ForeignKey(User)

    history = HistoricalRecords()

    @property
    def _history_user(self):
        return self.user

    @_history_user.setter
    def _history_user(self, value):
        self.user = value

    def __unicode__(self):
        return self.client.__str__()

    class Meta:
        verbose_name_plural = 'Agenda para atendimentos Nutricionais'

