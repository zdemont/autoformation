# Ajouter plusieurs éléments à une liste

ma_liste = [1, 2, 3]

ma_liste += [i for i in range(ma_liste[-1]+1, 7)]
print(ma_liste)


# solution
ma_liste.extend([4, 5, 6])
print(ma_liste)