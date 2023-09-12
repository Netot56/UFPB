Quest= int(input("Digite a questão: "))
def switch_case(Quest):
    if Quest == 1:
        i=1
        soma=0
        while(i<=500):
            if((i%2!=0) and (i%3==0)):
                print(i)
                soma = soma+i
            i+=1
        print(f"A soma de todos os número ímpares que são multiplus de tres e que se encontram no conjunto dos número de 1 até 500 é :{soma}")
    elif Quest ==2:
        menor_valor = float('inf')  # Inicializado com infinito para garantir que qualquer número seja menor
        maior_valor = float('-inf')  # Inicializado com menos infinito para garantir que qualquer número seja maior
        soma_valores = 0

        # Solicita ao usuário que insira números repetidamente até que -1 seja digitado
        while True:
            entrada = input("Digite um número (ou -1 para sair): ")
            
            # Verifica se o usuário deseja sair
            if entrada == '-1':
                break
            
            # Converte a entrada para um número real
            numero = float(entrada)
            
            # Atualiza o menor e o maior valor, se necessário
            if numero < menor_valor:
                menor_valor = numero
            if numero > maior_valor:
                maior_valor = numero
            
            # Atualiza a soma dos valores
            soma_valores += numero

        # Exibe os resultados
        if soma_valores != 0:
            print(f"Menor valor: {menor_valor}")
            print(f"Maior valor: {maior_valor}")
            print(f"Soma dos valores: {soma_valores}")
        else:
            print("Nenhum número foi inserido.")
    elif Quest ==3:
        populacao_x = 70000  # População inicial do país X
        taxa_crescimento_x = 0.035  # Taxa de crescimento anual de 3.5% para o país X

        populacao_y = 180000  # População inicial do país Y
        taxa_crescimento_y = 0.015  # Taxa de crescimento anual de 1.5% para o país Y

        anos = 0  # Inicialize o contador de anos

        # Continue o loop até que a população de X seja maior ou igual à população de Y
        while populacao_x < populacao_y:
            # Calcule o crescimento populacional para ambos os países
            populacao_x += populacao_x * taxa_crescimento_x
            populacao_y += populacao_y * taxa_crescimento_y
            anos += 1

        # Exibe o número de anos necessários
        print(f"Serão necessários {anos} anos para que a população do país X ultrapasse ou iguale a população do país Y.")
    elif Quest ==4:
        dividendo = int(input("Digite o dividendo (número a ser dividido): "))
        divisor = int(input("Digite o divisor (número pelo qual dividir): "))

        # Inicializa as variáveis para o quociente e o resto
        quociente = 0
        resto = dividendo  # Inicialmente, o resto é igual ao dividendo

        # Realiza a divisão inteira usando subtração
        while resto >= divisor:
            resto -= divisor
            quociente += 1

        # Exibe o resultado
        print(f"Quociente da divisão: {quociente}")
        print(f"Resto da divisão: {resto}")
    elif Quest ==5:
        # Solicita ao usuário que insira o valor inicial da dívida, a taxa de juros mensal e o valor mensal pago
        valor_inicial = float(input("Digite o valor inicial da dívida: "))
        taxa_juros_mensal = float(input("Digite a taxa de juros mensal (em decimal, por exemplo, 0.05 para 5%): "))
        valor_mensal_pago = float(input("Digite o valor mensal a ser pago: "))

        # Inicializa variáveis para o número de meses, o total pago e o total de juros
        num_meses = 0
        total_pago = 0
        total_juros_pago = 0

        # Calcula o número de meses necessários para pagar a dívida
        while valor_inicial > 0:
            juros = valor_inicial * taxa_juros_mensal
            amortizacao = valor_mensal_pago - juros
            
            if amortizacao <= 0:
                break
            
            valor_inicial -= amortizacao
            num_meses += 1
            total_pago += valor_mensal_pago
            total_juros_pago += juros

        # Exibe os resultados
        print(f"Número de meses necessários para pagar a dívida: {num_meses}")
        print(f"Total pago: R${total_pago:.2f}")
        print(f"Total de juros pago: R${total_juros_pago:.2f}")
    elif Quest ==6:
        # Cria um dicionário para mapear códigos para preços
        codigo_preco = {
            1: 5.50,
            2: 2.30,
            3: 4.75,
            4: 6.80,
            5: 9.30
        }

        # Inicializa variáveis para o total da compra
        total_compra = 0.0

        # Solicita ao usuário que insira os produtos e suas quantidades até que deseje encerrar
        while True:
            codigo = int(input("Digite o código do produto (ou 0 para finalizar a compra): "))
            
            # Verifica se o usuário deseja finalizar a compra
            if codigo == 0:
                break
            
            # Verifica se o código está no dicionário
            if codigo in codigo_preco:
                quantidade = int(input(f"Digite a quantidade do produto {codigo}: "))
                
                # Calcula o subtotal para o produto
                subtotal = codigo_preco[codigo] * quantidade
                
                # Adiciona o subtotal ao total da compra
                total_compra += subtotal
            else:
                print("Código não encontrado. Por favor, insira um código válido.")

        # Exibe o total da compra
        print(f"Total da compra: R${total_compra:.2f}")
    elif Quest ==7:
        # Solicita ao usuário que insira o número para o qual deseja calcular a raiz quadrada
        n = float(input("Digite o número para calcular a raiz quadrada: "))

        # Valor inicial de b
        b = 2.0

        # Inicializa p
        p = (b + n / b) / 2.0

        # Define a precisão desejada
        precisao = 0.001

        # Realiza o cálculo da raiz quadrada usando o método de Newton
        while abs(b - p) >= precisao:
            b = p
            p = (b + n / b) / 2.0

        # Exibe o valor da raiz quadrada aproximada
        print(f"A raiz quadrada de {n} é aproximadamente {p:.3f}")

    
