nombres = range(50)


#  exercice 45
nombres_pairs = []

for i in nombres:
    if i%2 == 0:
        nombres_pairs.append(i)
print(nombres_pairs)

#  excerice 46 short version
nombres_pairs = [i  for i in nombres if i % 2 == 0]
print(nombres_pairs)