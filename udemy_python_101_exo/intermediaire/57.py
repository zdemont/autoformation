nombre = 52039480394023

nombre_ = str(nombre)
first_couple = len(str(nombre))%3

first_couplenb = [nombre_[0:first_couple]]
reste = nombre_[first_couple:]
couple3 = [reste[i*3:(i+1)*3] for i in range(int(len(reste)/3))]

if '' in first_couplenb:
    nb_splitted = ','.join(couple3)
else:
    nb_splitted = ','.join(first_couplenb + couple3)
print(nb_splitted)

# solution 

def ajout_separateur(nombre):
    nombre = str(nombre)[::-1]
    resultat = ""
 
    for i, chiffre in enumerate(nombre, 1):
        chiffre_formatte = chiffre + "," if i % 3 == 0 and i != len(nombre) else chiffre
        resultat += chiffre_formatte
 
    return resultat[::-1]
