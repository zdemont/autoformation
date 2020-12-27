import os

# get extension

fichier = "C:/Python36/python.exe"

_, extention = os.path.splitext(fichier)

extention = extention.replace('.', '')
print(extention)

# solution
extension = os.path.splitext(fichier)[1]
extension = extension.strip(".")
print(extention)