
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from app_base.apresentacao import *
from app_base.views import *
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
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
