#  Gestão Pro

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Interface-Terminal-black?style=for-the-badge&logo=windowsterminal&logoColor=white"/>
</p>

<p align="center">
  <strong>Sistema de gerenciamento de funcionários desenvolvido em Python.</strong>
</p>

<p align="center">
  Controle funcionários, tarefas, turnos e registro de ponto através de uma aplicação simples e organizada.
</p>

---

##  Sobre o projeto

O **Gestão Pro** é um sistema de gerenciamento de funcionários desenvolvido em **Python**, executado diretamente pelo terminal.

A aplicação possui dois níveis de acesso:

*  **Funcionário**
*  **RH**

Cada perfil possui funcionalidades específicas para gerenciamento de colaboradores, tarefas e controle de ponto.

O projeto foi desenvolvido com foco na prática de **lógica de programação, funções, estruturas de dados, condicionais, loops e tratamento de exceções**.

---

##  Funcionalidades

###  Área do Funcionário

| Funcionalidade | Descrição                                 |
| -------------- | ----------------------------------------- |
|  Login       | Acesso através do nome cadastrado         |
|  Entrada     | Registro automático do horário de entrada |
|  Saída       | Registro do horário de saída              |
|  Tarefas     | Visualização das tarefas atribuídas       |
|  Conclusão    | Marcação de tarefas como concluídas       |
|  Informações | Visualização dos dados do funcionário     |
|  Bloqueio    | Impede acesso de funcionários removidos   |

###  Área do RH

| Funcionalidade          | Descrição                                 |
| ----------------------- | ----------------------------------------- |
|  Login administrativo | Acesso protegido por usuário e senha      |
|  Cadastro              | Adição de novos funcionários              |
|  Remoção              | Bloqueio de funcionários ativos           |
|  Listagem             | Visualização dos funcionários cadastrados |
|  Tarefas              | Criação de novas tarefas                  |
|  Atribuição           | Tarefas individuais ou para todos         |
|  Turnos               | Alteração do turno dos funcionários       |

---

##  Regras do sistema

O sistema possui algumas regras para controlar o fluxo de trabalho:

```text
┌──────────────────────────────────────────────┐
│              FLUXO DO FUNCIONÁRIO           │
├──────────────────────────────────────────────┤
│                                              │
│  Login                                       │
│    ↓                                         │
│  Entrada registrada                          │
│    ↓                                         │
│  Visualizar tarefas                          │
│    ↓                                         │
│  Concluir tarefas                            │
│    ↓                                         │
│  Verificação de tarefas pendentes            │
│    ↓                                         │
│  Saída registrada                            │
│                                              │
└──────────────────────────────────────────────┘
```

###  Regra principal

O funcionário **não pode registrar a saída enquanto possuir tarefas pendentes**.

Isso é verificado automaticamente pelo sistema antes do registro do ponto.

---

##  Tecnologias

<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
</p>

### Bibliotecas utilizadas

* `datetime` → registro de data e horário
* `time` → controle de pausas no sistema

### Conceitos utilizados

*  Funções
*  Listas
*  Dicionários
*  Condicionais
*  Loops
*  `try/except`
*  Busca de dados
*  Manipulação de informações
*  Data e hora

---

##  Estrutura

```text
Gestao-Pro/
│
├── Código colado.py
│
└── README.md
```

---

## 🚀 Como executar

###  Clone o repositório

```bash
git clone (https://github.com/pedroluizeto631-ops/GESTAO-PRO)
```

###  Entre na pasta

```bash
cd Gestao-Pro
```

###  Execute o programa

```bash
python "gestaopro.py"
```

>  Dependendo do seu sistema, pode ser necessário utilizar `python3`.

---

##  Login administrativo

Para acessar a área do RH:

```text
Usuário: admin
Senha: 1234
```

>  Essas credenciais estão definidas diretamente no código e existem apenas para fins de desenvolvimento.

---

##  Demonstração

###  Menu principal

```text
=============================================
              GESTÃO PRO
=============================================

Sistema de gerenciamento de funcionários

[1] Funcionário
[2] RH
[3] Sair

> Escolha uma opção:
```

###  Menu do funcionário

```text
=============================================
        MENU DOS FUNCIONÁRIOS
=============================================

[1] Bater ponto
[2] Ver tarefas
[3] Info
[4] Sair
```

###  Menu do RH

```text
========================================
             MENU DO RH
========================================

[1] Adicionar funcionário
[2] Remover funcionário
[3] Criar tarefa
[4] Modificar turno
[5] Ver funcionários
[6] Sair
```

---

## 🔄 Fluxo de tarefas

```text
             🧑‍💼 RH
               │
               ▼
         Criar tarefa
               │
       ┌───────┴───────┐
       ▼               ▼
   👥 Todos        👤 Funcionário
       │               │
       └───────┬───────┘
               ▼
         Tarefa pendente
               │
               ▼
        Funcionário
               │
               ▼
        Concluir tarefa
               │
               ▼
         Registrar saída
```

---

##  Próximas versões

O projeto ainda está em desenvolvimento e pode receber diversas melhorias:

* [ ]  Persistência de dados
* [ ]  Integração com banco de dados
* [ ]  Sistema de autenticação mais seguro
* [ ]  Interface gráfica
* [ ]  Dashboard administrativo
* [ ]  Histórico de ponto
* [ ]  Relatórios
* [ ]  Separação do projeto em módulos
* [ ]  Programação Orientada a Objetos
* [ ]  Versão Web
* [ ]  API para integração com outros sistemas

---

##  Objetivo

O principal objetivo do **Gestão Pro** é transformar conceitos de programação em um projeto funcional.

O sistema serve como prática para desenvolver habilidades em:

```text
Lógica
  ↓
Estruturas de dados
  ↓
Funções
  ↓
Validação
  ↓
Tratamento de erros
  ↓
Organização de código
  ↓
Projetos maiores
```

---

##  Desenvolvedor

<p align="center">
  <strong>Pedro Luizeto</strong>
</p>

<p align="center">
  Projeto desenvolvido como parte da evolução nos estudos de programação.
</p>

---

<p align="center">
   Se este projeto foi útil ou interessante para você, considere deixar uma estrela no repositório!
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Made%20with-❤️-red?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Powered%20by-Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
</p>
