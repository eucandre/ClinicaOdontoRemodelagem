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
    
    soma_fun = 0
    soma_prof = 0
    soma_produ = 0
    if len(obj_func)==0:
        obj_func_data = 0
    
    if len(obj_func)>0:  
        for i in range(len(obj_func)):  
            soma_fun = Funcionario.objects.get(pk=len(obj_func)).salary + Funcionario.objects.get(pk=len(obj_func)-1).salary
            obj_func_data = soma_fun

    if len(obj_prof)==0:
        obj_prof_data = 0

    if len(obj_prof)>0:  
        for i in range(len(obj_prof)):  
            soma_prof = Profissional.objects.get(pk=len(obj_prof)).salary + Profissional.objects.get(pk=len(obj_prof)-1).salary
            obj_prof_data = soma_prof
    
    if len(obj_clie) == 0:
        obj_clie_data = 0

    if len(obj_produ) > 0:
        soma_produ =  Produto.objects.get(pk=len(obj_clie)).salary + Produto.objects.get(pk=len(obj_clie)-1).salary
        obj_clie_data = soma_cli

    return render(request,'index.html',{'funcionario':len(obj_func), 'profissionais':len(obj_prof),
        'cliente':len(obj_clie), 'marcas':len(obj_marc),'fornecedor':len(obj_forn),'produto':len(obj_prod),
        'contas_a_pagar':len(obj_cnta),'contas_pagas':len(obj_cntp), 
        'valor_func':obj_func_data, 'valor_prof':obj_prof_data, })