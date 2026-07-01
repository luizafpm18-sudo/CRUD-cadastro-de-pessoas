import sqlite3 as conector

try:
    conexao = conector.connect("Pessoal.db")

    cursor = conexao.cursor()

    comando = '''CREATE TABLE cadastro_de_pessoas(
    CPF varchar(11) not null,
    nome varchar(200) not null,
    data_de_nascimento varchar(12) not null,
    email varchar(50) not null,
    telefone varchar(11) not null,
    PRIMARY KEY(CPF)
    );
    '''

    cursor.execute(comando)
    conexao.commit()
    cursor.close()
    conexao.close()

except conector.DatabaseError as erro:
    print (erro)
