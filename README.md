
# 📚 Cadastro de Alunos

Projeto em Python que permite cadastrar alunos com três notas, calcular a média e realizar consultas e listagens.

---

## 🎯 Objetivo

Este sistema foi criado para praticar os fundamentos da linguagem Python, como:

- Variáveis e tipos de dados  
- Funções  
- Estruturas de repetição e condição  
- Modularização de código  
- Validação de entradas do usuário  
- Limpeza de terminal (cross-platform)  
- Organização de projeto

---

## 🛠 Funcionalidades

- ✅ Cadastrar aluno com nome e 3 notas  
- ✅ Calcular a média das notas  
- ✅ Consultar aluno pelo nome  
- ✅ Listar todos os alunos cadastrados  
- ✅ Menu interativo com opções de navegação  
- ✅ Validações de entrada (notas entre 0 e 10, nome não vazio)

---

## 🗂 Estrutura de Pastas

```
cadastro-alunos-cli/
├── main.py
├── README.md
├── .gitignore
├── .venv/
└── app/
    ├── util.py         # Funções auxiliares (limpeza de tela, menus)
    ├── menu.py         # Menu principal e navegação
    ├── cadastro.py     # Lógica de cadastro
    ├── consulta.py     # Consulta individual
    ├── listagem.py     # Listagem completa
    └── validador.py    # Validações de nome e nota
```

---

## ▶️ Como executar

1. Clone o repositório:

```bash
git clone https://github.com/QueliHV/Cadastro-Alunos-CLI.git
cd Cadastro-Alunos-CLI
```

2. (Opcional) Crie e ative um ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate  # Para Mac/Linux
```

3. Execute o programa:

```bash
python3 app/main.py
```

---

## 🚧 Próximos passos

Este projeto será incrementado conforme o avanço nos estudos:

- [ ] Salvamento em arquivos `.txt`, `.csv`, `.json`  
- [ ] Orientação a objetos (classe `Aluno`)  
- [ ] Integração com banco de dados (SQLite)  
- [ ] Interface Web ou API para consulta externa  

---

## 👩‍💻 Autora

Desenvolvido por [Queli Hesper](https://www.linkedin.com/in/quelihesper/) 💡

---
