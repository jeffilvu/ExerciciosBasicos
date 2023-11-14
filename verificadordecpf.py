"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""

"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10
Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0
Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O primeiro dígito do CPF é 7
"""
multp = 10
somaDigitos=0
primeiroDigito = 0
segundoDigito = 0


while True:
    cpf = input("digite o cpf sem traços e pontos: \n")
    noveDigitos = cpf[0:9]
    primeiraEntrada = cpf[0]
    if cpf == primeiraEntrada * len(cpf):
        print("cpf invalido!!\n")
        continue
    else:
        # print("Primeiro Digito: \n")
        try:
            for digito in noveDigitos:
                    digito = int(digito);
                    digitoMultiplicado = digito*multp
                    # print(f'{digitoMultiplicado}')
                    multp = multp-1
                    somaDigitos = somaDigitos + digitoMultiplicado
                    somaDigitosMultiplicado = somaDigitos * 10
                    primeiroDigito = somaDigitosMultiplicado % 11
            break

        except:
            print(f'digite apenas numeros no cpf\n')
            continue



if primeiroDigito > 9:
    primeiroDigito = 0
    # print(f"O primeiro digito é {primeiroDigito}\n")

# else:

#     print(f"O primeiro digito é {primeiroDigito}\n")

primeiroDigito = str(primeiroDigito)
dezDigitos = noveDigitos + primeiroDigito
multp = 11
somaDigitos = 0

# print("Segundo digito: \n")

for digito in dezDigitos:
        digito = int(digito);
        digitoMultiplicado = digito*multp
        # print(f'{digitoMultiplicado}')
        multp = multp-1
        somaDigitos = somaDigitos + digitoMultiplicado
        somaDigitosMultiplicado = somaDigitos * 10
        segundoDigito = somaDigitosMultiplicado % 11

if segundoDigito > 9:
    segundoDigito = 0
    # print(f"O segundo digito é {segundoDigito}")

# else:

#     print(f"O segundo digito é {segundoDigito}\n")

cpfCalculado = noveDigitos + str(primeiroDigito) + str(segundoDigito)

if cpf == cpfCalculado:
    print("cpf valido!")
else:
     print("cpf invalido!!")
     