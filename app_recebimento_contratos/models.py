# coding=utf-8
from __future__ import unicode_literals
from django.contrib.auth.models import *
from simple_history.models import HistoricalRecords
from django.db import models
from app_contrato.models import *

TYPE_PROFESSIONAL = ((u'Dentista', 'Dentista'), (u'Nutricionista', 'Nutricionista'), (u'Psicologo', 'Psicologo'))

class Recebe_Contrato_Odonto(models.Model):
    client = models.ForeignKey(Contrato_Odontologico)
    value_received_total = models.FloatField()
    value_received_in_Credit = models.FloatField(blank=True)
    value_received_in_Debit = models.FloatField(blank=True)
    value_received_in_Money = models.FloatField(blank=True)
    value_received_in_Ticket = models.FloatField(blank=True)
    value_received_in_Check = models.FloatField(blank=True)
    value_received_in_Promissory = models.FloatField(blank=True)
    remaining_value = models.FloatField(help_text='Valor que falta ser pago pelo mês de tratamento, caso haja.',
                                        blank=True)

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
        verbose_name_plural= 'Recebe dos contratos odontológicos'


class Recebe_Contrato_Nutri(models.Model):
    client = models.ForeignKey(Contrato_Nutricional)
    value_received_total = models.FloatField()
    value_received_in_Credit = models.FloatField(blank=True)
    value_received_in_Debit = models.FloatField(blank=True)
    value_received_in_Money = models.FloatField(blank=True)
    value_received_in_Ticket = models.FloatField(blank=True)
    value_received_in_Check = models.FloatField(blank=True)
    value_received_in_Promissory = models.FloatField(blank=True)
    remaining_value = models.FloatField(help_text='Valor que falta ser pago pelo mês de tratamento, caso haja.',
                                        blank=True)

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
        verbose_name_plural = 'Recebe dos contratos Nutricionais'


class Recebe_Contrato_Psico(models.Model):
    client = models.ForeignKey(Contrato_Psicologicos)
    value_received_total = models.FloatField()
    value_received_in_Credit = models.FloatField(blank=True)
    value_received_in_Debit = models.FloatField(blank=True)
    value_received_in_Money = models.FloatField(blank=True)
    value_received_in_Ticket = models.FloatField(blank=True)
    value_received_in_Check = models.FloatField(blank=True)
    value_received_in_Promissory = models.FloatField(blank=True)
    remaining_value = models.FloatField(help_text='Valor que falta ser pago pelo mês de tratamento, caso haja.', blank=True)

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
        verbose_name_plural = 'Recebe dos contratos psicológicos'

class Recebe_sem_contrato_odonto(models.Model):
    """Esta classe tem a finalidade de cadastrar o recebimento de clientes sem contrato firmado com a clinica.
    Por peculiaridade, possui campos como valor do serviço, o valor que ele pagou e como pagou."""
    client = models.ForeignKey(Cliente)
    serices = models.ManyToManyField(Servicos_Odonto)
    velue_attendance= models.FloatField()
    value_received_total = models.FloatField()
    value_received_in_Credit = models.FloatField(blank=True)
    value_received_in_Debit = models.FloatField(blank=True)
    value_received_in_Money = models.FloatField(blank=True)
    value_received_in_Ticket = models.FloatField(blank=True)
    value_received_in_Check = models.FloatField(blank=True)
    value_received_in_Promissory = models.FloatField(blank=True)
    remaining_value = models.FloatField(help_text='Valor que falta ser pago pelo serviço, caso haja.',blank=True)

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
        verbose_name_plural = 'Recebe os clientes sem contrato na clinica'


class Recebe_sem_contrato_Psicologico(models.Model):
    """Esta classe tem a finalidade de cadastrar o recebimento de clientes sem contrato firmado com a clinica.
    Por peculiaridade, possui campos como valor do serviço, o valor que ele pagou e como pagou."""
    client = models.ForeignKey(Cliente)
    serices = models.ManyToManyField(Servicos_Psicologicos)
    velue_attendance = models.FloatField()
    value_received_total = models.FloatField()
    value_received_in_Credit = models.FloatField(blank=True)
    value_received_in_Debit = models.FloatField(blank=True)
    value_received_in_Money = models.FloatField(blank=True)
    value_received_in_Ticket = models.FloatField(blank=True)
    value_received_in_Check = models.FloatField(blank=True)
    value_received_in_Promissory = models.FloatField(blank=True)
    remaining_value = models.FloatField(help_text='Valor que falta ser pago pelo serviço, caso haja.', blank=True)

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
        verbose_name_plural = 'Recebe os clientes sem contrato na clinica'


class Recebe_sem_contrato_nutri(models.Model):
    """Esta classe tem a finalidade de cadastrar o recebimento de clientes sem contrato firmado com a clinica.
    Por peculiaridade, possui campos como valor do serviço, o valor que ele pagou e como pagou."""
    client = models.ForeignKey(Cliente)
    serices = models.ManyToManyField(Servicos_Nutricional)
    velue_attendance = models.FloatField()
    value_received_total = models.FloatField()
    value_received_in_Credit = models.FloatField(blank=True)
    value_received_in_Debit = models.FloatField(blank=True)
    value_received_in_Money = models.FloatField(blank=True)
    value_received_in_Ticket = models.FloatField(blank=True)
    value_received_in_Check = models.FloatField(blank=True)
    value_received_in_Promissory = models.FloatField(blank=True)
    remaining_value = models.FloatField(help_text='Valor que falta ser pago pelo serviço, caso haja.', blank=True)

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
        verbose_name_plural = 'Recebe os clientes sem contrato na clinica'