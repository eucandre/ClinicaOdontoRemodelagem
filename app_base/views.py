from django.shortcuts import render
from .forms import *

def InsereProfissional(request):
    if request.method=='POST':
        form = FormProfissional(request.POST)
        if form.is_valid():
            item= form.save(commit=False)
            item.user= request.user
            item.save()
    else:
        form = FormProfissional()
    return render(request, 'forms_app_base/Cadastra_Profissional.html', {'form':form})

def InsereFuncionario(request):
    if request.method=='POST':
        form = FormFuncionario(request.POST)
        if form.is_valid():
            item= form.save(commit=False)
            item.user= request.user
            item.save()
    else:
        form = FormFuncionario()
    return render(request, 'forms_app_base/Cadastra_Funcionario.html', {'form':form})

def InsereCliente(request):
    if request.method=='POST':
        form = FormCliente(request.POST)
        if form.is_valid():
            item= form.save(commit=False)
            item.user= request.user
            item.save()
    else:
        form = FormCliente()
    return render(request, 'forms_app_base/Cadastra_Cliente.html', {'form':form})

def InsereMarca(request):
    if request.method=='POST':
        form = FormMarca(request.POST)
        if form.is_valid():
            item= form.save(commit=False)
            item.user= request.user
            item.save()
    else:
        form = FormMarca()
    return render(request, 'forms_app_base/Cadastra_Marca.html', {'form':form})

def InsereFornecedor(request):
    if request.method=='POST':
        form = FormFornecedor(request.POST)
        if form.is_valid():
            item= form.save(commit=False)
            item.user= request.user
            item.save()
    else:
        form = FormFornecedor()
    return render(request, 'forms_app_base/Cadastra_Fornecedor.html', {'form':form})

def InsereProduto(request):
    if request.method=='POST':
        form = FormProduto(request.POST)
        if form.is_valid():
            item= form.save(commit=False)
            item.user= request.user
            item.save()
    else:
        form = FormProduto()
    return render(request, 'forms_app_base/Cadastra_Produto.html', {'form':form})

def InsereContasAPagar(request):
    if request.method=='POST':
        form = FormContaAPagar(request.POST)
        if form.is_valid():
            item= form.save(commit=False)
            item.user= request.user
            item.save()
    else:
        form = FormContaAPagar()
    return render(request, 'forms_app_base/Cadastra_Contas_a_Pagar.html', {'form':form})

def InsereContasAPagarPagas(request):
    if request.method=='POST':
        form = FormContasApagarPagas(request.POST)
        if form.is_valid():
            item= form.save(commit=False)
            item.user= request.user
            item.save()
    else:
        form = FormContasApagarPagas()
    return render(request, 'forms_app_base/Cadastro_Contas_a_Pagar_Pagas.html', {'form':form})
