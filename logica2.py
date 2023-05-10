print('Bem vindo a Lanchonete do Victor Camilo da Luz')         
print('*********cardapio*************')
print(""" 
100   Cachorro Quente                    9,00
101   Cachorro-Quente Duplo              11,00
102   X-Egg                              12,00
103   X-Salada                           13,00
104   X-Bacon                            14,00
105   X-Tudo                             17,00
200   Refrigerante Lata                  5,00
201   Chá Gelado                         4,00
""")

ped = 0

while True:
    cod = int(input('Digite o codigo Desejado : '))

    if cod == 100: 
        print('Você pediu um Cachorro Quente no valor de 9,00')
        ped += 9
    elif cod == 101:
        print('Você pediu um Cachorro Quente Duplo no valor de 11,00')
        ped += 11
    elif cod == 102:
        print('Você pediu um X-Egg no valor de 12,00')
        ped += 12
    elif cod == 103:
        print('Você pediu um X-Salada no valor de 13,00')
        ped += 13
    elif cod == 104:
        print('Você pediu um X-Bacon no valor de 14,00')
        ped += 14
    elif cod == 105:
        print('Você pediu um X-Tudo no valor de 17,00')  
        ped += 17
    elif cod == 200:
        print('Você pediu um Refrigerante Lata no valor de 5,00')
        ped += 5
    elif cod == 201:
        print('Você pediu um Chá Gelado no valor de 4,00')
        ped += 4
    else:
        print('Opção Invalida, digite uma das opções')
        continue

    segundo_pedido = input('Deseja fazer um segundo pedido? (S/N) ')
    if segundo_pedido.upper() == 'S':
        continue
    else:
        break
print(f'O valor total do pedido é de R${ped:.2f}')
