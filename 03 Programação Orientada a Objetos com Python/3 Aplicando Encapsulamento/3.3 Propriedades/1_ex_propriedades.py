class Foo:
    def __init__(self, x=None):
        self._x =  x

    # Transformando o método em atributo para conseguir exibi-lá
    @property
    def x(self):
        return self._x or 0

    @x.setter # Possibilita a modificar e atribuir de valor
    # O primeiro valor é a instancia e o segundo valor é o definido após o =
    def x(self, value):
        self._x += value
    
    @x.deleter
    def x(self):
        self._x = 0

# Exibindo x
foo = Foo(10)
print(foo.x)

# Deletando (zerando) x
del foo.x
print(foo.x)

# Settando (adicionando) x
foo.x = 10
print(foo.x)