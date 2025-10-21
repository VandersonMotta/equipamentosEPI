#  Site de controle de Equipamentos EPI

É um sistema web desenvolvido em Django para gerenciamento de Equipamentos de Proteção Individual (EPIs) e colaboradores. 
Ele permite controlar o cadastro de epis, colaboradores, atualização, registro de empréstimos/devoluções e geração de relatórios dos EPIs de forma eficiente.

## Funcionalidades principais

- **Cadastro e gerenciamento de colaboradores:** Permite adicionar, editar e excluir colaboradores, além de buscar colaboradores por nome.

- **Cadastro e gerenciamento de EPIs:** Permite cadastrar novos EPIs, editar informações, excluir equipamentos e visualizar a quantidade disponível.

- **Registro de empréstimos e devoluções de EPIs:** Controla o status dos equipamentos (emprestado, em uso, fornecido, devolvido, danificado, perdido) e ajusta automaticamente a quantidade disponível.

- **Relatórios e consultas:** Lista de todos os EPIs com filtros de busca, relatório de EPIs emprestados por colaborador, visualização de quantidade de EPIs por status.

- **Avisos automáticos:** Geração de notificações sobre devolução de EPIs próximas da data prevista.

- **Interface web:** Diferentes telas para cadastro, edição, listagem e visualização de informações, totalmente integradas com Django templates.

---

##  Tecnologias Utilizadas
- **Python**: Linguagem de programação principal.
- **Django**: Framework web para o desenvolvimento do back-end.
- **HTML, CSS e JavaScript**: Para a criação da interface de usuário (front-end).
- **SQLite**: Banco de dados padrão do Django, ideal para o desenvolvimento.

---

##  Pré-requisitos
- **Git** – Para clonar o repositório.
- **Python** – Com o ambiente de desenvolvimento configurado (versão 3.x recomendada).
- **pip** – Gerenciador de pacotes do Python.

---

##  Clonar o Repositório

Abra o terminal em seu computador e use o comando:

```bash
git clone https://github.com/VandersonMotta/equipamentosEPI.git
```

Em seguida:

```bash
cd equipamentos_epi
```

---

##  Configurar o Ambiente Virtual

É uma boa prática criar um ambiente virtual para isolar as dependências do projeto.

```bash
python -m venv venv
```

Ative o ambiente virtual:
- **Windows**
```bash
venv\Scripts\activate
```
- **macOS/Linux**
```bash
source venv/bin/activate
```

---

## Instalar as Dependências

Com o ambiente virtual ativado, instale todas as bibliotecas e dependências necessárias:

```bash
pip install -r requirements.txt
```

---

## Executar o Projeto

1. Aplique as migrações do banco de dados para criar as tabelas necessárias:

```bash
python manage.py migrate
```

2. Por fim, inicie o servidor de desenvolvimento:

```bash
python manage.py runserver
```

O projeto estará acessível no link disponível no terminal.

3. Usuário e senha para o login:
   
- **Usuário**: julius
- **Senha**: rock123*
