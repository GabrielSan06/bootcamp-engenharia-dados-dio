conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

# Nenhum elemento de A está em B
print(conjunto_a.isdisjoint(conjunto_b))

# Nenhum elemento de A está em C
print(conjunto_a.isdisjoint(conjunto_c))