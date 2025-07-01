import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import app

def setup_function(function):
    app.resetar_estado_tarefas()
    app.resetar_estado_usuarios()

def test_criar_tarefa_sucesso_com_prioridade():
    tarefa = app.criar_tarefa("Estudar Python", "Aprender conceitos de POO", "A Fazer", "2025-07-10", "Alta")
    assert tarefa is not None
    assert tarefa["titulo"] == "Estudar Python"
    assert tarefa["descricao"] == "Aprender conceitos de POO"
    assert tarefa["status"] == "A Fazer"
    assert tarefa["data_vencimento"] == "2025-07-10"
    assert tarefa["prioridade"] == "Alta"
    assert tarefa["id"] == 1
    assert len(app.tarefas) == 1

def test_criar_tarefa_campos_obrigatorios_com_prioridade():
    tarefa_invalida_titulo = app.criar_tarefa("", "Descrição", "A Fazer", "2025-07-10", "Média")
    assert tarefa_invalida_titulo is None
    assert len(app.tarefas) == 0

    tarefa_invalida_descricao = app.criar_tarefa("Título", "", "A Fazer", "2025-07-10", "Média")
    assert tarefa_invalida_descricao is None
    assert len(app.tarefas) == 0

    tarefa_invalida_data = app.criar_tarefa("Título", "Descrição", "A Fazer", "", "Média")
    assert tarefa_invalida_data is None
    assert len(app.tarefas) == 0

    tarefa_invalida_status = app.criar_tarefa("Título", "Descrição", "", "2025-07-10", "Média")
    assert tarefa_invalida_status is None
    assert len(app.tarefas) == 0


def test_criar_multiplas_tarefas_id_sequencial_com_prioridade():
    tarefa1 = app.criar_tarefa("Comprar pão", "Mercado", "A Fazer", "2025-06-27", "Baixa")
    tarefa2 = app.criar_tarefa("Lavar carro", "No posto", "Em Progresso", "2025-06-28", "Média")
    
    assert tarefa1["id"] == 1
    assert tarefa2["id"] == 2
    assert len(app.tarefas) == 2

def test_atualizar_tarefa_sucesso_com_prioridade():
    app.criar_tarefa("Tarefa Antiga", "Desc Antiga", "A Fazer", "2025-01-01", "Baixa")
    
    atualizado = app.atualizar_tarefa(1, novo_titulo="Tarefa Nova", novo_status="Concluído", nova_prioridade="Alta")
    assert atualizado is True
    
    tarefa_atualizada = app.listar_tarefas()[0]
    assert tarefa_atualizada["titulo"] == "Tarefa Nova"
    assert tarefa_atualizada["status"] == "Concluído"
    assert tarefa_atualizada["prioridade"] == "Alta"
    assert tarefa_atualizada["descricao"] == "Desc Antiga"
    assert tarefa_atualizada["data_vencimento"] == "2025-01-01"

def test_atualizar_tarefa_nao_encontrada_com_prioridade():
    app.criar_tarefa("Tarefa Teste", "Desc Teste", "A Fazer", "2025-01-01", "Média")
    
    atualizado = app.atualizar_tarefa(99, novo_status="Concluído", nova_prioridade="Alta")
    assert atualizado is False
    assert len(app.listar_tarefas()) == 1

def test_excluir_tarefa_sucesso_com_prioridade():
    app.criar_tarefa("Tarefa para Excluir", "Desc", "A Fazer", "2025-01-01", "Baixa")
    assert len(app.tarefas) == 1

    excluido = app.excluir_tarefa(1)
    assert excluido is True
    assert len(app.tarefas) == 0

def test_excluir_tarefa_nao_encontrada_com_prioridade():
    app.criar_tarefa("Tarefa para Manter", "Desc", "A Fazer", "2025-01-01", "Alta")
    assert len(app.tarefas) == 1

    excluido = app.excluir_tarefa(99)
    assert excluido is False
    assert len(app.tarefas) == 1

def test_registrar_usuario_sucesso():
    usuario = app.registrar_usuario("testuser", "password123")
    assert usuario is not None
    assert usuario["nome_usuario"] == "testuser"
    assert usuario["senha"] == "password123"
    assert usuario["id"] == 1
    assert len(app.usuarios) == 1

def test_registrar_usuario_campos_vazios():
    usuario_invalido = app.registrar_usuario("", "password123")
    assert usuario_invalido is None
    assert len(app.usuarios) == 0

    usuario_invalido = app.registrar_usuario("testuser2", "")
    assert usuario_invalido is None
    assert len(app.usuarios) == 0

def test_registrar_usuario_existente():
    app.registrar_usuario("existinguser", "pass1")
    usuario_duplicado = app.registrar_usuario("existinguser", "pass2")
    assert usuario_duplicado is None
    assert len(app.usuarios) == 1

def test_fazer_login_sucesso():
    app.registrar_usuario("loginuser", "loginpass")
    login_sucesso = app.fazer_login("loginuser", "loginpass")
    assert login_sucesso is True
    assert app.usuario_logado["nome_usuario"] == "loginuser"

def test_fazer_login_credenciais_incorretas():
    app.registrar_usuario("wronguser", "wrongpass")
    login_falha = app.fazer_login("wronguser", "incorrect")
    assert login_falha is False
    assert app.usuario_logado is None

    login_falha = app.fazer_login("nonexistent", "anypass")
    assert login_falha is False
    assert app.usuario_logado is None

def test_fazer_logout_sucesso():
    app.registrar_usuario("logoutuser", "logoutpass")
    app.fazer_login("logoutuser", "logoutpass")
    assert app.usuario_logado is not None

    logout_sucesso = app.fazer_logout()
    assert logout_sucesso is True
    assert app.usuario_logado is None
