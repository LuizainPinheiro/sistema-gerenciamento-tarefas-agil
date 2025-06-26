# tests/test_app.py
import sys
import os

# Adiciona o diretório 'src' ao caminho de importação do Python
# para que 'app.py' possa ser importado corretamente.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Importa as funções e variáveis globais do app.py necessárias para os testes.
# A função resetar_estado_tarefas é crucial para a independência dos testes.
from app import criar_tarefa, listar_tarefas, atualizar_tarefa, excluir_tarefa, resetar_estado_tarefas, tarefas, proximo_id

# O pytest possui um mecanismo de "fixtures" que é mais robusto para setup/teardown.
# No entanto, para este projeto, manter o setup_function que chama resetar_estado_tarefas() é eficaz.
def setup_function(function):
    """
    Esta função é executada ANTES de cada teste individual (função com prefixo 'test_').
    Ela garante que a lista 'tarefas' e o contador 'proximo_id' sejam resetados,
    assegurando que cada teste inicie com um estado limpo e não seja afetado
    por execuções de testes anteriores.
    """
    resetar_estado_tarefas() # Chama a função do app.py para resetar o estado global

# --- Testes para a função criar_tarefa ---

def test_criar_tarefa_sucesso():
    """
    Verifica se a função 'criar_tarefa' cria uma tarefa corretamente,
    com os atributos esperados e se a tarefa é adicionada à lista global.
    """
    tarefa = criar_tarefa("Estudar Python", "Aprender conceitos de POO", "2025-07-10")
    assert tarefa is not None # Garante que a tarefa foi retornada
    assert tarefa["titulo"] == "Estudar Python"
    assert tarefa["descricao"] == "Aprender conceitos de POO"
    assert tarefa["status"] == "A Fazer" # Verifica o status padrão
    assert tarefa["data_vencimento"] == "2025-07-10"
    assert tarefa["id"] == 1 # Verifica o ID inicial
    assert len(tarefas) == 1 # Verifica se a tarefa foi adicionada à lista

def test_criar_tarefa_campos_obrigatorios():
    """
    Testa se a função 'criar_tarefa' retorna None (indicando falha)
    e não adiciona a tarefa à lista quando campos obrigatórios estão vazios.
    """
    # Testando com título vazio
    tarefa_invalida_titulo = criar_tarefa("", "Descrição", "2025-07-10")
    assert tarefa_invalida_titulo is None
    assert len(tarefas) == 0 # Nenhuma tarefa deve ser adicionada

    # Testando com descrição vazia (reseta o estado antes de cada teste)
    tarefa_invalida_descricao = criar_tarefa("Título", "", "2025-07-10")
    assert tarefa_invalida_descricao is None
    assert len(tarefas) == 0

    # Testando com data de vencimento vazia
    tarefa_invalida_data = criar_tarefa("Título", "Descrição", "")
    assert tarefa_invalida_data is None
    assert len(tarefas) == 0

def test_criar_multiplas_tarefas_id_sequencial():
    """
    Verifica se os IDs das tarefas são gerados de forma sequencial e correta
    quando múltiplas tarefas são criadas.
    """
    tarefa1 = criar_tarefa("Comprar pão", "Mercado", "2025-06-27")
    tarefa2 = criar_tarefa("Lavar carro", "No posto", "2025-06-28")
    
    assert tarefa1["id"] == 1
    assert tarefa2["id"] == 2
    assert len(tarefas) == 2 # Garante que ambas foram adicionadas

# --- Testes para a função atualizar_tarefa ---

def test_atualizar_tarefa_sucesso():
    """
    Testa se a função 'atualizar_tarefa' modifica corretamente
    os atributos de uma tarefa existente.
    """
    criar_tarefa("Tarefa Antiga", "Desc Antiga", "2025-01-01") # Cria uma tarefa com ID 1
    
    # Atualiza título e status
    atualizado = atualizar_tarefa(1, novo_titulo="Tarefa Nova", novo_status="Concluído")
    assert atualizado is True # Deve indicar sucesso na atualização
    
    tarefa_atualizada = listar_tarefas()[0] # Pega a tarefa que foi atualizada
    assert tarefa_atualizada["titulo"] == "Tarefa Nova"
    assert tarefa_atualizada["status"] == "Concluído"
    assert tarefa_atualizada["descricao"] == "Desc Antiga" # Descrição não foi alterada, deve permanecer a mesma
    assert tarefa_atualizada["data_vencimento"] == "2025-01-01" # Data também não foi alterada

def test_atualizar_tarefa_nao_encontrada():
    """
    Testa se a função 'atualizar_tarefa' retorna False
    quando tenta atualizar uma tarefa que não existe.
    """
    criar_tarefa("Tarefa Teste", "Desc Teste", "2025-01-01") # Cria uma tarefa com ID 1
    
    # Tenta atualizar uma tarefa com ID 99 (que não existe)
    atualizado = atualizar_tarefa(99, novo_status="Concluído")
    assert atualizado is False # Deve indicar falha na atualização
    assert len(listar_tarefas()) == 1 # A tarefa original deve permanecer intacta na lista

# --- Testes para a função excluir_tarefa ---

def test_excluir_tarefa_sucesso():
    """
    Testa se a função 'excluir_tarefa' remove corretamente
    uma tarefa existente da lista.
    """
    criar_tarefa("Tarefa para Excluir", "Desc", "2025-01-01") # Cria uma tarefa com ID 1
    assert len(tarefas) == 1 # Verifica que a tarefa foi adicionada

    excluido = excluir_tarefa(1) # Tenta excluir a tarefa com ID 1
    assert excluido is True # Deve indicar sucesso na exclusão
    assert len(tarefas) == 0 # A lista de tarefas deve estar vazia após a exclusão

def test_excluir_tarefa_nao_encontrada():
    """
    Testa se a função 'excluir_tarefa' retorna False
    quando tenta excluir uma tarefa que não existe.
    """
    criar_tarefa("Tarefa para Manter", "Desc", "2025-01-01") # Cria uma tarefa com ID 1
    assert len(tarefas) == 1 # Verifica que a tarefa foi adicionada

    excluido = excluir_tarefa(99) # Tenta excluir uma tarefa com ID 99 (não existente)
    assert excluido is False # Deve indicar falha na exclusão
    assert len(tarefas) == 1 # A tarefa original deve permanecer na lista

