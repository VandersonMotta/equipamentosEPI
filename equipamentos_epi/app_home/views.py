from django.shortcuts import render, redirect, get_object_or_404
from .forms import ColaboradorForm
from .forms import EPIForm
from .forms import RegistrarForm
from django.contrib import messages
from .models import Colaborador

def home(request):
    return render(request, 'app_home/pages/home.html')

def listar_colaboradores(request): 
    colaboradores = Colaborador.objects.all()
    return render(request, 'app_home/pages/listar_colaboradores.html', {'colaboradores': colaboradores})

def editar_colaborador(request, id):
    colaborador = get_object_or_404(Colaborador, id=id)
    if request.method == 'POST':
        form = ColaboradorForm(request.POST, instance=colaborador)
        if form.is_valid():
            form.save()
            messages.success(request, 'Colaborador atualizado com sucesso!')
            return redirect('listar_colaboradores')
    else:
        form = ColaboradorForm(instance=colaborador)    
    return render(request, 'app_home/pages/editar_colaborador.html', {'form': form})

def excluir_colaborador(request, id):
    colaborador = get_object_or_404(Colaborador, id=id)
    colaborador.delete()
    messages.success(request, 'Colaborador excluído com sucesso!')
    return redirect('listar_colaboradores')

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

def registrar (request):
    if request.method == 'POST':
        form = RegistrarForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registrado com sucesso!')  
            return redirect(registrar)       
        else:        
            messages.error(request, "Item não foi cadastrado. Verifique os campos obrigatórios.")
    else:
        form = RegistrarForm()

    return render(request, 'app_home/pages/registrar.html', {'form': form})

def registro_sucesso(request):
    return render(request,'app_home/pages/registro_sucesso.html')