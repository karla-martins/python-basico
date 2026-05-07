'''
Exemplo prático - Dados totais de pagamento de salário
Crie um programa que calcule o total a ser gasto com o pagamento de todos os funcionários.
'''

#1. Quais são os dados de entrada necessários?
# - Número de funcionários
# - Valor pago a cada funcionário

#2. O que devo fazer com esses dados?
# - Somar o valor pago a cada funcionário.

#3. Quais são as restrições desse problema?
# - Precisamos de no mínimo dois salários para somar o total a ser gasto.

#4. Qual é o resultado esperado?
# - Exibir o total a ser gasto com o pagamento de todos os funcionários.

#5. Qual é a sequêncoa de passos a ser feita para chegar ao resultado esperado? (pseudocódigo)
# 1. Solicitar o número de funcionários
# 2. Para cada funcionário, solicitar o valor pago
# 3. Somar todos os valores pagos
# 4. Exibir o total a ser gasto

Salários = []
total = 0
Número_de_funcionários = int(input('Digite o número de funcionários: '))
for i in range(Número_de_funcionários):
    salário = float(input(f'Digite o salário do funcionário {i + 1}: '))
    Salários.append(salário)

for salário in Salários:
    total += salário

print(f'O total a ser gasto no pagamento dos funcionários é: R$ {total}')