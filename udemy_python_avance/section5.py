
# Exercice 1
liste = [1, 2, 3, 4, 5]
list_double = [element*2 for element in liste]
print(list_double)

# Exercice 2
liste = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
list_double = [i*2 for i in liste if i > 0 ]
print(list_double)

# Exercice 3
liste = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
list_double = [i*2 if i > 0 else i*3 for i in liste]
print(list_double)

# Exercice 4
liste_finale = [(i,y) for i in range(10) for y in range(2)]
print(liste_finale)