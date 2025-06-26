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

*(Esta seção será preenchida posteriormente, com os diagramas de Casos de Uso e Classes.)*
