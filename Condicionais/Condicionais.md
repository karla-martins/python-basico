Condicionais - if else elif

if 
Se acontecer x, faça isso

else
Se não acontecer x, faça isso

elif
um intermediário entre if e else, quando há mais de duas possibilidades.




EXEMPLOS

Exemplo 1

'''
"Oii, vamos dar uma saída hoje?"
"Se eu sair mais cedo do trabalho eu consigo!"

Em python, diriamos algo como...
'''
trabalho_terminado = True
if trabalho_terminado == True:
    print('Bora!')
else:
    print('Não posso sair')


Exemplo 2

'''
"Me ajuda a mover as caixas lá para fora hoje?"
"Se eu estiver livre, sim. Mas se não der, pede auda ao meu irmão"
'''
estou_livre = True
if estou_livre == True:
    print('Bora mover as caixas!')
else:
    print('Pede ajuda pro meu irmão')


Exemplo 3

'''
"Eu cheguei atrasado na aula, ainda posso entrar?"
"Se for a sua primeira vez chegando atrasado, pode entrar. Mas se for a terceira vez, você será suspenso!"
'''
atrasos = 0
if atrasos >= 3:
    print('Você será suspenso!')
elif atrasos ==2:
    print('Mais um atraso e você será suspenso!')
elif atrasos ==1:
    print('Mais dois atrasos e você será suspenso!')
else:
    print('Pode entrar, mas cuidado com os atrasos!')