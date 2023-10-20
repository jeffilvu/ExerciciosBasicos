# clculadora com o while

sair = "n"

while sair == "n":

    num1 = input("digite o primeiro valor: ")
    num2 = input("digite o segundo valor: ")
    operador = input("digite o operador (/, * , -, +): ")
    num1 = float(num1)
    num2 = float(num2)
    while operador == "/":

        resultado = num1/num2
        break

    while operador == "*":

        resultado = num1*num2
        break

    while operador == "+":
        resultado = num1+num2
        break

    while operador == "-":
        resultado = num1-num2
        break

    print(resultado)
    sair = input("deseja sair? \"s\" ou \"n\": ")


