# clculadora com o while

sair = "n"
resultado = ''



while sair == "n":
        
    num1 = input("digite o primeiro valor: ")
    num2 = input("digite o segundo valor: ")
    operador = input("digite o operador (/, * , -, +): ")

    try:
        num1 = float(num1)
        num2 = float(num2)
        numvalidos = True

    except:
        numvalidos = False

    if numvalidos:

        if operador == "/":

            resultado = num1/num2
                    

        elif operador == "*":

            resultado = num1*num2
                        

        elif operador == "+":
            resultado = num1+num2
                        

        elif operador == "-":
            resultado = num1-num2

        print(resultado)
                  
    else:
        print("algum numero digitado é invalido")
        sair = "n"

    sair = input("deseja sair? \"s\" ou \"n\": ")

    while sair != "n" and sair != "s":
        sair = input("deseja sair? \"s\" ou \"n\": ")
