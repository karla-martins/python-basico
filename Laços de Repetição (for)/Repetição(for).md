Ao invés de escrevermos número por número em um código, podemos usar o comando for para repetir criar o código com a regra desejada até alcançar o objetivo indicado.

for [variável] in range ([quantidade de números desejada])
    print ([variável])
RANGE NUNCA INCLUI O ÚLTIMO NÚMERO
Dessa forma, teremos em nosso terminal os números partindo do 0 e parando 1 número antes do número escrito (se escrever que deseja 12 números, o programa irá até o número 11).

for [variáve] in range ([primeiro número], [até esse número], [pulando tantos números])
for lista in range (2, 22, 2)
Ou seja: quero uma lista de 20 números, começando do 2 e pulando sempre 2 números.

Para listas de elementos, uma lista pode conter todo tipo de dados
elementos = ['joão', 123, True, 1.6]
    for elemento in elementos:
        print(nome)

Podemos juntar as listas com os condicionais
idades = [13, 15 18, 30, 50, 75]
for idade in idades:
    if idade >= 18:
        print(f'{idade} É maior de idade')
    else:
        print(f'{idade} É menor de idade)

A função len
serve para verificar a quantidade de caracteres nas variáveis dentro da lista.

#Preciso encontrar um nome que contenha mais de 6 letras
nomes = [Karla, Fernanda, Jaqueline, Helena, Luiza]
for senha in senhas
    if len(nomes) > 6:
        print(f'O nome {nome} é maior')
    else:
        print(f'O nome {nome} é menor ou igual')