conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

# todos os elementos de B pertencem a A
print(conjunto_a.issuperset(conjunto_b))

# todos os elementos de A pertencem a B
print(conjunto_b.issuperset(conjunto_a))