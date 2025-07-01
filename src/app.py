# src/app.py

tarefas = []
proximo_id = 1

def resetar_estado_tarefas():
    global tarefas, proximo_id
    tarefas.clear()
    proximo_id = 1

def criar_tarefa(titulo, descricao, status, data_vencimento, prioridade):
    if not titulo or not descricao or not status or not data_vencimento or not prioridade:
        return None

    global proximo_id
    tarefa = {
        "id": proximo_id,
        "titulo": titulo,
        "descricao": descricao,
        "status": status,
        "data_vencimento": data_vencimento,
        "prioridade": prioridade
    }
    tarefas.append(tarefa)
    proximo_id += 1
    return tarefa

def listar_tarefas():
    return tarefas

def buscar_tarefa_por_id(tarefa_id):
    for tarefa in tarefas:
        if tarefa["id"] == tarefa_id:
            return tarefa
    return None

def atualizar_tarefa(tarefa_id, novo_titulo=None, nova_descricao=None, novo_status=None, nova_data_vencimento=None, nova_prioridade=None):
    tarefa = buscar_tarefa_por_id(tarefa_id)
    if tarefa:
        if novo_titulo is not None:
            tarefa["titulo"] = novo_titulo
        if nova_descricao is not None:
            tarefa["descricao"] = nova_descricao
        if novo_status is not None:
            tarefa["status"] = novo_status
        if nova_data_vencimento is not None:
            tarefa["data_vencimento"] = nova_data_vencimento
        if nova_prioridade is not None:
            tarefa["prioridade"] = nova_prioridade
        return True
    return False

def excluir_tarefa(tarefa_id):
    global tarefas
    initial_len = len(tarefas)
    new_tarefas = [t for t in tarefas if t["id"] != tarefa_id]
    
    if len(new_tarefas) < initial_len:
        tarefas.clear()
        tarefas.extend(new_tarefas)
        return True
    return False

def mostrar_menu():
    print("\n--- Sistema de Gerenciamento de Tarefas ---")
    print("1. Criar Tarefa")
    print("2. Listar Tarefas")
    print("3. Atualizar Tarefa")
    print("4. Excluir Tarefa")
    print("5. Sair")
    print("------------------------------------------")

def main():
    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            titulo = input("Digite o título da tarefa: ")
            descricao = input("Digite a descrição da tarefa: ")
            status = input("Digite o status da tarefa (A Fazer, Em Progresso, Concluído): ")
            data_vencimento = input("Digite a data de vencimento (YYYY-MM-DD): ")
            prioridade = input("Digite a prioridade da tarefa (Baixa, Média, Alta): ")
            
            tarefa_criada = criar_tarefa(titulo, descricao, status, data_vencimento, prioridade)
            if tarefa_criada:
                print("Tarefa criada com sucesso!")
            else:
                print("Erro: Todos os campos (Título, Descrição, Status, Data de Vencimento, Prioridade) são obrigatórios.")

        elif escolha == '2':
            todas_tarefas = listar_tarefas()
            if todas_tarefas:
                print("\n--- Lista de Tarefas ---")
                for t in todas_tarefas:
                    print(f"ID: {t['id']}, Título: {t['titulo']}, Status: {t['status']}, Vencimento: {t['data_vencimento']}, Prioridade: {t['prioridade']}")
                print("------------------------")
            else:
                print("Nenhuma tarefa cadastrada.")
        elif escolha == '3':
            try:
                tarefa_id = int(input("Digite o ID da tarefa a ser atualizada: "))
                tarefa_existente = buscar_tarefa_por_id(tarefa_id)
                if not tarefa_existente:
                    print("Tarefa não encontrada.")
                    continue

                print("\nDeixe em branco para manter o valor atual.")
                novo_titulo = input(f"Novo título (atual: {tarefa_existente['titulo']}): ") or None
                nova_descricao = input(f"Nova descrição (atual: {tarefa_existente['descricao']}): ") or None
                novo_status = input(f"Novo status (atual: {tarefa_existente['status']}): ") or None
                nova_data_vencimento = input(f"Nova data de vencimento (atual: {tarefa_existente['data_vencimento']}): ") or None
                nova_prioridade = input(f"Nova prioridade (atual: {tarefa_existente['prioridade']}): ") or None

                if atualizar_tarefa(tarefa_id, novo_titulo, nova_descricao, novo_status, nova_data_vencimento, nova_prioridade):
                    print("Tarefa atualizada com sucesso!")
                else:
                    print("Erro ao atualizar tarefa. Verifique o ID.")
            except ValueError:
                print("ID inválido. Digite um número inteiro.")
        elif escolha == '4':
            try:
                tarefa_id = int(input("Digite o ID da tarefa a ser excluída: "))
                if excluir_tarefa(tarefa_id):
                    print("Tarefa excluída com sucesso!")
                else:
                    print("Tarefa não encontrada.")
            except ValueError:
                print("ID inválido. Digite um número inteiro.")
        elif escolha == '5':
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()
