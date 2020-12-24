# list contenant les élèments présents dans les deux liste

liste_01 = [1, 5, 6, 7, 9, 10, 11]
liste_02 = [2, 3, 5, 7, 8, 10, 12]


# set version 
l = list(set(liste_01).intersection(set(liste_02)))

# method 1 
l = list()
for nb in liste_01:
    if nb in liste_02:
        l.append(nb)

# method 1 : comprehension list
l = [nb for nb in liste_01 if nb in liste_02]
print(l)

