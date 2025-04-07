from django.urls import path
from app_home import views

urlpatterns = [
    path('', views.home),
    path('cadastrar_colaborador/', views.cadastrar_colaborador),
    path('sucesso/', views.sucesso),
    path('cadastrar_epi/', views.cadastrar_epi),
    path('cadastro_epi_sucesso/', views.cadastro_epi_sucesso),
    path('registrar/', views.registrar),
]

