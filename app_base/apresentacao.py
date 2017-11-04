# coding=utf-8
from django.shortcuts import render
from app_base.models import *
from app_base.forms import *
"""
    Módulo destinado à criação de dashboards para a tela inicial.
"""

def apresenta(request):

    """Este método irá carregar todas as tabelas do banco para mostrar no dashboard."""

    #-- Variáveis da app_base--#
    obj_func= Funcionario.objects.all()
    obj_prof= Profissional.objects.all()
    obj_clie= Cliente.objects.all()
    obj_marc= Marca.objects.all()
    obj_forn= Fornecedor.objects.all()
    obj_prod= Produto.objects.all()
    obj_cnta= Contas_a_Pagar.objects.all()
    obj_cntp= Contas_a_Pagar_Pagas.objects.all()

    return render(request,'index.html')