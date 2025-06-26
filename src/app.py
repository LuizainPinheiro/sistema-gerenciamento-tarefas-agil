# src/app.py

# Lista para armazenar as tarefas (simulação em memória por enquanto)
tarefas = []
proximo_id = 1

def criar_tarefa(titulo, descricao, data_vencimento):
    """Cria uma nova tarefa e a adiciona à lista."""
    global proximo_id
    if not titulo or not descricao or not data_vencimento:
        # Imprime erro apenas na CLI, não nos testes
        if __name__ == "__main__":
            print("Erro: Todos os campos (título, descrição, data de vencimento) são obrigatórios.")
        return None # Retorna None para indicar falha na criação

    tarefa = {
        "id": proximo_id,
        "titulo": titulo,
        "descricao": descricao,
        "status": "A Fazer", # Status inicial padrão
        "data_vencimento": data_vencimento
    }
    tarefas.append(tarefa)
    proximo_id += 1
    return tarefa

def listar_tarefas():
    """Retorna todas as tarefas cadastradas."""
    return tarefas

def atualizar_tarefa(id_tarefa, novo_titulo=None, nova_descricao=None, novo_status=None, nova_data_vencimento=None):
    """
    Atualiza os detalhes de uma tarefa existente.
    Retorna True se a tarefa for encontrada e atualizada, False caso contrário.
    """
    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa:
            if novo_titulo is not None:
                tarefa["titulo"] = novo_titulo
            if nova_descricao is not None:
                tarefa["descricao"] = nova_descricao
            if novo_status is not None:
                # Opcional: Adicionar validação para status permitidos
                tarefa["status"] = novo_status
            if nova_data_vencimento is not None:
                tarefa["data_vencimento"] = nova_data_vencimento
            return True
    return False # Tarefa não encontrada

def excluir_tarefa(id_tarefa):
    """
    Exclui uma tarefa da lista.
    Retorna True se a tarefa for encontrada e excluída, False caso contrário.
    """
    global tarefas
    
    tarefas_mantidas = [t for t in tarefas if t["id"] != id_tarefa]

    if len(tarefas_mantidas) < len(tarefas):
        tarefas[:] = tarefas_mantidas # <--- Esta é a linha corrigida
        return True
    return False


def resetar_estado_tarefas():
    """
    Reseta a lista de tarefas e o contador de ID para os testes.
    Isso é crucial para garantir que cada teste inicie com um estado limpo.
    """
    global tarefas, proximo_id
    tarefas.clear() # Limpa a lista de tarefas
    proximo_id = 1   # Reseta o contador de ID


# --- Interface de Linha de Comando Simples (CLI) ---
if __name__ == "__main__":
    print("--- Sistema de Gerenciamento de Tarefas (CLI) ---")
    
    while True:
        print("\nMenu:")
        print("1. Criar Nova Tarefa")
        print("2. Visualizar Todas as Tarefas")
        print("3. Atualizar Tarefa Existente")
        print("4. Excluir Tarefa")
        print("5. Sair")
        
        escolha = input("Digite sua opção: ")

        if escolha == '1':
            print("\n--- Criar Tarefa ---")
            titulo = input("  Título: ")
            descricao = input("  Descrição: ")
            data_vencimento = input("  Data de Vencimento (AAAA-MM-DD): ")
            
            nova_tarefa = criar_tarefa(titulo, descricao, data_vencimento)
            if nova_tarefa: # Verifica se a tarefa foi realmente criada (não é None)
                print(f"Tarefa '{nova_tarefa['titulo']}' (ID: {nova_tarefa['id']}) criada com sucesso.")
        
        elif escolha == '2':
            print("\n--- Lista de Tarefas ---")
            todas_tarefas = listar_tarefas()
            if not todas_tarefas:
                print("  Nenhuma tarefa cadastrada até o momento.")
            else:
                for t in todas_tarefas:
                    print(f"  ID: {t['id']} | Título: {t['titulo']} | Status: {t['status']} | Vencimento: {t['data_vencimento']}")
            print("--------------------------")
        
        elif escolha == '3':
            print("\n--- Atualizar Tarefa ---")
            try:
                id_para_atualizar = int(input("  Digite o ID da tarefa para atualizar: "))
                
                # Coleta os novos dados, permitindo que fiquem vazios se não houver alteração
                novo_status = input("  Novo Status (A Fazer, Em Progresso, Concluído - deixe em branco para não alterar): ")
                novo_titulo = input("  Novo Título (deixe em branco para não alterar): ")
                nova_descricao = input("  Nova Descrição (deixe em branco para não alterar): ")
                nova_data_vencimento = input("  Nova Data de Vencimento (AAAA-MM-DD - deixe em branco para não alterar): ")

                # Passa None se o campo estiver vazio, para que a função ignore
                atualizado = atualizar_tarefa(
                    id_para_atualizar,
                    novo_titulo if novo_titulo else None,
                    nova_descricao if nova_descricao else None,
                    novo_status if novo_status else None,
                    nova_data_vencimento if nova_data_vencimento else None
                )
                if atualizado:
                    print(f"Tarefa ID {id_para_atualizar} atualizada com sucesso.")
                else:
                    print(f"Erro: Tarefa ID {id_para_atualizar} não encontrada.")
            except ValueError:
                print("ID inválido. Por favor, digite um número inteiro.")

        elif escolha == '4':
            print("\n--- Excluir Tarefa ---")
            try:
                id_para_excluir = int(input("  Digite o ID da tarefa para excluir: "))
                excluido = excluir_tarefa(id_para_excluir)
                if excluido:
                    print(f"Tarefa ID {id_para_excluir} excluída com sucesso.")
                else:
                    print(f"Erro: Tarefa ID {id_para_excluir} não encontrada.")
            except ValueError:
                print("ID inválido. Por favor, digite um número inteiro.")

        elif escolha == '5':
            print("Encerrando o sistema. Até logo!")
            break
        
        else:
            print("Opção inválida. Por favor, escolha um número válido do menu.")

