
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from app_base.apresentacao import *
from app_base.views import *
from app_atendimento.views import *
from app_atendimento.apresentacao import *
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', apresenta),
    url(r'^Cadastra_profissional/', InsereProfissional),
    url(r'^Cadastra_funcionario/', InsereFuncionario),
    url(r'^Cadastra_cliente/', InsereCliente),
    url(r'^Cadastra_marca/', InsereMarca),
    url(r'^Cadastra_fornecedor/', InsereFornecedor),
    url(r'^Cadastra_produto/', InsereProduto),
    url(r'^Cadastra_contas_a_pagar/', InsereContasAPagar),
    url(r'^Cadastra_contas_a_pagar_pagas/', InsereContasAPagarPagas),
    #------------ urls da app_base a cima ----------------#
    url(r'^dashboard2/',apresenta_atendimento),
    url(r'^dashboard3/',apresenta_atendimento_Nutri),
    url(r'^dashboard4/',apresenta_atendimento_Psico),
    url(r'^Cadastra_dias/',InsereDias),
    url(r'^Cadastra_escala/',InsereEscala),
    url(r'^Cadastra_agenda_odonto/',InsereAgendaOdonto),
    url(r'^Cadastra_agenda_nutri/',InsereAgendaNutri),
    url(r'^Cadastra_agenda_psico/',InsereAgendaPsico),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
