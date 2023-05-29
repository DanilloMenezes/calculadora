from time import sleep


print(32 * "=")
print("Boas Vindas a minha calculadora")
print(32 * "=")

# Variável "nome" com um input perguntado ao usuário seu nome, depois mandar mensagem de boas vindas colocando o nome que o usuário digitou.
nome = input("Digite seu nome: ")
print("A calculadora está iniciando...")
sleep(3)
print(f"Bem-vindo, {nome}! calculadora iniciada. \n Vamos começar?")

# Variável "continua" valendo "s" como sim, dentro do laço de repetição while perguntando no final se o usuário deseja continuar.
# 3 variáveis com inputs perguntando o primeiro número, o operador e o segundo número da conta.
continua = "s"
while continua == "s":
    numero_1 = float(input("Digite o primeiro número: "))
    operador = input("Diga o operador (+, -, *, /): ")
    numero_2 = float(input("Digite o segundo número: "))

    # Operadores sendo utilizados no if, elif e else com suas respectivas condições.

    if operador == "+":
        resultado = numero_1 + numero_2
    elif operador == "-":
        resultado = numero_1 - numero_2
    elif operador == "*":
        resultado = numero_1 * numero_2
    elif operador == "/":
        resultado = numero_1 / numero_2

    # Se caso o usuário não digitar nenhuma das opções a cima, vai mostrar um "erro" para o usuário.
    else:
        resultado = 0 * "Você não digitou qual seria o operador"

    # No final da conta vai mostrar o resultado da operação
    print(f"Resposta: {resultado}")

    # Pergunta ao usuário se ele quer continuar na calculadora, caso digite "n" vai mandar uma mensagem e finalizar o programa.
    continua = input("Você quer continuar na calculadora? (s/n): ")
    if continua == "n":
        print("Obrigador por usar a calculadora!")
        break
