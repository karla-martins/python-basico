Blocos de comando que atuam e processam de forma separada do código em si, podendo ter variáveis locais diferentes das globais.
Podemos criar as funções e chamar por elas igual acontece com um input ou print, e as funções atuam da forma personalizada que as criamos para atuar.
Para a criação de uma função, basta inserir def [nome da função](): e adicionar a ela as ações desejadas.

Ou seja, se digitarmos e tentarmos rodar o código:
def minha_funcao():
     print('Essa é a minha função!')

 Não vai acontecer nada! 😁

Criamos a função, mas para ela ser executada, precisamos CHAMAR a função! Para isso basta escrever a função na linha do código.

def minha_funcao():
     print('Essa é a minha função!')  -- Esse recuo significa que o código nele é atribuído ao código acima.
minha_funcao()

Mas e se quiser colocar uma variável dentro da minha função? É possível por duas formas.

I. Incluindo a variável somente a função:
def minha_funcao():
     nome = 'Karla'
     print(f'Essa é a minha função! Prazer {nome}!')  minha_funcao()

II. Incluindo a variável no código:
nome = 'Karla'
def minha_funcao():
     print(f'Essa é a minha função! Prazer {nome}!')  minha_funcao()

A diferença é simples, incluindo a variável somente a função, ela só existirá na função. Se incluir a variável ao código, ela existirá no código em si e não somente na função.

Se você quiser que sua função haja de forma mais direta e não só mostre as informações, como as funções criadas anteriormente, você pode criá-la para, por exemplo, somar números. Mas para informá-la os números que devem ser somados, utilizamos os parâmetros. 
Para adicionar parâmeros a uma função, basta inseri-los dentro dos parênteses presentes ao lado da função.
def somar(n1, n2):
      resultado = n1 + n2
      print(f'A soma entre {n1} e {n2} é igual a {resultado}')
def somar(6, 40)

a função por se tratar de uma ação, se tentar colocá-la junto a uma variável, não é possível, a não ser que se use o comando return ao final.
def somar(n1, n2):
      resultado = n1 + n2
      print(f'A soma entre {n1} e {n2} é igual a {resultado}')
      return resultado
resultado_da_soma = somar(5, 5)
print(resultado_da_soma)

Os parâmetros utilizados na função, serão sempre 2, quando há uma quantidade indefinida de parâmetros, utilizamos * para acrescentar vários parâmetros.
Vamos calcular por exemplo, a média de alguns números:
def calcular_media(*numeros)
      qtd = len(numeros)
      soma = 0
      for numero in numeros: 
            soma += numero
      media = soma / qtd
      return media
resultado = cacular_media(7, 2, 4, 9)
print(f"A média é {resultado}!")

Por último, se nos parâmetros, colocarmos ** antes do parâmetro, o código retorna com todas as informações adicionadas ao parâmetro.
def informacoes_pessoais(**informacoes):
      print(informacoes)
informacoes_pessoais(nome="Karla", idade=21)