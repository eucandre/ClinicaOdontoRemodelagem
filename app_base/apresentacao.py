# coding=utf-8
from django.shortcuts import render
from app_base.models import *
from app_base.forms import *

"""
    Módulo destinado à criação de dashboards para a tela inicial.
"""


def apresenta(request):
    """Este método irá carregar todas as tabelas do banco para mostrar no dashboard."""

    # -- Variáveis da app_base--#
    obj_func = Funcionario.objects.all()
    obj_prof = Profissional.objects.all()
    obj_clie = Cliente.objects.all()
    obj_marc = Marca.objects.all()
    obj_forn = Fornecedor.objects.all()
    obj_prod = Produto.objects.all()
    obj_cnta = Contas_a_Pagar.objects.all()
    obj_cntp = Contas_a_Pagar_Pagas.objects.all()

    soma_fun = 0
    soma_prof = 0
    soma_produ = 0
    soma_conta_paga = 0

    soma_conta_paga_jan = 0
    soma_conta_paga_fev = 0
    soma_conta_paga_mar = 0
    soma_conta_paga_abr = 0
    soma_conta_paga_mai = 0
    soma_conta_paga_jun = 0
    soma_conta_paga_jul = 0
    soma_conta_paga_ago = 0
    soma_conta_paga_set = 0
    soma_conta_paga_out = 0
    soma_conta_paga_nov = 0
    soma_conta_paga_dez = 0

    soma_conta_pagar = 0
    soma_conta_pagar_jan = 0
    soma_conta_pagar_fev = 0
    soma_conta_pagar_mar = 0
    soma_conta_pagar_abr = 0
    soma_conta_pagar_mai = 0
    soma_conta_pagar_jun = 0
    soma_conta_pagar_jul = 0
    soma_conta_pagar_ago = 0
    soma_conta_pagar_set = 0
    soma_conta_pagar_out = 0
    soma_conta_pagar_nov = 0
    soma_conta_pagar_dez = 0

    if len(obj_cntp) == 0:
        soma_conta_paga = 0

    elif len(obj_cntp) == 1:
        if Contas_a_Pagar_Pagas.objects.get(pk=1).date_payment.month == 1:
            soma_conta_paga_jan = Contas_a_Pagar_Pagas.objects.get(pk=1).conta.value + soma_conta_paga_jan
            soma_conta_paga = soma_conta_paga_jan

        if Contas_a_Pagar_Pagas.objects.get(pk=1).date_payment.month == 2:
            soma_conta_paga_fev = Contas_a_Pagar_Pagas.objects.get(pk=1).conta.value + soma_conta_paga_fev
            soma_conta_paga = soma_conta_paga_fev

        if Contas_a_Pagar_Pagas.objects.get(pk=1).date_payment.month == 3:
            soma_conta_paga_mar = Contas_a_Pagar_Pagas.objects.get(pk=1).conta.value + soma_conta_paga_mar
            soma_conta_paga = soma_conta_paga_mar
        if Contas_a_Pagar_Pagas.objects.get(pk=1).date_payment.month == 4:
            soma_conta_paga_abr = Contas_a_Pagar_Pagas.objects.get(pk=1).conta.value + soma_conta_paga_abr
            soma_conta_paga = soma_conta_paga_abr
        if Contas_a_Pagar_Pagas.objects.get(pk=1).date_payment.month == 5:
            soma_conta_paga_mai = Contas_a_Pagar_Pagas.objects.get(pk=1).conta.value + soma_conta_paga_mai
            soma_conta_paga = soma_conta_paga_mai

        if Contas_a_Pagar_Pagas.objects.get(pk=1).date_payment.month == 6:
            soma_conta_paga_jun = Contas_a_Pagar_Pagas.objects.get(pk=1).conta.value + soma_conta_paga_jun
            soma_conta_paga = soma_conta_paga_jun

        if Contas_a_Pagar_Pagas.objects.get(pk=1).date_payment.month == 7:
            soma_conta_paga_jul = Contas_a_Pagar_Pagas.objects.get(pk=1).conta.value + soma_conta_paga_jul
            soma_conta_paga = soma_conta_paga_jul

        if Contas_a_Pagar_Pagas.objects.get(pk=1).date_payment.month == 8:
            soma_conta_paga_ago = Contas_a_Pagar_Pagas.objects.get(pk=1).conta.value + soma_conta_paga_ago
            soma_conta_paga = soma_conta_paga_ago

        if Contas_a_Pagar_Pagas.objects.get(pk=1).date_payment.month == 9:
            soma_conta_paga_set = Contas_a_Pagar_Pagas.objects.get(pk=1).conta.value + soma_conta_paga_set
            soma_conta_paga = soma_conta_paga_set

        if Contas_a_Pagar_Pagas.objects.get(pk=1).date_payment.month == 10:
            soma_conta_paga_out = Contas_a_Pagar_Pagas.objects.get(pk=1).conta.value + soma_conta_paga_out
            soma_conta_paga = soma_conta_paga_out

        if Contas_a_Pagar_Pagas.objects.get(pk=1).date_payment.month == 11:
            soma_conta_paga_nov = Contas_a_Pagar_Pagas.objects.get(pk=1).conta.value + soma_conta_paga_nov
            soma_conta_paga = soma_conta_paga_nov

        if Contas_a_Pagar_Pagas.objects.get(pk=1).date_payment.month == 12:
            soma_conta_paga_dez = Contas_a_Pagar_Pagas.objects.get(pk=1).conta.value + soma_conta_paga_dez
            soma_conta_paga = soma_conta_paga_dez

    elif len(obj_cntp) > 1:
        for i in range(1,len(obj_cntp)):
            if Contas_a_Pagar_Pagas.objects.get(pk=i).date_payment.month == 1:
                soma_conta_paga_jan = Contas_a_Pagar_Pagas.objects.get(pk=i).conta.value + soma_conta_paga_jan
                soma_conta_paga = soma_conta_paga_jan

            if Contas_a_Pagar_Pagas.objects.get(pk=i).date_payment.month == 2:
                soma_conta_paga_fev = Contas_a_Pagar_Pagas.objects.get(pk=i).conta.value + soma_conta_paga_fev
                soma_conta_paga = soma_conta_paga_fev

            if Contas_a_Pagar_Pagas.objects.get(pk=i).date_payment.month == 3:
                soma_conta_paga_mar = Contas_a_Pagar_Pagas.objects.get(pk=i).conta.value + soma_conta_paga_mar
                soma_conta_paga = soma_conta_paga_mar
            if Contas_a_Pagar_Pagas.objects.get(pk=i).date_payment.month == 4:
                soma_conta_paga_abr = Contas_a_Pagar_Pagas.objects.get(pk=i).conta.value + soma_conta_paga_abr
                soma_conta_paga = soma_conta_paga_abr
            if Contas_a_Pagar_Pagas.objects.get(pk=i).date_payment.month == 5:
                soma_conta_paga_mai = Contas_a_Pagar_Pagas.objects.get(pk=i).conta.value + soma_conta_paga_mai
                soma_conta_paga = soma_conta_paga_mai

            if Contas_a_Pagar_Pagas.objects.get(pk=i).date_payment.month == 6:
                soma_conta_paga_jun = Contas_a_Pagar_Pagas.objects.get(pk=i).conta.value + soma_conta_paga_jun
                soma_conta_paga = soma_conta_paga_jun

            if Contas_a_Pagar_Pagas.objects.get(pk=i).date_payment.month == 7:
                soma_conta_paga_jul = Contas_a_Pagar_Pagas.objects.get(pk=i).conta.value + soma_conta_paga_jul
                soma_conta_paga = soma_conta_paga_jul

            if Contas_a_Pagar_Pagas.objects.get(pk=i).date_payment.month == 8:
                soma_conta_paga_ago = Contas_a_Pagar_Pagas.objects.get(pk=i).conta.value + soma_conta_paga_ago
                soma_conta_paga = soma_conta_paga_ago

            if Contas_a_Pagar_Pagas.objects.get(pk=i).date_payment.month == 9:
                soma_conta_paga_set = Contas_a_Pagar_Pagas.objects.get(pk=i).conta.value + soma_conta_paga_set
                soma_conta_paga = soma_conta_paga_set

            if Contas_a_Pagar_Pagas.objects.get(pk=i).date_payment.month == 10:
                soma_conta_paga_out = Contas_a_Pagar_Pagas.objects.get(pk=i).conta.value + soma_conta_paga_out
                soma_conta_paga = soma_conta_paga_out

            if Contas_a_Pagar_Pagas.objects.get(pk=i).date_payment.month == 11:
                soma_conta_paga_nov = Contas_a_Pagar_Pagas.objects.get(pk=i).conta.value + soma_conta_paga_nov
                soma_conta_paga = soma_conta_paga_nov

            if Contas_a_Pagar_Pagas.objects.get(pk=i).date_payment.month == 12:
                soma_conta_paga_dez = Contas_a_Pagar_Pagas.objects.get(pk=i).conta.value + soma_conta_paga_dez
                soma_conta_paga = soma_conta_paga_dez

    if len(obj_cnta) == 0:
        soma_conta_pagar = 0
    elif len(obj_cnta) == 1:
        if Contas_a_Pagar_Pagas.objects.get(pk=1).date_payment.month == 1:
            soma_conta_pagar_jan = Contas_a_Pagar_Pagas.objects.get(pk=1).conta.value + soma_conta_pagar_jan
            soma_conta_pagar = soma_conta_pagar_jan

        if Contas_a_Pagar_Pagas.objects.get(pk=1).date_payment.month == 2:
            soma_conta_pagar_fev = Contas_a_Pagar_Pagas.objects.get(pk=1).conta.value + soma_conta_pagar_fev
            soma_conta_pagar = soma_conta_pagar_fev

        if Contas_a_Pagar_Pagas.objects.get(pk=1).date_payment.month == 3:
            soma_conta_pagar_mar = Contas_a_Pagar_Pagas.objects.get(pk=1).conta.value + soma_conta_pagar_mar
            soma_conta_pagar = soma_conta_pagar_mar
        if Contas_a_Pagar_Pagas.objects.get(pk=1).date_payment.month == 4:
            soma_conta_pagar_abr = Contas_a_Pagar_Pagas.objects.get(pk=1).conta.value + soma_conta_pagar_abr
            soma_conta_pagar = soma_conta_pagar_abr
        if Contas_a_Pagar_Pagas.objects.get(pk=1).date_payment.month == 5:
            soma_conta_pagar_mai = Contas_a_Pagar_Pagas.objects.get(pk=1).conta.value + soma_conta_pagar_mai
            soma_conta_pagar = soma_conta_pagar_mai

        if Contas_a_Pagar_Pagas.objects.get(pk=1).date_payment.month == 6:
            soma_conta_pagar_jun = Contas_a_Pagar_Pagas.objects.get(pk=1).conta.value + soma_conta_pagar_jun
            soma_conta_pagar = soma_conta_pagar_jun

        if Contas_a_Pagar_Pagas.objects.get(pk=1).date_payment.month == 7:
            soma_conta_pagar_jul = Contas_a_Pagar_Pagas.objects.get(pk=1).conta.value + soma_conta_pagar_jul
            soma_conta_pagar = soma_conta_pagar_jul

        if Contas_a_Pagar_Pagas.objects.get(pk=1).date_payment.month == 8:
            soma_conta_pagar_ago = Contas_a_Pagar_Pagas.objects.get(pk=1).conta.value + soma_conta_pagar_ago
            soma_conta_pagar = soma_conta_pagar_ago

        if Contas_a_Pagar_Pagas.objects.get(pk=1).date_payment.month == 9:
            soma_conta_pagar_set = Contas_a_Pagar_Pagas.objects.get(pk=1).conta.value + soma_conta_pagar_set
            soma_conta_pagar = soma_conta_pagar_set

        if Contas_a_Pagar_Pagas.objects.get(pk=1).date_payment.month == 10:
            soma_conta_pagar_out = Contas_a_Pagar_Pagas.objects.get(pk=1).conta.value + soma_conta_pagar_out
            soma_conta_pagar = soma_conta_pagar_out

        if Contas_a_Pagar_Pagas.objects.get(pk=1).date_payment.month == 11:
            soma_conta_pagar_nov = Contas_a_Pagar_Pagas.objects.get(pk=1).conta.value + soma_conta_pagar_nov
            soma_conta_pagar = soma_conta_pagar_nov

        if Contas_a_Pagar_Pagas.objects.get(pk=1).date_payment.month == 12:
            soma_conta_pagar_dez = Contas_a_Pagar_Pagas.objects.get(pk=1).conta.value + soma_conta_pagar_dez
            soma_conta_pagar = soma_conta_paga_dez

    return render(request,'index.html',{'conta_paga_jan': soma_conta_paga_jan,
                                        'conta_paga_fev': soma_conta_paga_fev,'conta_paga_mar': soma_conta_paga_mar,
                                        'conta_paga_abr': soma_conta_paga_abr,'conta_paga_mai': soma_conta_paga_mai,
                                        'conta_paga_jun': soma_conta_paga_jun,'conta_paga_jul': soma_conta_paga_jul,
                                        'conta_paga_ago': soma_conta_paga_ago,'conta_paga_set': soma_conta_paga_set,
                                        'conta_paga_out': soma_conta_paga_out,'conta_paga_nov': soma_conta_paga_nov,
                                        'conta_paga_dez': soma_conta_paga_dez,  ####
                                        'conta_pagar_jan': soma_conta_pagar_jan,'conta_pagar_fev': soma_conta_pagar_fev,
                                        'conta_pagar_mar': soma_conta_pagar_mar,'conta_pagar_abr': soma_conta_pagar_abr,
                                        'conta_pagar_mai': soma_conta_pagar_mai,'conta_pagar_jun': soma_conta_pagar_jun,
                                        'conta_pagar_jul': soma_conta_pagar_jul,'conta_pagar_ago': soma_conta_pagar_ago,
                                        'conta_pagar_set': soma_conta_pagar_set,'conta_pagar_out': soma_conta_pagar_out,
                                        'conta_pagar_nov': soma_conta_pagar_nov,
                                        'conta_pagar_dez': soma_conta_pagar_dez,
                                        'funcionarios':len(obj_func), 'profissionais':len(obj_prof), 'clientes':len(obj_clie),
                                        'marcas':len(obj_marc),'fornecedores':len(obj_forn),'produtos':len(obj_prod)
                                        #### toda as tabelas da base estao nas variaveis a cima#
                                          })
