# coding=utf-8
from __future__ import unicode_literals
from django.contrib.auth.models import *
from django.db import models
from simple_history.models import HistoricalRecords

'''Este módulo tem a finalidade de cadastros base da organização'''


TYPE_PROFESSIONAL = ((u'Dentista', 'Dentista'), (u'Nutricionista', 'Nutricionista'), (u'Psicologo', 'Psicologo'))

SEXO = ((u'Masculino','Masculino'),(u'Feminino','Feminino'))

FUNCTION = ((u'Gerente','Gerente'),(u'Zelador(a)','Zelador(a)'),
            (u'Atendente', 'Atendente'), (u'Vigia','Vigia'),
            (u'Seguranca', 'Seguranca'))
FREQUENCIA = ((u'Unica','Unica'),(u'Daria','Daria'),(u'Semanal','Semanal'),(u'Mensal','Mensal'),(u'Trimestral','Trimestral'),(u'Semestral','Semestral'),(u'Anual','Anual'))

class Profissional(models.Model):

    '''Cadastro de Profissional na clinica, os que atendem os clientes. Dentistas, Nutricionistas e Psicólogos'''

    name = models.CharField(max_length=150, unique = True )
    professional_as = models.CharField(max_length=150, choices=TYPE_PROFESSIONAL)
    cpf = models.CharField(max_length=11,unique=True)
    rg = models.CharField(max_length=30,unique=True)
    salary = models.FloatField(help_text='Em R$')
    sex = models.CharField(max_length=150, choices=SEXO)
    email = models.EmailField()
    phone = models.CharField(max_length=150, blank=True)
    watsapp = models.CharField(max_length=12, blank=True)
    register = models.CharField(max_length=150, help_text='Registro no conselho regional', unique=True)
    cep = models.CharField(max_length=9)
    birth_day = models.DateField()
    date_register_in_company = models.DateField(blank=True)
    note = models.TextField()
    active = models.BooleanField(blank=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.name

    history = HistoricalRecords()

    @property
    def _history_user(self):
        return self.user

    @_history_user.setter
    def _history_user(self, value):
        self.user = value

    class Meta:
        verbose_name_plural= 'Profissonal Cadastrado na Clínica'

class Funcionario(models.Model):

    '''Cadastro de Funcionário que faz a manutenção da clínica'''

    name = models.CharField(max_length=150,  unique = True)
    date_register_in_company = models.DateField()
    sex = models.CharField(max_length=150,choices=SEXO)
    function = models.CharField(max_length=150, choices = FUNCTION)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=11,blank=True)
    watsapp = models.CharField(max_length=12, blank=True)
    street = models.CharField(max_length=150)
    district = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    rg = models.CharField(max_length=25, unique= True)
    cpf = models.CharField(max_length=11, unique=True)
    cep = models.CharField(max_length=9)
    birth_day = models.DateField()
    note = models.TextField()
    salary = models.FloatField()
    active = models.BooleanField(blank=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.name

    history = HistoricalRecords()

    @property
    def _history_user(self):
        return self.user

    @_history_user.setter
    def _history_user(self, value):
        self.user = value

    class Meta:
        verbose_name_plural = 'Funcionários Cadastrados na Clínica'

class Cliente(models.Model):

    '''Cadastro de Clientes da base da clínica, este método serve de base para os contratos e para os contatos 
    sugeridos pelos clientes'''

    name = models.CharField(max_length=150, unique = True)
    sex = models.CharField(max_length=150,choices=SEXO)
    date_register = models.DateField(help_text='A data sugerida para pagamento mensal!')
    date_register_in_company = models.DateField(help_text='Data de registro na clínica')
    birth_day = models.DateField()
    profession = models.CharField(max_length=150)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=150, blank=True)
    watsapp = models.CharField(max_length=12, blank=True)
    street = models.CharField(max_length=150)
    district = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    cep = models.CharField(max_length=9)
    rg = models.CharField(max_length=25, unique= True)
    cpf = models.CharField(max_length=11, unique=True)
    Note = models.TextField(blank=True)
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
        return self.name

    class Meta:
        verbose_name_plural = 'Clientes Cadastrados na Clínica'

class Marca(models.Model):

    '''Cadastra a marca do produto que é usado'''

    name = models.CharField(max_length=150)
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
        return self.name

class Fornecedor(models.Model):

    '''Cadastra o fornecedor dos produtos que serão usados na clinica, para uso e venda e a marca que fornece.'''

    fantasy_name = models.CharField(max_length=150)
    cnpj = models.CharField(max_length=23, unique=True)
    state_register = models.CharField(max_length=150)
    mak_to_provides = models.ForeignKey(Marca)

    user = models.ForeignKey(User)

    history = HistoricalRecords()

    @property
    def _history_user(self):
        return self.user

    @_history_user.setter
    def _history_user(self, value):
        self.user = value

    def __unicode__(self):
        return self.fantasy_name

    class Meta:
        verbose_name_plural = 'Fornecedores de Produtos para a Clínica'

class Produto(models.Model):

    '''Cadastra o produto e o relaciona a uma marca já cadastrada'''

    name = models.CharField(max_length=150)
    active = models.BooleanField(blank=True)
    mark = models.ForeignKey(Marca)
    provider = models.ForeignKey(Fornecedor)

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
        verbose_name_plural= 'Produtos usados na Clínica'

class Contas_a_Pagar(models.Model):

    '''Cadastra as contas a pagar pela clínica, com sua frequencia e valor.'''

    name = models.CharField(max_length=150)
    periodic = models.BooleanField(blank=True)
    frequency = models.CharField(choices=FREQUENCIA, max_length=150)
    active = models.BooleanField(blank=True)
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
        verbose_name_plural = 'Contas a serem Pagas pela Clínica e suas periodicidade.'

class Contas_a_Pagar_Pagas(models.Model):
    """Cadastro de contas pagas."""
    conta= models.ForeignKey(Contas_a_Pagar)
    date_payment = models.DateField()
    responsible_for_payment = models.ForeignKey(Funcionario)
    Image_of_receipt =  models.ImageField(
        null=True,
        blank=True,
        upload_to='/imagem_contrato_odonto/',
    )
    user = models.ForeignKey(User)
    def __unicode__(self):
        return self.conta.__str__()

    history = HistoricalRecords()

    @property
    def _history_user(self):
        return self.user

    @_history_user.setter
    def _history_user(self, value):
        self.user = value

    class Meta:
        verbose_name_plural = "Contas a Pagar que foram pagas"