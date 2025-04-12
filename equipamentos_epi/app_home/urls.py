from django.urls import path
from app_home import views

urlpatterns = [
    path('', views.home),
    path('cadastrar_colaborador/', views.cadastrar_colaborador),
    path('sucesso/', views.sucesso),
    path('cadastrar_epi/', views.cadastrar_epi),
    path('cadastro_epi_sucesso/', views.cadastro_epi_sucesso),
    path('registrar/', views.registrar),
    path('registro_sucesso/', views.registro_sucesso, name= 'registro_sucesso'),
    path('listar_colaboradores/', views.listar_colaboradores, name= 'listar_colaboradores'),
    path('editar_colaborador/<int:id>/', views.editar_colaborador, name= 'editar_colaborador'),
    path('excluir_colaborador/<int:id>/', views.excluir_colaborador, name='excluir_colaborador'),
    path('listar_epi/', views.listar_epi, name= 'listar_epi'),
    path('editar_epi/<int:id>/', views.editar_epi, name= 'editar_epi'),
    path('excluir_epi/<int:id>/', views.excluir_epi, name= 'excluir_epi')
]

