"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

listaDeCompras = []
while True:
    funcao = input("Selecione uma opção\n[i]nserir [a]pagar [l]istar: ")

    if funcao == 'i':

        add = input('digite o nome do produto a ser adicionado: ')
        listaDeCompras.append(add)
        print(f'o item {add} foi adicionado a lista de compras')

    elif funcao == 'l':
        indice = 0
        for item in listaDeCompras:
            print(indice, item)
            indice +=1

    elif funcao == 'a':
        indice = 0
        print('selecione o item que deseja excluir: ')
        for item in listaDeCompras:
            print(indice,item)
            indice+=1
        excluir = input('digite o numero: ')
        excluir = int(excluir)
        del listaDeCompras[excluir]
        indice = 0
        print('ITEM EXCLUIDO!')
        for item in listaDeCompras:
            print(indice,item)
            indice+=1





