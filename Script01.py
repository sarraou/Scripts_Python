#Les identifiants Python
a=20
nom='Sarra'
#1 Les symboles autorisés pour les noms identifiants en python sont :
#L'alphabet est autorisé en Majuscule ou en miniscule
#Les chiffres de 0 à 9
#Le symbole _
somme=200
#somme$=400


#Les identifiants ne doivent pas commencer par un chiffre
#123test=2
test123=2

# Les identifiants en python sont sensibles à la casse :
somme=20
SOMME=200
print(somme,SOMME)

# On ne peut pas utiliser des mots résérvés python comme identifiant :
#if=10

#for=10

# Il n'y a pas de limite pour la taille d'un identifiant :
test=20
testttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt=200


#on choisit Markdown puis on écrit le titre
# Les mots résérvés en python
#exécuter le markdown pour qu'il soit affiché comme un titre sans #

import keyword #importer le package
listdekeyword=keyword.kwlist # affichage des mots résérvé en liste
print(listdekeyword) # afficher la liste
print(len(listdekeyword)) #afficher la taille de la liste


#Les types de données en python

#les types de données natifs en python :
#1 int
#2 float
#3 complex
#4 bool
#5 str
#6 bytes
#7 bytearray
#8 range
#9 list
#10 tuple
#11 set
#12 frozenset
#13 dict
#14 None


a=20
b=62.5
c=2+3j
d='test'