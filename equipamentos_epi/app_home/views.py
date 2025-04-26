from django.shortcuts import render, redirect, get_object_or_404
from .forms import ColaboradorForm
from .forms import EPIForm
from .forms import RegistrarForm
from django.contrib import messages
from .models import Colaborador
from .models import EPI
from .models import Registrar

def home(request):
    return render(request, 'app_home/pages/home.html')

def listar_colaboradores(request): 
    termo_busca = request.GET.get('busca', '')  # pega o valor do campo de busca da URL
    if termo_busca:
        colaboradores = Colaborador.objects.filter(nome__icontains=termo_busca)
    else:
        colaboradores = Colaborador.objects.all()
        
    return render(request, 'app_home/pages/listar_colaboradores.html', {
        'colaboradores': colaboradores,
        'termo_busca': termo_busca,
    })

def listar_epi(request):
    busca = request.GET.get('busca', '')
    if busca:
        epi = EPI.objects.filter(nomeEPI__icontains=busca)
    else:      
        epi = EPI.objects.all()
        
    return render(request, 'app_home/pages/listar_epi.html', {'equipamentos': epi, 'busca': busca})


def editar_colaborador(request, id):
    colaborador = get_object_or_404(Colaborador, id=id)
    if request.method == 'POST':
        form = ColaboradorForm(request.POST, instance=colaborador)
        if form.is_valid():
            form.save()
            messages.success(request, 'Colaborador atualizado!')
            return redirect('listar_colaboradores')
    else:
        form = ColaboradorForm(instance=colaborador)    
    return render(request, 'app_home/pages/editar_colaborador.html', {'form': form})

def editar_status(request, id):
    registro = get_object_or_404(Registrar, id=id)

    if request.method == 'POST':
        # Só atualiza o campo status
        status_atualizado = request.POST.get('status')
        registro.status = status_atualizado
        registro.save()

        messages.success(request, 'Status atualizado com sucesso!')

        # Redireciona para o relatório certo
        return redirect('relatorio_colaborador')
    else:
        form = RegistrarForm(instance=registro)

    return render(request, 'app_home/pages/editar_status.html', {
        'form': form,
        'registro': registro  # Passar o objeto para mostrar dados
    })

def excluir_epi(request, id):
    epi = get_object_or_404(EPI, id=id)
    epi.delete()
    messages.success(request, 'EPI excluído com sucesso!')
    return redirect('listar_epi')

def cadastro_epi_sucesso(request):
    return render(request,'app_home/pages/cadastro_epi_sucesso.html')

def editar_epi(request, id):
    epi = get_object_or_404(EPI, id=id)
    if request.method == 'POST':
        form = EPIForm(request.POST, instance=epi)
        if form.is_valid():
            form.save()
            messages.success(request, 'Equipamento atualizado!')
            return redirect('listar_epi')
    else:
        form = EPIForm(instance=epi)

    return render(request, 'app_home/pages/editar_epi.html', {'form': form})

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
            form = EPIForm()  
    else:
        form = EPIForm()
    
    return render(request, 'app_home/pages/cadastrar_epi.html', {'form': form})


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

def listar_registro_relatorio(request):
    termo_busca = request.GET.get('busca', '')

    if termo_busca:
        registros = Registrar.objects.filter(
            colaborador__nome__icontains=termo_busca
        )
    else:
        registros = Registrar.objects.all()

    return render(request, 'app_home/pages/listar_registro_relatorio.html', {
        'registros': registros,
        'termo_busca': termo_busca,
    })


def relatorio_colaborador(request):
    termo_busca = request.GET.get('busca', '')
    
    if termo_busca:
        registros = Registrar.objects.filter(
            status='emprestado',
            colaborador__nome__icontains=termo_busca
        )
    else:
        registros = Registrar.objects.filter(status='emprestado')
        
    return render(request, 'app_home/pages/relatorio_colaborador.html', {
        'registros': registros,
        'termo_busca': termo_busca,
    })

def perfil(request):
    return render(request, 'app_home/pages/perfil.html')