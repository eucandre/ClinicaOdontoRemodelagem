# coding=utf-8
from django import forms
from .models import *

TYPE_PROFESSIONAL = ((u'Dentista', 'Dentista'), (u'Nutricionista', 'Nutricionista'), (u'Psicologo', 'Psicologo'))

SEXO = ((u'Masculino', 'Masculino'), (u'Feminino', 'Feminino'))

FUNCTION = ((u'Gerente', 'Gerente'), (u'Zelador(a)', 'Zelador(a)'),
            (u'Atendente', 'Atendente'), (u'Vigia', 'Vigia'),
            (u'Seguranca', 'Seguranca'))
FREQUENCIA = (
(u'Unica', 'Unica'), (u'Daria', 'Daria'), (u'Semanal', 'Semanal'), (u'Mensal', 'Mensal'), (u'Trimestral', 'Trimestral'),
(u'Semestral', 'Semestral'), (u'Anual', 'Anual'))


class FormProfissional(forms.ModelForm):
    name = forms.CharField(label='Nome', max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    professional_as = forms.ChoiceField(label='Tipo de Profissional', choices=TYPE_PROFESSIONAL,
                                        widget=forms.Select(attrs={'class': 'form-control'}))
    cpf = forms.CharField(label='CPF', max_length=11, widget=forms.TextInput(attrs={'class': 'form-control'}))
    rg = forms.CharField(label='Registro Geral(RG)', max_length=30,
                         widget=forms.TextInput(attrs={'class': 'form-control'}))
    salary = forms.FloatField(label='Salário', help_text='Em R$',
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label='Sexo', choices=SEXO, widget=forms.Select(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='e-Mail', widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label='Telefone', max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    watsapp = forms.CharField(label='Watsapp', max_length=12, widget=forms.TextInput(attrs={'class': 'form-control'}))
    register = forms.CharField(label='Registro', max_length=150, help_text='Conselho regional',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    cep = forms.CharField(label='CEP', max_length=9, help_text='Registro no conselho regional',
                          widget=forms.TextInput(attrs={'class': 'form-control'}))
    birth_day = forms.DateField(label='Aniversário',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'Type': 'Date'}))
    date_register_in_company = forms.DateField(label='Data de Registro na clínica',
                                               widget=forms.TextInput(attrs={'class': 'form-control', 'Type': 'Date'}))
    note = forms.CharField(label='Observação', widget=forms.Textarea(attrs={'class': 'form-control'}))
    active = forms.BooleanField(label='Ativo Na Clínica(?)')

    class Meta:
        model = Profissional
        fields = (
        'name', 'professional_as', 'cpf', 'rg', 'salary', 'sex', 'email', 'phone', 'watsapp', 'register', 'cep',
        'birth_day', 'date_register_in_company',
        'note', 'active')


class FormFuncionario(forms.ModelForm):
    name = forms.CharField(label='Nome', max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    function = forms.ChoiceField(label='Função desempenhada', choices=FUNCTION,
                                 widget=forms.Select(attrs={'class': 'form-control'}))
    cpf = forms.CharField(label='CPF', max_length=11, widget=forms.TextInput(attrs={'class': 'form-control'}))
    rg = forms.CharField(label='Registro Geral(RG)', max_length=30,
                         widget=forms.TextInput(attrs={'class': 'form-control'}))
    salary = forms.FloatField(label='Salário', help_text='Em R$',
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label='Sexo', choices=SEXO, widget=forms.Select(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='e-Mail', widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label='Telefone', max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    watsapp = forms.CharField(label='Watsapp', max_length=12, widget=forms.TextInput(attrs={'class': 'form-control'}))

    street = forms.CharField(label='Rua', max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    district = forms.CharField(label='Bairro', max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.CharField(label='Cidade', max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))

    cep = forms.CharField(label='CEP', max_length=9, widget=forms.TextInput(attrs={'class': 'form-control'}))
    birth_day = forms.DateField(label='Aniversário',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'Type': 'Date'}))
    date_register_in_company = forms.DateField(label='Data de Registro na clínica',
                                               widget=forms.TextInput(attrs={'class': 'form-control', 'Type': 'Date'}))
    note = forms.CharField(label='Observação', widget=forms.Textarea(attrs={'class': 'form-control'}))
    active = forms.BooleanField(label='Ativo Na Clínica(?)')

    class Meta:
        model = Funcionario
        fields = ('name', 'function', 'cpf', 'rg', 'salary', 'sex', 'email', 'phone', 'watsapp', 'street',
                  'district', 'city', 'cep', 'birth_day', 'date_register_in_company', 'note', 'active')


class FormCliente(forms.ModelForm):
    name = forms.CharField(label='Nome', max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label='Sexo', choices=SEXO, widget=forms.Select(attrs={'class': 'form-control'}))
    date_register_in_company = forms.DateField(label='Data de Registro na clínica',
                                               widget=forms.TextInput(attrs={'class': 'form-control', 'Type': 'Date'}))
    date_register = forms.DateField(label='Data de Para pagamento',
                                    widget=forms.TextInput(attrs={'class': 'form-control', 'Type': 'Date'}))
    birth_day = forms.DateField(label='Aniversário',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'Type': 'Date'}))
    profession = forms.CharField(label='Profissão', max_length=150,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='e-Mail', widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label='Telefone', max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    watsapp = forms.CharField(label='Watsapp', max_length=12, widget=forms.TextInput(attrs={'class': 'form-control'}))
    street = forms.CharField(label='Rua', max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    district = forms.CharField(label='Bairro', max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.CharField(label='Cidade', max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cep = forms.CharField(label='CEP', max_length=9, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cpf = forms.CharField(label='CPF', max_length=11, widget=forms.TextInput(attrs={'class': 'form-control'}))
    rg = forms.CharField(label='Registro Geral(RG)', max_length=30,
                         widget=forms.TextInput(attrs={'class': 'form-control'}))
    Note = forms.CharField(label='Observação', widget=forms.Textarea(attrs={'class': 'form-control'}))
    active = forms.BooleanField(label='Ativo Na Clínica(?)')

    class Meta:
        model = Cliente
        fields = (
        'name', 'sex', 'date_register', 'date_register_in_company', 'birth_day', 'profession', 'email', 'phone',
        'watsapp',
        'street', 'district', 'city', 'cep', 'rg', 'cpf', 'Note', 'active')


class FormMarca(forms.ModelForm):
    name = forms.CharField(label='Nome', max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    active = forms.BooleanField(label='Ativo Na Clínica(?)')

    class Meta:
        model = Marca
        fields = ('name', 'active')


class FormFornecedor(forms.ModelForm):

    name = forms.CharField(label='Nome', max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fantasy_name = forms.CharField(label='Nome Fantasia', max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cnpj = forms.CharField(label='CNPJ', max_length=22, widget=forms.TextInput(attrs={'class': 'form-control'}))
    state_register = forms.CharField(label='Inscrição Estadual', max_length=22, widget=forms.TextInput(attrs={'class': 'form-control'}))
    mak_to_provides = forms.ModelChoiceField(label='Marca',queryset=Marca.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Fornecedor
        fields = ('name', 'fantasy_name', 'cnpj', 'mak_to_provides', 'state_register')

class FormProduto(forms.ModelForm):
    name = forms.CharField(label='Nome', max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    mak_to_provides = forms.ModelChoiceField(label='Marca', queryset=Marca.objects.all(),
                                             widget=forms.Select(attrs={'class': 'form-control'}))
    provider = forms.ModelChoiceField(label='Fornecedor', queryset=Fornecedor.objects.all(),
                                             widget=forms.Select(attrs={'class': 'form-control'}))
    active = forms.BooleanField(label='Ativo Na Clínica(?)')
    class Meta:
        model = Produto
        fields= ('name','mark','provider','active')

class FormContaAPagar(forms.ModelForm):
    name = forms.CharField(label='Nome', max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    periodic = forms.BooleanField(label='É periódico(?)')
    value= forms.CharField(label='Valor da conta', max_length=22, widget=forms.TextInput(attrs={'class': 'form-control'}))
    active = forms.BooleanField(label='Ativo Na Clínica(?)')
    class Meta:
        model = Contas_a_Pagar
        fields= ('name','periodic','frequency','active','value')

class FormContasApagarPagas(forms.ModelForm):

    conta = forms.ModelChoiceField(label='Conta a ser Paga', queryset=Contas_a_Pagar.objects.all(),widget=forms.Select(attrs={'class': 'form-control'}))
    date_payment = forms.DateField(label='Data de Para pagamento',
                                    widget=forms.TextInput(attrs={'class': 'form-control', 'Type': 'Date'}))
    responsible_for_payment = forms.ModelChoiceField(label='Responsável pelo recebimento',queryset=Funcionario.objects.all(),widget=forms.Select(attrs={'class': 'form-control'}))
    Image_of_receipt = forms.ImageField()
    class Meta:
        model= Contas_a_Pagar_Pagas
        fields=('conta','date_payment','responsible_for_payment','Image_of_receipt')