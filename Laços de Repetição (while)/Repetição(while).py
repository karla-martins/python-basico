'''
Exemplo prático - Gerenciador de login simples

Crie um gerenciador de login simples com o máximo de 3 tentativas.
(apenas um usuário e senha pré-definidos)

usuário - karla
senha - 123456

Após 3 tentativas erradas, o programa deve exibir "Aguarde 30min para tentar novamente!"

Se o usuário e senha estiverem corretos, o programa deve exibir "Login bem-sucedido!"
'''

#1. Quais são os dados de entrada necessários?
# - Usuário e senha pré-definidos

#2. O que devo fazer com esses dados?
# - Verificar se o usuário e senha inseridos correspondem aos pré-definidos

#3. Quais são as restrições desse problema?
# - O usuário tem no máximo 3 tentativas de login

#4. Qual é o resultado esperado?
# - Exibir "Login bem-sucedido!" se as credenciais estiverem corretas
# - Exibir "Aguarde 30min para tentar novamente!" se o usuário exceder o número de tentativas

#5. Qual é a sequêncoa de passos a ser feita para chegar ao resultado esperado? (pseudocódigo)
# 1. Solicitar usuário e senha
# 2. Verificar se as credenciais estão corretas
# 3. Se estiverem corretas, exibir "Login bem-sucedido!"
# 4. Se estiverem erradas, incrementar o contador de tentativas
# 5. Se o contador de tentativas atingir 3, exibir "Aguarde 30min para tentar novamente!"
# 6. Repetir os passos 1 a 5 até que o login seja bem-sucedido ou o limite de tentativas seja atingido

usuário = ''
senha = ''
tentativas = 0

while usuário != 'karla' and senha != '123456':
    usuário = input('Digite o usuário: ')
    senha = input('Digite a senha: ')
    tentativas += 1

if usuário != 'karla' and senha != '123456':
    print('Aguarde 30min para tentar novamente!')
else:
    print('Login bem-sucedido!')