symbole = "$"
taille = 20

for nb, _ in enumerate(range(taille), start=1):
    nb_symbole = '$ ' * nb
    nb_space = ' ' * (taille - nb + 1) 
    print(nb_space, nb_symbole)


# solution 

for i in range(1, taille + 1):
    espaces = " " * (taille - i)
    print(espaces + (symbole + " ") * i)