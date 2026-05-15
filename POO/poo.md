A Programação Orientada a Objetos é diferenciada da Programação Estruturada pelo seu funcionamento.
Enquanto na Programação Estruturada, o código é organizado em funções e executado de maneira sequencial, na Programação Orientada a Objetos, os dados e comportamentos são agrupados em objetos que possuem atributos e métodos.

Uma forma muito simples de explicar como funciona a POO é a seguinte:
Vamos fazer Cookies!

Fazemos a massa da forma que desejamos, mas eu gostaria de cookies em formatos de coração. Para que todos fiquem com o mesmo formato bonito de coração, usamos uma forma.  -- Essa é nossa classe.

Quando abrimos a massa no balcão e pressionamos a forma contra ela, estamos cortando a massa. -- Essa é nossa instância (o movimento que a classe faz para a criação de um objeto)

Retiramos então a forma, deixando somente a massa com o formato de coração pronto para ir ao forno. -- Esse é nosso objeto.

Fizemos três coberturas diferentes e, como o forno é pequeno, separamos as fornadas por cobertura, ou seja, três fornadas, colocando uma delas no forno. Com isso, conseguimos dizer que, mesmo com a mesma forma(classe) os cookies são diferentes entre si, correto?

Na primeira fornada, colocamos uma cobertura de chocolate e, enquanto esfriam, colocamos a segunda fornada para assar.

Na segunda fornada, colocamos uma cobertura de caramelo, enquanto esfriam, colocamos a terceira fornada para assar e embalamos a primeira fornada já fria.

na terceira fornada, tivemos um problema e os cookies não conseguiram assar completamente, por isso os congelaremos junto com sua cobertura para assar em outra oportunidade, embalamos a segunda fornada já fria e limpamos os utensílios usados.

Ao final, temos 3 tipos de cookies diferentes, correto?

Temos o cookie com cobertura de chocolate.
Temos o cookie com cobertura de caramelo.
Temos o cookie com cobertura de maracujá.

E se eu te perguntasse:
Os cookies estão embalados?
Eles estão prontos para consumo?
Eles estão assados?
Eles estão com cobertura?
Os cookies estão na temperatura correta para consumo?

Essas perguntas, em POO são consideradas métodos, os métodos no caso citado retornaria com um valor Booleano. Os métodos são funções dentro de classes.

Mas e os cookies que estão prontos, como eles estão? Quais são suas características?
Qual seu formato?
Qual sua cobertura?
Qual sua temperatura?
Qual seu estado?
Ele está embalado?

As características em POO são chamadas de atributos, que, quando chamados, exibem as informações desejadas na tela.

No final, se tentarmos passar todo esse exemplo para código, ficaria assim:

class Cookie:
    def __init__(self, formato, cobertura):
        # ATRIBUTOS
        self.formato = formato
        self.cobertura = cobertura
        self.temperatura = "quente"
        self.estado = "cru"
        self.embalado = False

    # MÉTODOS
    def assar(self):
        self.estado = "assado"
        print(f"O cookie de {self.cobertura} foi assado.")

    def esfriar(self):
        self.temperatura = "frio"
        print(f"O cookie de {self.cobertura} esfriou.")

    def embalar(self):
        if self.temperatura == "frio":
            self.embalado = True
            print(f"O cookie de {self.cobertura} foi embalado.")
        else:
            print("O cookie ainda está quente para ser embalado.")

    def congelar(self):
        self.estado = "congelado"
        print(f"O cookie de {self.cobertura} foi congelado.")

    # MÉTODOS BOOLEANOS
    def esta_assado(self):
        return self.estado == "assado"

    def esta_embalado(self):
        return self.embalado

    def pronto_para_consumo(self):
        return self.estado == "assado" and self.temperatura == "frio"

    # EXIBIR INFORMAÇÕES
    def mostrar_informacoes(self):
        print("\n--- INFORMAÇÕES DO COOKIE ---")
        print(f"Formato: {self.formato}")
        print(f"Cobertura: {self.cobertura}")
        print(f"Temperatura: {self.temperatura}")
        print(f"Estado: {self.estado}")
        print(f"Embalado: {self.embalado}")

OBJETOS (COOKIES)

cookie_chocolate = Cookie("coração", "chocolate")
cookie_caramelo = Cookie("coração", "caramelo")
cookie_maracuja = Cookie("coração", "maracujá")

PRIMEIRA FORNADA
cookie_chocolate.assar()
cookie_chocolate.esfriar()
cookie_chocolate.embalar()

SEGUNDA FORNADA
cookie_caramelo.assar()
cookie_caramelo.esfriar()
cookie_caramelo.embalar()

TERCEIRA FORNADA
cookie_maracuja.congelar()

EXIBINDO INFORMAÇÕES
cookie_chocolate.mostrar_informacoes()
cookie_caramelo.mostrar_informacoes()
cookie_maracuja.mostrar_informacoes()

TESTANDO MÉTODOS BOOLEANOS
print("\n--- TESTES BOOLEANOS ---")

print(cookie_chocolate.pronto_para_consumo())
print(cookie_caramelo.esta_embalado())
print(cookie_maracuja.esta_assado())

OBS: O __init__ é utilizado para inicializar o objeto no momento da sua criação, definindo seus atributos iniciais.
OBS¹: O self serve para representar o próprio objeto, permitindo acessar seus atributos e métodos.
