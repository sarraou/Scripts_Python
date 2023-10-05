# Ecrire un programme qui va trouver le plus grand nombre parmi 3 nombres saisis à partir du clavier

print("Veuillez saisir trois nombres : ")
nombre1 = int(input("Nombre 1 : "))
nombre2 = int(input("Nombre 2 : "))
nombre3 = int(input("Nombre 3 : "))

if nombre1 > nombre2 and nombre1 > nombre3:
    print("Le nombre", nombre1, "est le plus grand")
elif nombre2 > nombre1 and nombre2 > nombre3:
    print("Le nombre", nombre2, "est le plus grand")
elif nombre3 > nombre1 and nombre3 > nombre2:
    print("Le nombre", nombre3, "est le plus grand")
else:
    print("Les trois nombres sont égaux")

print("Veuillez saisir trois nombres : ")
a=input("valeur A : ")
b=input("valeur B : ")
c=input("valeur C : ")
if ( a>b and a>c):
    max=a
elif (b>c):
    max=b
else :max=c

print("la valeur max est :" ,max)