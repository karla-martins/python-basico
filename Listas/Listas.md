Definimos um nome para a lista, abrimos colchetes e colocamos as variaveis da lista.
preços = [20, 30, 50]

Podemos acessar cada variável de forma individual pelo seu índice, o índice é a posição da variável na lista vista pelo computador.
preços = [20, 30, 50]
[20, 30, 50]
  0   1   2
E no python, o primeiro valor é sempre 0 na lista.

Se escrevermos um código
preços = [20, 30, 50]
print(preços[0])
o programa imprimirá o valor 20.

A lista pode alterar entre variáveis, mas o índice será sempre um valor numérico.

Podemos também encontrar o indíce pelo nome da variável.
preços = [20, 30, 50]
print(preços.index(30))

Podemos adicionar novos itens a lista também!
preços = [20, 30, 50]
preços_novos = float(input('Qual novo valor deseja adicionar?: '))
preços.append(preços_novos)
print(preços)

