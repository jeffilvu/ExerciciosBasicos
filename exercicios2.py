# iterando strings com while
#      012345678910

import random
import string

senha= input('digite sua senha:\n ') 
#     -11...

indice = 0
nova_senha = ''
senhaEscondida = ''
while indice < len(senha):
    aleatorio = random.choice(string.ascii_letters)
    letra = senha[indice]
    nova_senha += f'{aleatorio}{letra}'
    indice+=1
    senhaEscondida = nova_senha[::-1]


print(f'Senha escondida: {senhaEscondida}')
