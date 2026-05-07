Funciona da mesma forma que o comando for, mas repete o código até a condição ser atendida, não necessariamente o objetivo concretizado.

Criar um programa que permite 3 tentativas antes de fechar
tentativas = 0
while tentativas >= 3:
    print('Tente novamente!')
    tentativas = tentativas + 1

Criar um programa que só permite logar quando digitar a senha correta
senha = ''
while senha != '123456':
    senha = input('Digite a senha correta: ')

print('Bem-vindo ao sistema')

Criar um programa que só continua quando obter o nome do usuário
nome = ''
while nome == '': 
    nome = input('Digite o seu nome: ')
print(f'Bem-vindo {nome}')

Criar um programa de contagem no while
horario = 0
while horário <= 17:
    print('horario')
    horario = horario + 1

print('hora de ver o por do sol')