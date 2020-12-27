employes = {}
liste = [10, 2329, 5, "Pierre", 203, "Marie", 867, "Adrien"]

index_nb = 1
for obj in liste:
    if isinstance(obj, str):
        index = "id-0{}".format(index_nb) if index_nb < 10 else "id-{}".format(index_nb)
        employes[index] = obj
        index_nb += 1
print(employes)


#  solution
i = 1
 
for element in liste:
    if not str(element).isdigit():
        employes["id-{:02d}".format(i)] = element
        i += 1
 
print(employes)