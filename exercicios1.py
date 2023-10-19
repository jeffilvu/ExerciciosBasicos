"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

num = input("digite um numero inteiro\n")

if num.isdigit:

    try:
        num = int(num)
        if num % 2 == 0:
            print("o numero digitado é par")
        else:
            print("o numero digitado é impar")
    except:
        print("seu numero não é inteiro")




"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# horario = input("Digite o horario neste formato 00:00\n")
# horarioreplace = horario.replace(':','.')
# horario = float(horarioreplace)
# if horario >= 0 and horario <= 11:
#     print("bom dia")
# elif horario >= 12 and horario <= 17:
#     print("boa tarde")
# else:
#     print("boa noite")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input("digite o seu nome\n")

letras = len(nome)


if letras == 4:
    print("seu nome é curto")

elif letras == 5 or letras == 6:

    print("Seu nome é normal")

else:

    print("seu nome é mto grande")


