"""Calculadora com while"""

while True:
    numero_1 = input("Digite um número: ")
    numero_2 = input("Digite outro número: ")
    operador = input("Digite um operador (+-/*): ")

    num_1_float = 0
    num_2_float = 0
    numeros_validos = None

    # Verificando se os números fornecidos são valores válidos
    # Obs: Não é uma boa prática deixa o except desta forma
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print("Um ou ambos os números digitados são inválidos.")
        continue

    operadores_permitidos = "+-/*"
    # Verificando se os operadores são os que estão dentro dos possiveis
    if operador not in operadores_permitidos:
        print("Operador inválido.")

    #  Verifica se o usuário informou mais de um operador
    if len(operador) > 1:
        print("Digite apenas um operador.")
        continue

    #  Faz as operações
    print("Resultado: ")
    if operador == "+":
        print(f"{num_1_float}+{num_2_float}=", num_1_float + num_2_float)
    elif operador == "-":
        print(f"{num_1_float}-{num_2_float}=", num_1_float - num_2_float)
    elif operador == "*":
        print(f"{num_1_float}*{num_2_float}=", num_1_float * num_2_float)
    elif operador == "/":
        print(f"{num_1_float}/{num_2_float}=", num_1_float / num_2_float)
    else:
        print("Nunca deveria chegar aqui.")

    #  Torna a palavra ou letra em minusculo e depois verifica se começa com 's'
    sair = input("Quer sair? [s]im: ").lower().startswith("s")

    if sair is True:
        break
