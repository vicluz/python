#cadastrar uma peças
def cadastrarPeca(codigo):
    nome = input("Digite o nome da peça: ")
    fabricante = input("Digite o fabricante da peça: ")
    valor = float(input("Digite o valor da peça: "))

    peca = {
        "Código": codigo,
        "Nome": nome,
        "Fabricante": fabricante,
        "Valor": valor
    }

    return peca

#consultar peças
def consultarPeca(pecas):
    while True:
        print("\nMenu de Consulta:")
        print("1) Consultar Todas as Peças")
        print("2) Consultar Peças por Código")
        print("3) Consultar Peças por Fabricante")
        print("4) Retornar")

        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1:
            print("\nTodas as Peças:")
            for peca in pecas:
                print(peca)
        elif opcao == 2:
            codigo = int(input("\nDigite o código da peça: "))
            for peca in pecas:
                if peca["Código"] == codigo:
                    print("\nPeça encontrada:")
                    print(peca)
                    break
            else:
                print("\nPeça não encontrada.")
        elif opcao == 3:
            fabricante = input("\nDigite o fabricante da peça: ")
            print("\nPeças do fabricante", fabricante + ":")
            encontradas = False
            for peca in pecas:
                if peca["Fabricante"].lower() == fabricante.lower():
                    print(peca)
                    encontradas = True
            if not encontradas:
                print("Nenhuma peça encontrada desse fabricante.")
        elif opcao == 4:
            break
        else:
            print("Opção inválida. Digite novamente.")

#remover uma peça
def removerPeca(pecas):
    codigo = int(input("Digite o código do produto que deseja remover: "))
    for i, peca in enumerate(pecas):
        if peca["Código"] == codigo:
            pecas.pop(i)
            print("Peça removida com sucesso.")
            break
    else:
        print("Peça não encontrada.")


pecas = []
contador = 1

while True:
    print("\nMenu:")
    print("1) Cadastrar Peça")
    print("2) Consultar Peça")
    print("3) Remover Peça")
    print("4) Sair")

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        nova_peca = cadastrarPeca(contador)
        pecas.append(nova_peca)
        contador += 1
        print("\nPeça cadastrada com sucesso.")
    elif opcao == 2:
        consultarPeca(pecas)
    elif opcao == 3:
        removerPeca(pecas)
    elif opcao == 4:
        break
    else:
        print("Opção inválida. Digite novamente.")


