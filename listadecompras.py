"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os

listaDeCompras = []
while True:
    funcao = input("Selecione uma opção\n[i]nserir [a]pagar [l]istar: ")

    if funcao == 'i':
        os.system('cls')
        add = input('digite o nome do produto a ser adicionado: ')
        listaDeCompras.append(add)
        print(f'o item {add} foi adicionado a lista de compras')

    elif funcao == 'l':
        os.system('cls')
        if len(listaDeCompras) == 0:
            print("Você não adicionou nada na lista")
        for i, item in enumerate(listaDeCompras):
            print(i, item)

    elif funcao == 'a':
        os.system('cls')
        print('Selecione o item que deseja excluir: ')
        for i, item in enumerate(listaDeCompras):
            print(i, item)
            if len(listaDeCompras) == i + 1:
                print('[C] para cancelar')
        excluir = input('digite o valor: ')
        if excluir == 'C':
            continue
        try:
            excluir = int(excluir)
            del listaDeCompras[excluir]
            print('ITEM EXCLUIDO!')
            for i, item in enumerate(listaDeCompras):
                print(i, item)
        except TypeError:
            print('Digite apenas o índice do produto na lista')
            
        except IndexError:
            print('O valor digitado não existe na lista')

