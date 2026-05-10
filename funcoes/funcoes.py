# Crie uma função que recebe um número, e faz um contador regressivo a partir dele.
print('Exercício 1: Contador Regressivo')

n = int(input("Digite um número para o contador regressivo: "))
def contador_regressivo(n):
    for i in range (n, -1, -1): # O range começa em n, vai até -1 (não incluindo) e decrementa de 1 em 1.
        print(i)                # exibe o valor de i a cada iteração do loop.
contador_regressivo(n)


# Crie uma função que recebe uma lista e retorne o maior número dessa lista.
print('Exercício 2: Maior Número na Lista')

def maior_numero(lista):
    if len(lista) == 0:
        return None
    maior = lista[0]
    for numero in lista:
        if numero > maior:
            maior = numero
    return maior 
print(maior_numero([3, 7, 2, 9, 5]))

# Exercício 2.1: Maior Número na Lista usando a função max()
''' 
def maior_numero(lista)
    maior_numero = max(lista)
    return maior_numero
print(maior_numero([3, 7, 2, 9, 5]))
'''