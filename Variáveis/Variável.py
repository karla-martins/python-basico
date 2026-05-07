''' Valor por hora
Escreva um programa que retorna o valor hora de um funcionário, a partir do valor do salário mensal e da quantidade de horas trabalhadas no mês.
'''
#1. Quais são os dados de entrada necessários?
#- Salário mensal
#- Quantidade de horas trabalhadas

#2. O que devo fazer com esses dados?
#- Calcular o valor hora

#3. Quais são as restrições desse problema?
#- Preciso de um valor de salário mensal
#- Preciso de um valor da quantidade de horas trabalhadas

#4. Qual é o resultado esperado?
#- Exibir o valor hora da pessoa, com base no cálculo de valor hora

#5. Qual é a sequêncoa de passos a ser feita para chegar ao resultado esperado? (pseudocódigo)
#- Carregar o salário
#- Carregar a quantidade mensal de horas trabalhadas
#- Calcular o salário dividido pelas horas trabalhadas.
#- Exibir valor hora

salario_mensal = input("Digite o salário mensal: ")
horas_trabalhadas = input("Digite a quantidade de horas trabalhadas no mês: ")
valor_hora = float(salario_mensal) / float(horas_trabalhadas)
print("O valor hora é: ", valor_hora)