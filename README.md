# API Academia (Estilo SmartFit) 🏋️‍♂️

Uma API RESTful completa desenvolvida em Python e Django REST Framework para o gerenciamento de uma rede de academias. Este projeto foca exclusivamente no backend, modelando regras de negócio reais, desde o controle de planos e unidades até a autenticação customizada de alunos e o registro de acessos (catraca).

## 🚀 Tecnologias e Ferramentas

* **Python:** Linguagem base do projeto.
* **Django:** Framework web utilizado para a estruturação do backend, ORM e painel administrativo.
* **Django REST Framework (DRF):** Utilizado para a construção da API, serialização de dados e roteamento (ModelViewSets e Routers).
* **SQLite:** Banco de dados relacional padrão utilizado para desenvolvimento local.
* **Postman:** Ferramenta fundamental utilizada para testar as requisições (GET, POST) e validar o fluxo de dados em formato JSON.
* **Git:** Versionamento de código.

## ⚙️ Arquitetura de Dados (Models)

O banco de dados foi estruturado com relacionamentos utilizando `ForeignKeys` e proteção de integridade (`on_delete=PROTECT` e `CASCADE`). As principais entidades são:

1. **Unidade:** Representa as filiais físicas da academia.
2. **Plano:** Pacotes de assinatura disponíveis (ex: Plano Black).
3. **Aluno (Custom User):** O cliente da academia. O sistema de autenticação padrão do Django foi reescrito (herdando de `AbstractUser`) para utilizar o **E-mail** como chave principal de login no lugar do `username`.
4. **Ficha de Treino:** Rotina de exercícios atrelada a um aluno específico.
5. **Registro de Acesso:** Simula a catraca da academia, gerando um log automático com data e hora (`auto_now_add=True`) sempre que um aluno acessa uma unidade.

## 🔒 Segurança

* **Criptografia de Senhas:** A criação de alunos via API foi customizada no `serializers.py` para garantir que as senhas sejam submetidas a algoritmos de hash antes de serem salvas no banco.
* **Ocultação de Dados Sensiveis:** Utilização do parâmetro `'write_only': True` para garantir que o backend nunca retorne a senha do usuário nas respostas JSON.

## 🌐 Endpoints da API

A API está roteada sob o caminho base `/api/`. Todos os endpoints suportam operações CRUD padrão (GET, POST, PUT, PATCH, DELETE).

| Endpoint | Método | Descrição |
| :--- | :--- | :--- |
| `/api/unidades/` | GET, POST | Lista ou cria unidades da academia |
| `/api/planos/` | GET, POST | Lista ou cria planos de assinatura |
| `/api/alunos/` | GET, POST | Lista ou cadastra novos alunos |
| `/api/fichas/` | GET, POST | Gerencia as fichas de treino |
| `/api/acessos/` | GET, POST | Registra ou lista os acessos na catraca |

## 💻 Como rodar o projeto localmente

Siga os passos abaixo para testar o projeto na sua máquina:

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git](https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git)
   cd SEU_REPOSITORIO
