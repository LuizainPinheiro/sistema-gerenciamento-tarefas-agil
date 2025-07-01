import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from app import criar_tarefa, listar_tarefas, atualizar_tarefa, excluir_tarefa, resetar_estado_tarefas, tarefas, proximo_id

def setup_function(function):
    resetar_estado_tarefas()

def test_criar_tarefa_sucesso_com_prioridade():
    tarefa = criar_tarefa("Estudar Python", "Aprender conceitos de POO", "A Fazer", "2025-07-10", "Alta")
    assert tarefa is not None
    assert tarefa["titulo"] == "Estudar Python"
    assert tarefa["descricao"] == "Aprender conceitos de POO"
    assert tarefa["status"] == "A Fazer"
    assert tarefa["data_vencimento"] == "2025-07-10"
    assert tarefa["prioridade"] == "Alta"
    assert tarefa["id"] == 1
    assert len(tarefas) == 1

def test_criar_tarefa_campos_obrigatorios_com_prioridade():
    tarefa_invalida_titulo = criar_tarefa("", "Descrição", "A Fazer", "2025-07-10", "Média")
    assert tarefa_invalida_titulo is None
    assert len(tarefas) == 0

    tarefa_invalida_descricao = criar_tarefa("Título", "", "A Fazer", "2025-07-10", "Média")
    assert tarefa_invalida_descricao is None
    assert len(tarefas) == 0

    tarefa_invalida_data = criar_tarefa("Título", "Descrição", "A Fazer", "", "Média")
    assert tarefa_invalida_data is None
    assert len(tarefas) == 0

    tarefa_invalida_status = criar_tarefa("Título", "Descrição", "", "2025-07-10", "Média")
    assert tarefa_invalida_status is None
    assert len(tarefas) == 0


def test_criar_multiplas_tarefas_id_sequencial_com_prioridade():
    tarefa1 = criar_tarefa("Comprar pão", "Mercado", "A Fazer", "2025-06-27", "Baixa")
    tarefa2 = criar_tarefa("Lavar carro", "No posto", "Em Progresso", "2025-06-28", "Média")
    
    assert tarefa1["id"] == 1
    assert tarefa2["id"] == 2
    assert len(tarefas) == 2

def test_atualizar_tarefa_sucesso_com_prioridade():
    criar_tarefa("Tarefa Antiga", "Desc Antiga", "A Fazer", "2025-01-01", "Baixa")
    
    atualizado = atualizar_tarefa(1, novo_titulo="Tarefa Nova", novo_status="Concluído", nova_prioridade="Alta")
    assert atualizado is True
    
    tarefa_atualizada = listar_tarefas()[0]
    assert tarefa_atualizada["titulo"] == "Tarefa Nova"
    assert tarefa_atualizada["status"] == "Concluído"
    assert tarefa_atualizada["prioridade"] == "Alta"
    assert tarefa_atualizada["descricao"] == "Desc Antiga"
    assert tarefa_atualizada["data_vencimento"] == "2025-01-01"

def test_atualizar_tarefa_nao_encontrada_com_prioridade():
    criar_tarefa("Tarefa Teste", "Desc Teste", "A Fazer", "2025-01-01", "Média")
    
    atualizado = atualizar_tarefa(99, novo_status="Concluído", nova_prioridade="Alta")
    assert atualizado is False
    assert len(listar_tarefas()) == 1

def test_excluir_tarefa_sucesso_com_prioridade():
    criar_tarefa("Tarefa para Excluir", "Desc", "A Fazer", "2025-01-01", "Baixa")
    assert len(tarefas) == 1

    excluido = excluir_tarefa(1)
    assert excluido is True
    assert len(tarefas) == 0

def test_excluir_tarefa_nao_encontrada_com_prioridade():
    criar_tarefa("Tarefa para Manter", "Desc", "A Fazer", "2025-01-01", "Alta")
    assert len(tarefas) == 1

    excluido = excluir_tarefa(99)
    assert excluido is False
    assert len(tarefas) == 1
