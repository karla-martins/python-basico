'''Escreva um programa que gera um número aleatório entre 1 e 100 e pede para o usuário adivinhar o número. O programa deve informar se a tentativa do usuário é muito alta, muito baixa ou correta. O jogo deve continuar até que o usuário adivinhe o número corretamente.
'''

# 1. Quais são os dados de entrada necessários?
# - O número aleatório gerado pelo programa.
# - A tentativa do usuário para adivinhar o número.

#2. O que devo fazer com esses dados?
# - Comparar a tentativa do usuário com o número aleatório e fornecer feedback se a tentativa é muito alta, muito baixa ou correta.

#3. Quais são as restrições desse problema?
# - O número aleatório deve estar entre 1 e 100.
# - O usuário deve inserir um número inteiro como tentativa.

#4. Qual é o resultado esperado?
# - O programa deve continuar solicitando tentativas do usuário até que ele adivinhe o número corretamente, fornecendo feedback a cada tentativa.

#5. Qual é a sequêncoa de passos a ser feita para chegar ao resultado esperado? (pseudocódigo)
# - Gerar um número aleatório entre 1 e 100.
# - Solicitar ao usuário que adivinhe o número.
# - Comparar a tentativa do usuário com o número aleatório.
# - Fornecer feedback se a tentativa é muito alta, muito baixa ou correta.
import random
número_aleatório = random.randint(1, 100)
tentativa = 0
while tentativa != número_aleatório:
    tentativa = int(input('Tente adivinhar o número entre 1 e 100: '))
    if tentativa < número_aleatório:
        print('Muito baixo! Tente novamente.')
    elif tentativa > número_aleatório:
        print('Muito alto! Tente novamente.')
    else:
        print('Parabéns! Você adivinhou o número corretamente.')