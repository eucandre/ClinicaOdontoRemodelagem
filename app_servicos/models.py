# coding=utf-8
from __future__ import unicode_literals
from django.contrib.auth.models import *
from simple_history.models import HistoricalRecords
from django.db import models
from app_base.models import *

class Servicos_Odonto(models.Model):
    '''Cadastra o serviço prestado, o especialista(s), o valor e a duração da aplicação do serviço.'''
    name = models.CharField(max_length=150)
    professional_specialist = models.ManyToManyField(Profissional)
    average_time_to_apply = models.CharField(max_length=150)
    value = models.FloatField()

    user = models.ForeignKey(User)

    history = HistoricalRecords()

    @property
    def _history_user(self):
        return self.user

    @_history_user.setter
    def _history_user(self, value):
        self.user = value

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Serviços prestado para Odontologia na Clínica'

class Servicos_Nutricional(models.Model):
    '''Cadastra o serviço prestado, o especialista(s), o valor e a duração da aplicação do serviço.'''
    name = models.CharField(max_length=150)
    professional_specialist = models.ManyToManyField(Profissional)
    average_time_to_apply = models.CharField(max_length=150)
    value = models.FloatField()

    user = models.ForeignKey(User)

    history = HistoricalRecords()

    @property
    def _history_user(self):
        return self.user

    @_history_user.setter
    def _history_user(self, value):
        self.user = value

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Serviços prestado para Nutricional na Clínica'

class Servicos_Psicologicos(models.Model):
    '''Cadastra o serviço prestado, o especialista(s), o valor e a duração da aplicação do serviço.'''
    name = models.CharField(max_length=150)
    professional_specialist = models.ManyToManyField(Profissional)
    average_time_to_apply = models.CharField(max_length=150)
    value = models.FloatField()

    user = models.ForeignKey(User)

    history = HistoricalRecords()

    @property
    def _history_user(self):
        return self.user

    @_history_user.setter
    def _history_user(self, value):
        self.user = value

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Serviços prestado para Psicologia na Clínica'
