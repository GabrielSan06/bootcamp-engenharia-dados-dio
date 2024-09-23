lista = [1, "Python", [40, 30.5, 20]]

l2 = lista.copy()

# São objetos diferentes
print(id(l2), id(lista)) 

l2[0] = 2

# A alteração em um, não influencia no outro
print(lista)
print(l2)