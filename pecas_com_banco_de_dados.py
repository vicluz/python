import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="seu_usuario",
    password="sua_senha",
    database="seu_banco_dados"

)

cursor = conn.cursor()

# Criar tabelas
cursor.execute('''
CREATE TABLE IF NOT EXISTS fabricantes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS categorias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS pecas (
    codigo INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255),
    fabricante_id INT,
    categoria_id INT,
    valor FLOAT,
    FOREIGN KEY (fabricante_id) REFERENCES fabricantes(id),
    FOREIGN KEY (categoria_id) REFERENCES categorias(id)
)
''')

conn.commit()

# Função para cadastrar um fabricante
def cadastrarFabricante():
    try:
        nome = input("Digite o nome do fabricante: ")
        cursor.execute("INSERT INTO fabricantes (nome) VALUES (%s)", (nome,))
        conn.commit()
        print("\nFabricante cadastrado com sucesso.")
    except ValueError:
        print("Erro ao cadastrar o fabricante.")

# Função para cadastrar uma categoria
def cadastrarCategoria():
    try:
        nome = input("Digite o nome da categoria: ")
        cursor.execute("INSERT INTO categorias (nome) VALUES (%s)", (nome,))
        conn.commit()
        print("\nCategoria cadastrada com sucesso.")
    except ValueError:
        print("Erro ao cadastrar a categoria.")

# Função para cadastrar uma peça
def cadastrarPeca():
    try:
        nome = input("Digite o nome da peça: ")
        fabricante_id = int(input("Digite o ID do fabricante: "))
        categoria_id = int(input("Digite o ID da categoria: "))
        valor = float(input("Digite o valor da peça: "))

        cursor.execute("INSERT INTO pecas (nome, fabricante_id, categoria_id, valor) VALUES (%s, %s, %s, %s)",
                       (nome, fabricante_id, categoria_id, valor))
        conn.commit()

        print("\nPeça cadastrada com sucesso.")
    except ValueError:
        print("Erro ao cadastrar a peça.")

# Função para consultar todas as peças cadastradas
def consultarTodasPecas():
    cursor.execute("SELECT p.codigo, p.nome, f.nome AS fabricante, c.nome AS categoria, p.valor FROM pecas p "
                   "INNER JOIN fabricantes f ON p.fabricante_id = f.id "
                   "INNER JOIN categorias c ON p.categoria_id = c.id")
    results = cursor.fetchall()

    if results:
        print("\nTodas as Peças Cadastradas:")
        print("Código | Nome da Peça | Fabricante | Categoria | Valor")
        for result in results:
            print(f"{result[0]:6} | {result[1]:13} | {result[2]:11} | {result[3]:10} | {result[4]:.2f}")
    else:
        print("Nenhuma peça cadastrada.")

# Função para remover uma peça
def removerPeca():
    try:
        codigo = int(input("Digite o código da peça que deseja remover: "))
        cursor.execute("DELETE FROM pecas WHERE codigo=%s", (codigo,))
        conn.commit()
        print("Peça removida com sucesso.")
    except ValueError:
        print("Digite apenas valores numéricos.")
    except mysql.connector.Error as err:
        print(f"Erro ao remover a peça: {err}")

# Função para atualizar o valor de uma peça
def atualizarValorPeca():
    try:
        codigo = int(input("Digite o código da peça que deseja atualizar: "))
        novo_valor = float(input("Digite o novo valor da peça: "))

        cursor.execute("UPDATE pecas SET valor=%s WHERE codigo=%s", (novo_valor, codigo))
        conn.commit()

        print("Valor da peça atualizado com sucesso.")
    except ValueError:
        print("Digite apenas valores numéricos.")

# Loop principal
while True:
    try:
        print("\nMenu:")
        print("1) Cadastrar Fabricante")
        print("2) Cadastrar Categoria")
        print("3) Cadastrar Peça")
        print("4) Consultar Todas as Peças Cadastradas")
        print("5) Atualizar Valor da Peça")
        print("6) Remover Peça")
        print("7) Sair")

        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1:
            cadastrarFabricante()
        elif opcao == 2:
            cadastrarCategoria()
        elif opcao == 3:
            cadastrarPeca()
        elif opcao == 4:
            consultarTodasPecas()
        elif opcao == 5:
            atualizarValorPeca()
        elif opcao == 6:
            removerPeca()
        elif opcao == 7:
            break
        else:
            print("Opção inválida. Digite novamente.")
    except ValueError:
        print("Digite apenas valores numéricos.")

# Fechar a conexão com o banco de dados
conn.close()