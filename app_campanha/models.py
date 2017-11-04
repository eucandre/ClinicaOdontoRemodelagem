# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from app_contrato.models import *
from app_base.models import *

class Campanha_geral(models.Model):

    name = models.CharField(max_length=150)
    premium_first = models.CharField(max_length=150, blank=True)
    premium_secund = models.CharField(max_length=150, blank=True)
    premium_third = models.CharField(max_length=150, blank=True)
    premium_fourth = models.CharField(max_length=150, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Cadastos de campanhas para a clinica'

class Campanha_odonto(models.Model):

    contract = models.ForeignKey(Contrato_Odontologico)
    date_to_sign_to_campain = models.DateField()
    employee = models.ForeignKey(Funcionario)
    value_contract =models.FloatField()
    campaign = models.ForeignKey(Campanha_geral)

    def __unicode__(self):
        return self.employee.__str__()

    class Meta:
        verbose_name_plural = 'Cadastra Campanha de vendas de odonto na clínica'


class Campanha_psico(models.Model):
    contract = models.ForeignKey(Contrato_Psicologicos)
    date_to_sign_to_campain = models.DateField()
    employee = models.ForeignKey(Funcionario)
    value_contract = models.FloatField()
    campaign = models.ForeignKey(Campanha_geral)

    def __unicode__(self):
        return self.employee.__str__()

    class Meta:
        verbose_name_plural = 'Cadastra Campanha de vendas de psico na clínica'


class Campanha_nutri(models.Model):
    contract = models.ForeignKey(Contrato_Nutricional)
    date_to_sign_to_campain = models.DateField()
    employee = models.ForeignKey(Funcionario)
    value_contract = models.FloatField()
    campaign = models.ForeignKey(Campanha_geral)

    def __unicode__(self):
        return self.employee.__str__()

    class Meta:
        verbose_name_plural = 'Cadastra Campanha de vendas de nutri na clínica'


