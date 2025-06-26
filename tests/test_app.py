# tests/test_app.py
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from app import criar_tarefa, listar_tarefas, atualizar_tarefa, excluir_tarefa, resetar_estado_tarefas, tarefas, proximo_id

def setup_function(function):

    resetar_estado_tarefas() 

def test_criar_tarefa_sucesso():
   
    tarefa = criar_tarefa("Estudar Python", "Aprender conceitos de POO", "2025-07-10")
    assert tarefa is not None 
    assert tarefa["titulo"] == "Estudar Python"
    assert tarefa["descricao"] == "Aprender conceitos de POO"
    assert tarefa["status"] == "A Fazer"
    assert tarefa["data_vencimento"] == "2025-07-10"
    assert tarefa["id"] == 1 
    assert len(tarefas) == 1 

def test_criar_tarefa_campos_obrigatorios():
    
    tarefa_invalida_titulo = criar_tarefa("", "Descrição", "2025-07-10")
    assert tarefa_invalida_titulo is None
    assert len(tarefas) == 0 


    tarefa_invalida_descricao = criar_tarefa("Título", "", "2025-07-10")
    assert tarefa_invalida_descricao is None
    assert len(tarefas) == 0

   
    tarefa_invalida_data = criar_tarefa("Título", "Descrição", "")
    assert tarefa_invalida_data is None
    assert len(tarefas) == 0

def test_criar_multiplas_tarefas_id_sequencial():
   
    tarefa1 = criar_tarefa("Comprar pão", "Mercado", "2025-06-27")
    tarefa2 = criar_tarefa("Lavar carro", "No posto", "2025-06-28")
    
    assert tarefa1["id"] == 1
    assert tarefa2["id"] == 2
    assert len(tarefas) == 2 


def test_atualizar_tarefa_sucesso():
  
    criar_tarefa("Tarefa Antiga", "Desc Antiga", "2025-01-01")
    
    atualizado = atualizar_tarefa(1, novo_titulo="Tarefa Nova", novo_status="Concluído")
    assert atualizado is True 
    
    tarefa_atualizada = listar_tarefas()[0] 
    assert tarefa_atualizada["titulo"] == "Tarefa Nova"
    assert tarefa_atualizada["status"] == "Concluído"
    assert tarefa_atualizada["descricao"] == "Desc Antiga" 
    assert tarefa_atualizada["data_vencimento"] == "2025-01-01" 

def test_atualizar_tarefa_nao_encontrada():
 
    criar_tarefa("Tarefa Teste", "Desc Teste", "2025-01-01")
    
    
    atualizado = atualizar_tarefa(99, novo_status="Concluído")
    assert atualizado is False 
    assert len(listar_tarefas()) == 1 


def test_excluir_tarefa_sucesso():
   
    criar_tarefa("Tarefa para Excluir", "Desc", "2025-01-01") 
    assert len(tarefas) == 1 

    excluido = excluir_tarefa(1) 
    assert excluido is True 
    assert len(tarefas) == 0 

def test_excluir_tarefa_nao_encontrada():
   
    criar_tarefa("Tarefa para Manter", "Desc", "2025-01-01") 
    assert len(tarefas) == 1 

    excluido = excluir_tarefa(99)
    assert excluido is False 
    assert len(tarefas) == 1 

