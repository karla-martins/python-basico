#Crie um programa que receba um número e imprima o seu fatorial.

#1. Quais são os dados de entrada necessários?
# - Um número inteiro.

#2. O que devo fazer com esses dados?
# - Calcular o fatorial do númeo recebido.

#3. Quais são as restrições desse problema?
# - O número deve ser inteiro e não deve ser negativo.

#4. Qual é o resultado esperado?
# - receber o número e imprimir seu fatorial.

#5. Qual é a sequêncoa de passos a ser feita para chegar ao resultado esperado? (pseudocódigo)
# - solicitar um número inteiro
# - verificar se o número é negativo, se for, exibir uma mensagem de erro
# - calcular o fatorial do número
# - exibir o resultado

número = int(input('Digite um número inteiro: '))
if número >= 0:
    fatorial = 1
    for i in range(1, número + 1):
        fatorial *= i
    print(f'O fatorial de {número} é: {fatorial}')
else:
    print('Erro: O número deve ser inteiro e não negativo.')