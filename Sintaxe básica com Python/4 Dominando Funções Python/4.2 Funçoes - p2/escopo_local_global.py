# ESCOPO GLOBAL 
salario = 2000

# Se o "global salario" não for utilizado, a função não saberá que a variável existe
def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario


salario_com_bonus = salario_bonus(500)
print(salario_com_bonus)