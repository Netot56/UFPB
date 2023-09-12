Quest= int(input("Digite a questão: "))

def switch_case(Quest):
    if Quest == 1:
        Raio= float(input("Digite o raio do círculo: "))
        Area= 3.14*(Raio*Raio)

        print(f"A area do círculo de raio {Raio} é : {Area}")
    elif Quest ==2:
        while True:
            altura = float(input("Digite a sua altura: "))
            genero = input("Dgigte o seu genero biologio(M/F): ")
            if(genero=="m" or genero=="M"):
                PesoI=(72.7*altura)-58
                break
            elif(genero=="f" or genero=="F"):
                PesoI= (62.1*altura)-44.7
                break
            else:
                print("Erro na digitação..... Tente novamente")
        print(PesoI)
    elif Quest ==3:
        valor_por_hora = float(input("Informe o valor ganho por hora: "))
        horas_trabalhadas = float(input("Informe o número de horas trabalhadas no mês: "))

        # Calcula o salário bruto
        salario_bruto = valor_por_hora * horas_trabalhadas

        # Calcula os descontos
        imposto_de_renda = 0.11 * salario_bruto
        inss = 0.08 * salario_bruto
        sindicato = 0.05 * salario_bruto

        # Calcula o salário líquido
        salario_liquido = salario_bruto - imposto_de_renda - inss - sindicato

        # Exibe os resultados
        print(f"Salário Bruto: R${salario_bruto:.2f}")
        print(f"Desconto Imposto de Renda(11%): R${imposto_de_renda:.2f}")
        print(f"Desconto INSS(8%): R${inss:.2f}")
        print(f"Desconto Sindicato(5%): R${sindicato:.2f}")
        print(f"Salário Líquido: R${salario_liquido:.2f}")
    elif Quest ==4:
        turno = input("Digite o turno em que você estuda (m - Manhã, v - Tarde, n - Noite): ")

        # Converte a entrada do usuário para minúsculas para facilitar a comparação
        turno = turno.lower()

        # Verifica o turno e exibe a mensagem apropriada
        if turno == 'm':
            print("Bom dia!")
        elif turno == 'v':
            print("Boa tarde!")
        elif turno == 'n':
            print("Boa noite!")
        else:
            print("Valor inválido. Por favor, digite 'm', 'v' ou 'n' para o turno.")
    elif Quest ==5:
        l1 = float(input("Digite o comprimento do primeiro lado do triângulo: "))
        l2 = float(input("Digite o comprimento do segundo lado do triângulo: "))
        l3 = float(input("Digite o comprimento do terceiro lado do triângulo: "))

        # Verifica a classificação do triângulo
        if l1 == l2 == l3:
            print("O triângulo é equilátero.")
        elif l1 == l2 or l1 == l3 or l2 == l3:
            print("O triângulo é isósceles.")
        else:
            print("O triângulo é escaleno.")
    elif Quest ==6:
        nota1 = float(input("Digite a primeira nota parcial: "))
        nota2 = float(input("Digite a segunda nota parcial: "))

        # Calcula a média das notas
        media = (nota1 + nota2) / 2

        # Exibe a média na tela
        print(f"A média das notas é: {media:.2f}")
        if(9>media<10):
            print("Conceito A")
        elif(7.5>media<9):
            print("Conceito B")
        elif(6>media<7.5):
            print("Conceito C")
        elif(4>media<6):
            print("Conceito D")
        elif(4>media<0):
            print("Conceito E")
    elif Quest ==7:
        valor_produto = float(input("Digite o valor do produto: "))
        forma_pagamento = input("Digite a forma de pagamento (dinheiro ou cheque): ")

        # Verifica se o cliente tem direito a desconto
        if valor_produto >= 100 and forma_pagamento.lower() == "dinheiro":
            desconto = 0.10 * valor_produto
        else:
            desconto = 0.0  # Nenhum desconto

        # Calcula o valor final a ser pago
        valor_final = valor_produto - desconto

        # Exibe o valor final a ser pago
        print(f"Valor a ser pago: R${valor_final:.2f}")
    elif Quest ==8:

        valor_produto = float(input("Digite o valor do produto: "))
        forma_pagamento = input("Digite a forma de pagamento (dinheiro, cheque, débito, crédito): ")

        # Verifica se o cliente tem direito a desconto
        desconto = 0.0
        if valor_produto >= 100 and forma_pagamento.lower() == "dinheiro":
            desconto = 0.10 * valor_produto

        # Calcula o valor final a ser pago
        valor_final = valor_produto - desconto

        # Exibe o valor final a ser pago
        print(f"Valor a ser pago: R${valor_final:.2f}")

        # Verifica se o pagamento é feito com cartão de crédito
        if forma_pagamento.lower() == "crédito":
            parcelas = int(input("Digite o número de parcelas (1, 2, ou 3): "))
            
            if parcelas >= 1 and parcelas <= 3:
                valor_parcela = valor_final / parcelas
                print(f"Valor de cada parcela: R${valor_parcela:.2f}")
            else:
                print("Número de parcelas inválido. Parcelamento permitido apenas em 1, 2 ou 3 vezes.")






