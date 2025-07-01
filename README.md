# Construindo um Projeto Ágil no GitHub: Sistema de Gerenciamento de Tarefas

## 1. Visão Geral do Projeto

Este repositório documenta e simula o desenvolvimento de um **Sistema de Gerenciamento de Tarefas** para a fictícia **TechFlow Solutions**, uma startup de logística. O objetivo principal é criar uma solução que permita o acompanhamento do fluxo de trabalho em tempo real, a priorização de tarefas críticas e o monitoramento do desempenho da equipe, aplicando os princípios da Engenharia de Software e metodologias ágeis.

## 2. Objetivo e Escopo

### 2.1. Objetivo Geral

Desenvolver um sistema robusto e adaptável para a gestão de tarefas, utilizando práticas ágeis e ferramentas colaborativas, com foco na eficiência operacional e na visibilidade do progresso.

### 2.2. Escopo Inicial

O sistema básico contempla as seguintes funcionalidades essenciais:
* **Gerenciamento de Tarefas (CRUD Completo):** Capacidade de criar, visualizar, atualizar e excluir tarefas. Cada tarefa inclui atributos como título, descrição, status (A Fazer, Em Progresso, Concluído) e data de vencimento.
* **Autenticação de Usuários (A Ser Implementado):** Um sistema básico de login e registro para que os usuários possam acessar suas tarefas de forma segura.

## 3. Metodologia Adotada

Este projeto adota uma abordagem **ágil**, com forte ênfase na **metodologia Kanban** para a gestão do fluxo de trabalho. O Kanban é implementado através da aba `Projects` do GitHub, visualizando o progresso das tarefas em um quadro com colunas definidas. Esta escolha visa promover a flexibilidade, a entrega contínua e a rápida adaptação a eventuais mudanças de requisitos.

## 4. Estrutura do Repositório

O repositório está organizado da seguinte forma:
* `src/`: Contém o código-fonte da aplicação Python.
* `tests/`: Armazena os testes automatizados (utilizando Pytest).
* `docs/`: Guarda a documentação adicional, incluindo diagramas UML.
* `.github/workflows/`: Contém as configurações para o GitHub Actions (Integração Contínua).
* `requirements.txt`: Lista as dependências Python do projeto.

## 5. Como Executar o Sistema

Para executar a versão atual do sistema (interface de linha de comando para gerenciar tarefas), siga os passos abaixo:

1.  **Clone este repositório:**
    ```bash
    git clone [https://github.com/LuizainPinheiro/sistema-gerenciamento-tarefas-agil.git](https://github.com/LuizainPinheiro/sistema-gerenciamento-tarefas-agil.git)
    ```

2.  **Navegue até o diretório do projeto:**
    ```bash
    cd sistema-gerenciamento-tarefas-agil
    ```

3.  **Crie e ative o ambiente virtual (recomendado):**
    ```bash
    python -m venv .venv
    # No Windows (PowerShell): .\.venv\Scripts\Activate.ps1
    # No Windows (CMD): .\.venv\Scripts\activate.bat
    # No macOS/Linux (Git Bash): source .venv/bin/activate
    ```

4.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Execute a aplicação:**
    ```bash
    python src/app.py
    ```
    Siga as instruções no terminal para interagir com o sistema (criar, listar, atualizar, excluir tarefas).

6.  **Executar Testes Unitários Localmente:**
    Com o ambiente virtual ativado e na raiz do projeto, execute:
    ```bash
    pytest
    ```

## 6. Testes Automatizados e Integração Contínua (CI/CD)

Este projeto utiliza testes unitários com `pytest` para garantir a qualidade do código. A integração contínua (CI) é implementada via **GitHub Actions**, que automatiza a execução desses testes a cada `push` ou `pull request` para a branch `main`. Isso garante que novas funcionalidades ou alterações não introduzam regressões, mantendo a estabilidade e a confiabilidade do sistema.

O workflow de CI pode ser visualizado e seus resultados acompanhados na aba '[Actions](https://github.com/LuizainPinheiro/sistema-gerenciamento-tarefas-agil/actions)' do repositório.

## 7. Histórico de Mudanças de Escopo

*(Esta seção será preenchida posteriormente, durante a simulação de gestão de mudanças.)*

## 8. Modelagem UML

### 8.1. Diagrama de Casos de Uso
O Diagrama de Casos de Uso (DCU) é uma ferramenta da Unified Modeling Language (UML) empregada para modelar a funcionalidade de um sistema sob a perspectiva de seus usuários. Para o Sistema de Gerenciamento de Tarefas, a elaboração deste diagrama foi crucial para visualizar e formalizar os requisitos funcionais de alto nível, servindo como um elo claro entre as necessidades dos usuários e as funcionalidades do sistema. Sua importância reside em fornecer uma compreensão concisa do escopo do projeto e das interações essenciais, facilitando a comunicação e o alinhamento entre as partes interessadas. Este diagrama foi desenvolvido utilizando a ferramenta Draw.io.

#### Atores Identificados:
O principal ator identificado no sistema é o **Usuário**. Este ator representa qualquer entidade humana que interage diretamente com as funcionalidades do sistema para gerenciar suas tarefas.

#### Casos de Uso e Funcionalidades:
O diagrama apresenta os seguintes casos de uso primários:
* **Gerenciar Tarefas:** Este é um caso de uso abrangente que encapsula as operações fundamentais de manipulação de tarefas. Ele inclui os seguintes casos de uso específicos, indicados pelo relacionamento `<<include>>`:
    * **Criar Tarefas:** Permite ao Usuário adicionar novas tarefas ao sistema.
    * **Visualizar Tarefas:** Habilita o Usuário a consultar a lista de tarefas existentes.
    * **Atualizar Tarefas:** Oferece ao Usuário a capacidade de modificar os detalhes de uma tarefa.
    * **Excluir Tarefas:** Permite ao Usuário remover tarefas do sistema.
* **Autenticar Usuário:** Este caso de uso gerencia o processo de acesso seguro ao sistema. Ele inclui:
    * **Fazer Login:** Permite ao Usuário acessar sua conta no sistema.
    * **Fazer Logout:** Permite ao Usuário encerrar sua sessão no sistema.
* **Registrar Usuário:** Este caso de uso permite que novos usuários criem uma conta no sistema, estabelecendo sua identidade para futuras interações.

#### Detalhes dos Relacionamentos `<<include>>`:
O relacionamento `<<include>>` denota que a execução do caso de uso "Gerenciar Tarefas" sempre incorpora o comportamento dos casos de uso incluídos, indicando uma dependência obrigatória para a completude da funcionalidade.
Similarmente, o relacionamento `<<include>>` aqui demonstra que a autenticação envolve intrinsecamente as operações de login e logout.

#### Conclusão:
O Diagrama de Casos de Uso fornece uma compreensão clara das fronteiras do sistema e das funcionalidades essenciais que ele oferece aos seus usuários. Ele serve como um ponto de partida para o detalhamento dos requisitos e para a subsequente modelagem da estrutura interna do sistema.

![Captura de tela 2025-07-01 162437](https://github.com/user-attachments/assets/876c132a-4cea-4c2a-9951-73d935ed7438)


### 8.2. Diagrama de Classes
O Diagrama de Classes é um dos diagramas estruturais da Unified Modeling Language (UML) utilizado para representar a estrutura estática de um sistema. Ele exibe as classes, seus atributos, operações (métodos) e os relacionamentos entre elas. **Para o Sistema de Gerenciamento de Tarefas, a criação deste diagrama foi essencial para modelar a arquitetura interna de dados e lógica, fornecendo uma visão detalhada das entidades fundamentais do sistema. Sua importância reside em formalizar a estrutura do código, facilitando o desenvolvimento, a manutenção e a compreensão da base de dados e das interações entre os componentes principais. Este diagrama foi desenvolvido utilizando a ferramenta Draw.io.**

#### Classes Identificadas:
O sistema é composto pelas seguintes classes principais:
* **Classe `Usuario`:**
  Esta classe representa os usuários do sistema, que interagem com as funcionalidades de gerenciamento de tarefas e autenticação.
  * **Atributos:**
    * `id: int`: Identificador único do usuário.
    * `nome: str`: Nome de usuário.
    * `senha_hash: str`: Representação segura (hash) da senha do usuário.
    * `email: str`: Endereço de e-mail do usuário.
  * **Operações:**
    * `__init__()`: Construtor da classe, responsável pela inicialização de um novo objeto `Usuario`.
    * `verificar_senha()`: Método para validar a senha fornecida pelo usuário.
    * `criar_tarefa()`: Método que permite ao usuário criar uma nova tarefa.
    * `listar_tarefas()`: Método que permite ao usuário visualizar as tarefas.

* **Classe `Tarefa`:**
  Esta classe representa uma tarefa individual dentro do sistema de gerenciamento.
  * **Atributos:**
    * `id: int`: Identificador único da tarefa.
    * `titulo: str`: Título descritivo da tarefa.
    * `descricao: str`: Detalhes adicionais sobre a tarefa.
    * `status: str`: Estado atual da tarefa (ex: "A Fazer", "Em Progresso", "Concluído").
    * `data_vencimento: str`: Data limite para a conclusão da tarefa.
  * **Operações:**
    * `Tarefa(titulo: str, descricao: str, data_vencimento: str)`: Construtor da classe, responsável pela inicialização de um novo objeto `Tarefa`.
    * `atualizar_status(novo_status: str)`: Método para modificar o estado da tarefa.
    * `obter_detalhes(): dict`: Método para retornar os detalhes completos da tarefa em formato de dicionário.

#### Relacionamentos:
O diagrama ilustra um relacionamento de **Associação** entre a classe `Usuario` e a classe `Tarefa`. Este relacionamento indica que um `Usuario` pode estar associado a várias `Tarefas`, enquanto uma `Tarefa` pode ser associada a um `Usuario`. A multiplicidade `1` no lado do `Usuario` e `0..*` no lado da `Tarefa` denota que um usuário pode possuir zero ou muitas tarefas. A seta de navegação indica que a classe `Usuario` tem conhecimento e pode interagir com as instâncias da classe `Tarefa`.

#### Conclusão:
O Diagrama de Classes oferece uma representação clara e detalhada da estrutura interna do Sistema de Gerenciamento de Tarefas. Ele serve como um blueprint para a implementação do código, garantindo a consistência na definição das entidades e suas interações, e facilitando a compreensão da arquitetura do software.

![Captura de tela 2025-07-01 170737](https://github.com/user-attachments/assets/264ab98b-fc28-431b-b9ee-6570137a030b)
