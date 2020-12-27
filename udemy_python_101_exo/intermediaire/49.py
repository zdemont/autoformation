nombres = [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7, 8, 9, 10]

nombres_deduplicate = list()

for nombre in nombres: 
    if nombre not in nombres_deduplicate:
        nombres_deduplicate.append(nombre)
print(nombres_deduplicate)
