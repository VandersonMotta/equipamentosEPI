from django.shortcuts import render, redirect
from .forms import ColaboradorForm
from .forms import EPIForm
from django.contrib import messages

def home(request):
    return render(request, 'app_home/pages/home.html')

def cadastrar_colaborador(request):
    if request.method == 'POST':
        form = ColaboradorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Colaborador cadastrado com sucesso!')
            return redirect(cadastrar_colaborador)
    else:
        form = ColaboradorForm()
    return render(request, 'app_home/pages/cadastrar_colaborador.html', {'form' : form})

def sucesso(request):
    return render(request,'app_home/pages/sucesso.html')

def cadastrar_epi(request):
    if request.method == 'POST':
        form = EPIForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'EPI cadastrado com sucesso!')
            return redirect(cadastrar_epi)  
    else:
        form = EPIForm()
    return render(request, 'app_home/pages/cadastrar_epi.html', {'form': form})

def cadastro_epi_sucesso(request):
    return render(request,'app_home/pages/cadastro_epi_sucesso.html')