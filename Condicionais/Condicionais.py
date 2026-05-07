'''
Um programa que receba dois valores e retorne o maior entre eles.
'''

#1. Quais são os dados de entrada necessários?
# - Dois valores numéricos

#2. O que devo fazer com esses dados?
# - Comparar os dois valores

#3. Quais são as restrições desse problema?
# - Os valores devem ser numéricos

#4. Qual é o resultado esperado?
# - Exibir o maior valor fornecido.

#5. Qual é a sequência de passos a ser feita para chegar ao resultado esperado? (pseudocódigo)
# - Receber o 1° valor
# - Receber o 2° valor
# - Comparar os dois valores
# - Exibir o maior valor

valor_1 = int(input('Digite o primeiro valor: '))
valor_2 = int(input('Digite o segundo valor: '))
if valor_1 > valor_2:
    print("O maior valor é: ", valor_1)
else:
    print("O maior valor é: ", valor_2)