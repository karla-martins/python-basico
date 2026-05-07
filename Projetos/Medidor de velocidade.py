'''
Crie um programa que receba do usuário um valor que represente a velocidade em uma via cuja velocidade máxima permitida é de 80km/h.

Com base nesse valor, o programa deve informar se o motorista levou um multa leve, grave ou gravíssima.

Se a velocidade estiver abaixo ou igual a 80km/h. Exiba "Sem multas"
Se a velocidade estiver até 10km/h acima do limite, exiba "Multa leve"
Se a velocidade estiver entre 11km/h e 20km/h acima do limite, exiba "Multa grave"
Se a velocidade estiver acima de 20km/h do limite, exiba "Multa gravíssima"
'''

#1. Quais são os dados de entrada necessários?
# - Velocidade do motorista.

#2. O que devo fazer com esses dados?
# - Comparar a velocidade do motorista e determinar se houve multa e qual gravidade.

#3. Quais são as restrições desse problema?
# - A velocidade deve ser um número positivo.

#4. Qual é o resultado esperado?
# - Informar se houve multa, leve, grave ou gravíssima caso tenha.

#5. Qual é a sequêncoa de passos a ser feita para chegar ao resultado esperado? (pseudocódigo)
# - receber a velocidade do motorista
# - verificar em que critério se enquadra.
# - exibir o resultado corresopndente a velocidade informada.

velocidade = float(input('Digite a velocidade do motorista em km/h: '))
if velocidade <= 80:
    print('Sem multas, parabéns!')
elif velocidade <= 90:
    print('Multa leve, tenha mais cuidado!')
elif velocidade <= 100:
    print('Multa grave, tenha mais cuidado!')
else:
    print('Multa gravíssima, você está muito acima do limite!')