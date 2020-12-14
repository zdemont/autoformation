# ----------- Trouver un caractère 

# .				Le point correspond à tous les caractères possibles (incluant symboles)
# [A-F]			Correspond à une liste de caractères possibles.
# (python|c++)	L'un ou l'autre
# ^				Le contraire de ce qu'on veut.
# \d 			Uniquement des chiffres. Équivalent à [0-9]
# \D 			Tout sauf des chiffres. Équivalent à [^0-9]
# \s 			Un espace
# \w 			Un caractère alphanumérique. Équivalent à [a-zA-Z0-9_]
# \W 			Tout sauf un caractère alphanumérique. Équivalent à [^a-zA-Z0-9_]
# \ 			Comme en Python, pour échapper un caractère.



# ----------- Compter un caractère 
# ? 		0 ou 1 fois
# *	    	0 à l'infini
# +	    	de 1 à l'infini
# {3} 		exactement 3
# {3,}  	de 3 à l'infini
# {,3}  	de 0 à 3 fois
# {3,6} 	de 3 à 6 fois