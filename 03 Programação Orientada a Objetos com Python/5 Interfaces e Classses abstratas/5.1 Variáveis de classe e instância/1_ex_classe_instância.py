class Estudante:
    # Variável de
    escola = "DIO"

    def __init__(self, nome, matricula):
        # Variáveis de instância
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"

def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

aluno_1 = Estudante("João", 1)
aluno_2 = Estudante("Gabriel", 2)

print(aluno_1)
print(aluno_2)
mostrar_valores(aluno_1, aluno_2)

# Alterando o número da matricula do aluno 1
# aluno_1.matricula = 3
mostrar_valores(aluno_1, aluno_2)

# Alterando o nome da Escola
Estudante.escola = "Python"

aluno_3 = Estudante("Chico", 3)
mostrar_valores(aluno_1, aluno_2, aluno_3)