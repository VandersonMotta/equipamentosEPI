from django.shortcuts import render, redirect
from .forms import ColaboradorForm


def home(request):
    return render(request, 'app_home/pages/home.html')

def cadastrar_colaborador(request):
    if request.method == 'POST':
        form = ColaboradorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sucesso')
    else:
        form = ColaboradorForm()
    return render(request, 'cadastrar_colaborador.html', {'form' : form})

def sucesso(request):
    return render(request,'sucesso.html')
