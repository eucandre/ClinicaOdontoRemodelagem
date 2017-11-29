# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from app_base.models import *
from app_servicos.models import *
from django.contrib.auth.models import *
from simple_history.models import HistoricalRecords


class Dente(models.Model):
    number_tooth = models.IntegerField()
    user = models.ForeignKey(User)

    history = HistoricalRecords()

    @property
    def _history_user(self):
        return self.user

    @_history_user.setter
    def _history_user(self, value):
        self.user = value

    def __unicode__(self):
        return self.number_tooth.__str__()

    class Meta:
        verbose_name_plural = 'Dentes e seus numerações'

class Orcamento_Odonto(models.Model):
    '''Cadastro de orçamento para contratos de odonto, conta com o nome do cliente
    os serviços que devem ser prestados, o valor do orçamento, os dentes para o tratamento
    e na anotação sugiro que detalhe as faces do dente e como se dará o tratamento.'''
    client_odonto = models.ForeignKey(Cliente)
    service_odonto = models.ManyToManyField(Servicos_Odonto)
    value_orcament = models.FloatField()
    tooth = models.ManyToManyField(Dente)
    note = models.TextField()
    active = models.BooleanField(blank=True)

    user = models.ForeignKey(User)

    history = HistoricalRecords()

    @property
    def _history_user(self):
        return self.user

    @_history_user.setter
    def _history_user(self, value):
        self.user = value

    def __unicode__(self):
        return self.client_odonto.__str__()

    class Meta:
        verbose_name_plural = 'Orçamento Odontológico da clínica'

class Orcamento_Psico(models.Model):
    '''Cadastro de orçamento para serviços psicológicos, conta com cliente vindo de uma chaave estrangeira, valor do orçamento e o
     profissional'''
    client_psico = models.ForeignKey(Cliente)
    service_psico = models.ManyToManyField(Servicos_Psicologicos)
    value_orcament = models.FloatField()
    note = models.TextField()
    active = models.BooleanField(blank=True)

    user = models.ForeignKey(User)

    history = HistoricalRecords()

    @property
    def _history_user(self):
        return self.user

    @_history_user.setter
    def _history_user(self, value):
        self.user = value

    def __unicode__(self):
        return self.client_psico.__str__()

    class Meta:
        verbose_name_plural = 'Orçamento Psicológico da clínica'

class Orcamento_Nutri(models.Model):
    '''Cadastro de orçamento para serviços Nutri, conta com cliente vindo de uma chaave estrangeira, valor do orçamento e o
         profissional'''
    client_nutri = models.ForeignKey(Cliente)
    service_nutri = models.ManyToManyField(Servicos_Nutricional)
    value_orcament = models.FloatField()
    note = models.TextField()
    active = models.BooleanField(blank=True)

    user = models.ForeignKey(User)

    history = HistoricalRecords()

    @property
    def _history_user(self):
        return self.user

    @_history_user.setter
    def _history_user(self, value):
        self.user = value

    def __unicode__(self):
        return self.client_nutri.__str__()

    class Meta:
        verbose_name_plural = 'Orçamento Nutricional da clínica'