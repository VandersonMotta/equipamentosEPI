from django.urls import path
from app_home import views

urlpatterns = [
    path('', views.home),
    path('cadastrar_colaborador/', views.cadastrar_colaborador),
    path('sucesso/', views.sucesso),
]

