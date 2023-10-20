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



        else:
            print("algum numero digitado é invalido")
            sair = "n"

        print(resultado)
        sair = input("deseja sair? \"s\" ou \"n\": ")
