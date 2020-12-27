import random

# 33 : reserve word

mot = "Udemy"

print(mot[::-1].lower().capitalize())

# 34 shuffle letter 

mot = 'Bonjour'

print(''.join(random.sample(mot.lower(),len(mot))).capitalize())

# solultion 34
mot = list(mot)
 
random.shuffle(mot)
 
mot_random = "".join(mot).capitalize()


# 35 
nombre = 2938.48872
decimales = 3

nb_rounded = round(nombre, decimales)
print(f"Nombre tronqué: {nb_rounded}")

# solution 35 

print("Nombre tronqué: {nombre:.{decimales}f}".format(nombre=nombre, decimales=decimales))
