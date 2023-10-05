# Ecrire un programme qui choisi le plus grand nombre parmi deux nombres saisies à partir du clavier

print("Veuillez saisir deux nombres : ")
nombre1 = int(input("Nombre 1 : "))
nombre2 = int(input("Nombre 2 : "))

if nombre1 > nombre2:
    print("Le nombre", nombre1, "est le plus grand")
elif nombre1 < nombre2:
    print("Le nombre", nombre2, "est le plus grand")
else:
    print("Les deux nombres sont égaux")