print('Bem Vindo a empresa logistica do Victor Camilo da luz (4120125)')

def dimensoesObjeto():
    while True:
        try:
            alt = float(input("Digite a altura do objeto (em cm): "))
            
            comprimento = float(input("Digite o comprimento do objeto (em cm): "))
           
            larg = float(input("Digite a largura do objeto (em cm): "))
            
            vol = alt * comprimento * larg
            if vol <= 1000:
                return 10
            elif 1001 <= vol <= 10000:
                return 20
            elif 10001 <= vol <= 30000:
                return 30
            elif 30001 <= vol <= 100000:
                return 50
            else:
                print("As dimensões do objeto estão fora dos limites aceitos (até 100000 cm³).")
        except ValueError:
            print("Digite apenas valores numéricos.")
            


def pesoObjeto():
    while True:
        try:
            peso = float(input("Digite o peso do objeto (em kg): "))
            if peso <= 0.1:
                return 1
            elif 0.11 <= peso <= 1:
                return 1.5
            elif 1.1 <= peso <= 10:
                return 2
            elif 10.1 <= peso <= 30:
                return 3
            else:
                print("O peso do objeto está fora dos limites aceitos (até 30 kg).")
        except ValueError:
            print("Digite apenas valores numéricos")
            


def rotaObjeto():
    while True:
        try:
            rota = input("Digite a rota do objeto (RS, SR, BS, SB, BR ou RB): ").upper()
            if rota == "RS" or rota == "SR":
                return 1
            elif rota == "BS" or rota == "SB":
                return 1.2
            elif rota == "BR" or rota == "RB":
                return 1.5
            else:
                print("A rota digitada não está na tabela de rotas aceitas.")
        except ValueError:
            print("Digite apenas as siglas das cidades para a rota do objeto.")
            


dimensoes = dimensoesObjeto()
peso = pesoObjeto()
rota = rotaObjeto()
total = dimensoes * peso * rota
print("O valor total a ser pago é de R$  {:.2f}".format(total))