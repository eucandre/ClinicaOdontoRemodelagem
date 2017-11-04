# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from app_orcamento.models import *
from django.contrib.auth.models import *
from simple_history.models import HistoricalRecords

"""
    A geração de doc para os documentos de contratos e de promissórias, recibos, etc, serão do módudo python-docx.
"""


class Responsavel(models.Model):
    """Cadastro de um responsável para um possível contrato que necessite.
    Caso seja um convênio com uma empresa usar esta classe para referenciar.
    O campo cpf será cadastrado quando for pessoa física, o campo cnpj será usado 
    quando for pessoa jurídica e configurar um convênio."""
    responsible = models.CharField(max_length=150)
    cpf = models.CharField(max_length=11, blank=True)
    cnpj = models.CharField(max_length=22, blank=True)
    rg = models.CharField(max_length=30, blank=True)
    rua = models.CharField(max_length=150)
    bairro = models.CharField(max_length=150)
    cidade = models.CharField(max_length=150)
    celular = models.CharField(max_length=11)
    watsapp = models.CharField(max_length=11)

    user = models.ForeignKey(User)

    history = HistoricalRecords()

    @property
    def _history_user(self):
        return self.user

    @_history_user.setter
    def _history_user(self, value):
        self.user = value

    def __unicode__(self):
        return self.responsible

    class Meta:
        verbose_name_plural = 'Responsável por clientes cadastrados na clínica'

class Contrato_Odontologico(models.Model):
    '''Cadastro de contrato odonto, nome do cliente, o resposnsácvel cado precise, data de assinatura e o valor do contrato.'''
    client_orcament = models.ForeignKey(Orcamento_Odonto)
    date_sign = models.DateField(auto_now=True)
    contract_value = models.FloatField()
    contract_duration = models.DateField(help_text='Data possível para finalizar o contrato.')
    responsible = models.ForeignKey(Responsavel)

    user = models.ForeignKey(User)

    history = HistoricalRecords()

    @property
    def _history_user(self):
        return self.user

    @_history_user.setter
    def _history_user(self, value):
        self.user = value

    def __unicode__(self):
        return self.client_orcament.__str__()

    class Meta:
        verbose_name_plural = 'Contratos odontológicos cadastrados na clínica'


class Contrato_Nutricional(models.Model):
    '''Cadastro de contrato odonto, nome do cliente, o resposnsácvel cado precise, data de assinatura e o valor do contrato.'''
    client_orcament = models.ForeignKey(Orcamento_Nutri)
    date_sign = models.DateField(auto_now=True)
    contract_value = models.FloatField()
    contract_duration = models.DateField(help_text='Data possível para finalizar o contrato.')
    responsible = models.ForeignKey(Responsavel)

    user = models.ForeignKey(User)

    history = HistoricalRecords()

    @property
    def _history_user(self):
        return self.user

    @_history_user.setter
    def _history_user(self, value):
        self.user = value

    def __unicode__(self):
        return self.client_orcament.__str__()

    class Meta:
        verbose_name_plural = 'Contratos nutricionais cadastrados na clínica'

class Contrato_Psicologicos(models.Model):
    '''Cadastro de contrato odonto, nome do cliente, o resposnsácvel cado precise, data de assinatura e o valor do contrato.'''
    client_orcament = models.ForeignKey(Orcamento_Psico)
    date_sign = models.DateField(auto_now=True)
    contract_value = models.FloatField()
    contract_duration = models.DateField(help_text='Data possível para finalizar o contrato.')
    responsible = models.ForeignKey(Responsavel)

    user = models.ForeignKey(User)

    history = HistoricalRecords()

    @property
    def _history_user(self):
        return self.user

    @_history_user.setter
    def _history_user(self, value):
        self.user = value

    def __unicode__(self):
        return self.client_orcament.__str__()

    class Meta:
        verbose_name_plural = 'Contratos psicológicos cadastrados na clínica'

