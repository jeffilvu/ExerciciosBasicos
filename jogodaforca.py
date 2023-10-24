"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import random

palavras = ['legal','diferente','talvez']
palavrasecreta = random.choice(palavras)
palavradigitada = '*' * len(palavrasecreta)
tentativas = 0

while palavrasecreta != palavradigitada:
    tentativas += 1
    print(palavradigitada)

    letra = input('digite uma letra: ')
    if len(letra) != 1:
        print('Por favor digite apenas uma letra')
        continue

    if letra in palavrasecreta:
       
       for i in range(len(palavrasecreta)):

            if letra == palavrasecreta[i]:
                palavradigitada = palavradigitada[:i] + letra + palavradigitada[i + 1:]    
                
    else:
        print('esta letra não está na palavra secreta')

print(f'parabéns voce descobriu a palavra {palavradigitada} em {tentativas} tentativas')
                


