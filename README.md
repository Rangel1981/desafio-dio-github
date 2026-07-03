# 💰 Hub de Finanças Pessoais com Insights Inteligentes

Este projeto é uma API RESTful moderna desenvolvida como o desafio final de encerramento do Bootcamp na **DIO (Digital Innovation One)**. A aplicação consiste em um sistema de gerenciamento financeiro pessoal que armazena transações (receitas e despesas) e utiliza **Programação Orientada a Objetos (POO)** para gerar insights automáticos sobre a saúde financeira do usuário.

O projeto foi desenvolvido utilizando o **GitHub Copilot** como parceiro de *pair programming*, acelerando a estruturação das camadas e auxiliando na resolução de bugs de validação do Pydantic.

---

## 🚀 Tecnologias Utilizadas

* **Python 3.10+**
* **FastAPI**: Framework web moderno e de alta performance.
* **SQLAlchemy**: ORM para mapeamento objeto-relacional.
* **Pydantic v2**: Validação de dados e tipagem estrita.
* **SQLite**: Banco de dados relacional local e leve.
* **Uvicorn**: Servidor ASGI para rodar a aplicação.
* **GitHub Copilot**: Assistente de IA para ganho de produtividade.

---

## 🏗️ Arquitetura do Projeto

O projeto foi estruturado seguindo o padrão de desenvolvimento por **camadas**, garantindo a separação de responsabilidades (Clean Architecture):

```text
src/
├── database/     # Configuração e gerenciamento da sessão do banco de dados (SQLite)
├── models/       # Modelos do SQLAlchemy (Representação das tabelas em POO)
├── schemas/      # Schemas do Pydantic (Validação de entrada e saída de dados)
├── services/     # Regras de negócio isoladas (Cálculos e geração de insights)
└── main.py       # Ponto de entrada da aplicação e definição das rotas/endpoints