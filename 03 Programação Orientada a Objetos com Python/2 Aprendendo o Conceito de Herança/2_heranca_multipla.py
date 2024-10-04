class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

# Função para retornar ao usuário os valores do objeto
    def __str__(self):
        # Retornando a classe e o nome e percorrendo o objeto para obter e criar chave e o valor de cada um utilizando iteração e o método __dict__ (dicionário)
        return f"{self.__class__.__name__}: {', '.join([f"{chave}={valor}" for {chave}, valor in self.__dict__.items()])}"



class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw): # Utilizando kwargs para passar por chave e valor evitando repetição de dado e erro
        self.cor_pelo = cor_pelo
        super().__init__(**kw) # Passando as kw para a classe pai (Animal)

class Ave(Animal):
    def __init__(self, cor_bico, **kw): 
        self.cor_bico = cor_bico
        super().__init__(**kw) 



class Gato(Mamifero):
    pass


class Ornitorrinco(Mamifero, Ave):
    def __init__(self, cor_bico, cor_pelo, nro_patas):
        print(Ornitorrinco.__mro__)

        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, nro_patas=nro_patas)



gato = Gato(nro_patas=4, cor_pelo="preto")
print(gato)

ornitorrinco = Ornitorrinco(nro_patas=2, cor_pelo="vermelho", cor_bico="laranja")
print(ornitorrinco)