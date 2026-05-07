'''
Exemplo prático com algoritmo real: Validador de senhas

Problema:
Você trabalha em um sistema que precisa veificar se todas as senhas digitadas pelos usuários são válidas. 

Para uma senha ser válida, ela deve ter pelo menos 6 caracteres.
'''

#1. Quais são os dados de entrada necessários?
# - a senha informada pelo usuário

#2. O que devo fazer com esses dados?
# - receber a senha do usuário.
# - verificar se a senha contém pelo menos 6 caracteres
# - exibir uma mensagem indicando se a senha é válida ou não.

#3. Quais são as restrições desse problema?
# - a senha deve conter pelo menos 6 caracteres

#4. Qual é o resultado esperado?
# - receber a senha e informar na tela se ela é valida ou não.

#5. Qual é a sequência de passos a ser feita para chegar ao resultado esperado? (pseudocódigo)
# - receber a senha do usuário.
# - verificar se a senha contém pelo menos 6 caracteres
# - exibir uma mensagem indicando se a senha é válida ou não.

senha = input("Digite sua senha: ")

if len(senha) >= 6:
    print("Senha válida!")
else:
    print("Senha inválida! Deve conter pelo menos 6 caracteres.")
    