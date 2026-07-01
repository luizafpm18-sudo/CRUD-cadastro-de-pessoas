# Cadastro de Pessoas

Sistema simples de cadastro de pessoas desenvolvido em Python, com interface
gráfica feita em Tkinter e banco de dados SQLite.

## Funcionalidades

- Cadastrar nova pessoa (CPF, nome, data de nascimento, email, telefone)
- Atualizar dados de um cadastro existente
- Excluir cadastro
- Listar registros em tabela, com paginação

## Tecnologias

- Python 3
- Tkinter (interface gráfica)
- SQLite3 (banco de dados)

## Como executar

1. Certifique-se de ter o Python 3 instalado.
2. Clone este repositório:
   ```bash
   git clone https://github.com/luizafpm18-sudo/CRUD-cadastro-de-pessoas.git
   ```
3. Na primeira vez, crie o banco de dados executando:
   ```bash
   python criarbd.py
   ```
4. Depois, execute o programa principal:
   ```bash
   python principalpessoal.py
   ```

## Estrutura do projeto

- `principalpessoal.py` — arquivo principal, inicia a janela da aplicação
- `cadastrodepessoas.py` — contém a classe `CadastroPessoas`, com toda a
  lógica de cadastro, atualização, exclusão e listagem de registros
- `criarbd.py` — script que cria o banco de dados `Pessoal.db` e a tabela
  `cadastro_de_pessoas` (deve ser executado uma única vez, antes do primeiro
  uso do sistema)
