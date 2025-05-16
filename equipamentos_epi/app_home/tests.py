import pytest
from django.urls import reverse
from datetime import date
from django.core.exceptions import ValidationError
from app_home.models import Colaborador, EPI, Registrar

@pytest.mark.django_db
@pytest.mark.parametrize("nome_url, status_esperado, metodo_http, dados_post", [
    ('home', 200, 'get', None),
    ('listar_colaboradores', 200, 'get', None),
    ('listar_epi', 200, 'get', None),
    ('cadastro_epi_sucesso', 200, 'get', None),
    ('cadastrar_colaborador', 200, 'get', None),
    ('sucesso', 200, 'get', None),
    ('cadastrar_epi', 200, 'get', None),
    ('registrar', 200, 'get', None),
    ('listar_registro_relatorio', 200, 'get', None),
    ('relatorio_colaborador', 200, 'get', None),
    ('perfil', 200, 'get', None),
    ('visualizar_quantidade_epi', 200, 'get', None),
    ('avisos', 200, 'get', None),

    ('editar_colaborador', 200, 'get', None),
    ('editar_epi', 200, 'get', None),

    ('editar_colaborador', 302, 'post', {'nome': 'Novo Nome', 'email': 'novo@email.com', 'cargo': 'Cargo', 'telefone': '123456789'}),
    ('editar_epi', 302, 'post', {'nomeEPI': 'Novo EPI', 'descricao': 'Desc', 'validade': '2026-12-31', 'quantidade_disponivel': 5, 'codigo': 'COD123'}),
    ('editar_status', 302, 'post', {'status': 'devolvido', 'condicao_equipamento': 'bom', 'observacao': 'teste', 'data_devolucao': '2025-05-16'}),

    ('excluir_colaborador', 302, 'post', None),
    ('excluir_epi', 302, 'post', None),
])
def test_views(client, nome_url, status_esperado, metodo_http, dados_post):
    colaborador = None
    epi = None
    registrar = None

    if nome_url in ['editar_colaborador', 'excluir_colaborador']:
        colaborador = Colaborador.objects.create(
            nome="Teste Colaborador",
            email="teste@teste.com",
            cargo="Cargo",
            telefone="123456789"
        )

    if nome_url in ['editar_epi', 'excluir_epi']:
        epi = EPI.objects.create(
            nomeEPI="Teste EPI",
            descricao="Descrição",
            validade=date(2026, 1, 1),
            quantidade_disponivel=10,
            codigo="CODTESTE"
        )

    if nome_url == 'editar_status':
        colaborador = Colaborador.objects.create(
            nome="Colaborador para status",
            email="colabstatus@teste.com",
            cargo="Cargo",
            telefone="987654321"
        )
        epi = EPI.objects.create(
            nomeEPI="EPI para status",
            descricao="Descrição",
            validade=date(2026, 1, 1),
            quantidade_disponivel=10,
            codigo="CODSTATUS"
        )
        registrar = Registrar.objects.create(
            colaborador=colaborador,
            equipamento=epi,
            status='emprestado',
            condicao_equipamento='bom',
            data_emprestimo=date.today(),
            data_prevista_da_devolucao=date.today()
        )

    if nome_url in ['editar_colaborador', 'excluir_colaborador']:
        url = reverse(nome_url, args=[colaborador.id])
    elif nome_url in ['editar_epi', 'excluir_epi']:
        url = reverse(nome_url, args=[epi.id])
    elif nome_url == 'editar_status':
        url = reverse(nome_url, args=[registrar.id])
    else:
        url = reverse(nome_url)

    if metodo_http == 'get':
        response = client.get(url)
    else:
        response = client.post(url, data=dados_post or {})

    assert response.status_code == status_esperado


@pytest.mark.django_db
def test_epi_validade_nao_passada():
    epi = EPI(
        nomeEPI="EPI Vencido",
        descricao="Descrição",
        validade=date(2000, 1, 1),  
        quantidade_disponivel=1,
        codigo="COD001"
    )

    hoje = date.today()
    if epi.validade < hoje:
        valido = False
    else:
        valido = True
    assert valido is False


@pytest.mark.django_db
def test_registrar_str():
    colaborador = Colaborador.objects.create(nome="Ana", email="ana@email.com", cargo="Engenheira", telefone="123456789")
    epi = EPI.objects.create(nomeEPI="Botina", descricao="Descrição", validade=date(2026, 1, 1), quantidade_disponivel=5, codigo="BOT001")
    registrar = Registrar.objects.create(
        equipamento=epi,
        colaborador=colaborador,
        status='emprestado',
        condicao_equipamento='bom',
        data_emprestimo=date.today(),
        data_prevista_da_devolucao=date.today()
    )
    assert str(registrar) == "Botina - Ana"
