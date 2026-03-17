# 🔐 Auth System

Sistema de autenticação de usuários desenvolvido em Python, utilizando conceitos de **Programação Orientada a Objetos (POO)**, banco de dados **SQLite** e hash seguro de senhas com **hashlib**.

## 📋 Funcionalidades

- Cadastro de usuários com validação de username, email e senha
- Hash de senha com salt aleatório (SHA-256)
- Login com limite de **3 tentativas**
- Área logada com visualização de dados do usuário

## 🗂️ Estrutura do Projeto

```
auth-system/
├── main.py                  # Ponto de entrada da aplicação
├── database/
│   ├── __init__.py
│   └── db.py                # Conexão e criação do banco SQLite
├── models/
│   ├── __init__.py
│   └── user.py              # Classe User
├── services/
│   ├── __init__.py
│   ├── auth_service.py      # Hash, verificação de senha e login
│   └── user_service.py      # Cadastro e busca de usuários
└── utils/
    ├── __init__.py
    └── validators.py        # Validações de email, senha e username
```

## 🚀 Como executar

**Pré-requisitos:** Python 3.8+

Clone o repositório:
```bash
git clone https://github.com/Kizuypy/auth-system.git
cd auth-system
```

Execute o projeto:
```bash
python main.py
```

> Nenhuma dependência externa necessária. O projeto utiliza apenas a biblioteca padrão do Python.

## 🔒 Segurança

- Senhas nunca são salvas em texto puro
- Cada senha recebe um **salt** aleatório de 32 bytes antes do hash
- Algoritmo utilizado: **SHA-256**
- Proteção contra tentativas excessivas de login (bloqueio após 3 erros)

## 🛠️ Tecnologias

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)

- Python 3
- SQLite3
- Hashlib
- POO (Programação Orientada a Objetos)

## 👤 Autor

Feito por [Vinicius](https://github.com/Kizuypy)
