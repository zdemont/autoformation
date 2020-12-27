liste = ["Pierre", "Marie", "Julie", "Adrien", "Julie"]
nom_a_chercher = "Julie"
nouveau_nom = "Julien"

liste_replaced = []
for name in liste:
    if nom_a_chercher == name:
        liste_replaced.append(nouveau_nom)
    else:
        liste_replaced.append(name)
print(liste_replaced)


# solution
liste_replaced = [x.replace(nom_a_chercher, nouveau_nom) for x in liste]
