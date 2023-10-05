#Lire les données utilisateur avec input
#input est tjrs string meme si on ecrit un nombre

nom = input("Entrez votre nom svp : ")
print("Salut " + nom)
#nombre = input("Veuillez saisir un nombre :")
#print(nombre+1)

nombre = int(input("Veuillez saisir un nombre : \n"))
resultat = nombre + 1
print(resultat)# il va afficher le resultat plus 1

#Concaténer une chaine de caractère avec un nombre int
#print("Le resultat est " + resultat) #on ne peut pas concatener une chaine de caractere avec un nombre
print("Le resultat est " + str(resultat)) #solution

#afficher le type ==> il faut convertir 
print(type(nombre))
resultat = int(nombre) + 1 #il faut convertir de str vers int
print(type(resultat))

