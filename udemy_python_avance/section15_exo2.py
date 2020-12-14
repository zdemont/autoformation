import re

numeros_de_telephone = ['06-71-45-34-23',
						'02-12-33-75-12',
						'00-23-14-52-44',
						'514-235-0293',
						'03-52-31-56-34']

for num in numeros_de_telephone:
    if re.match(r'0[1-7][-0-9]{12}', num):
        print(f'Le numéro {num} est valide')
    else:
        print(f'Le numéro {num} est invalide')

# Le numéro 06-71-45-34-23 est valide
# Le numéro 02-12-33-75-12 est valide
# Le numéro 00-23-14-52-44 est invalide
# Le numéro 514-235-0293 est invalide
# Le numéro 03-52-31-56-34 est valide


# solution

import re

numeros_de_telephone = ['06-71-45-34-23',
                        '02-12-33-75-12',
                        '00-23-14-52-44',
                        '514-235-0293',
                        '03-52-31-56-34']

for tel in numeros_de_telephone:
    match = re.search(r'0{1}[1-7]{1}(-[0-9]{2}){4}', tel)
    print('Le numero {} est {}'.format(tel, 'valide' if match else 'invalide'))