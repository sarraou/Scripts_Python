#Écrire un programme qui va demander à l'utilisateur deux nombres et lui retourne la somme des deux nombres

print("Veuillez saisir deux nombres : ")
nombre1 = int(input("Nombre 1 : "))
nombre2 = int(input("Nombre 2 : "))

print( "La somme est : " + str(nombre1 + nombre2 ))
print( "Le produit est : " + str(nombre1 * nombre2 ))
print( "La difference est : " + str(nombre1 - nombre2 ))
print( "La division est : " + str(nombre1 / nombre2 ))

print( "La somme est : " ,nombre1 + nombre2) # on peut afficher le resultat en utilisant la virgule sans les convertir a srt
#dry = don't repeat yourself = ne pas repeter votre code