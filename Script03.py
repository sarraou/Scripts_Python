#Découpage d'une chaine de caractère (Slicing)
Collège = "Collège Bois de Boulogne "
#accedere à un caractère spécifique via l'indice
print(Collège[0],Collège[1])
print(Collège[2])
print(Collège[3])
print(Collège[20])
print(Collège[-2]) #pour commencer à l'inverse ==> n

print(Collège[8:11]) #inclus le premier indice 8 et pas le dernier 11 ==> Boi
print(Collège[8:12]) #==> Bois
#print(Collège[16:24])
print(Collège[-9:-1])#ajouter un espace à la fin de la phrase pour commencer le calcul du -1
print(Collège[0:20:2]) #afficher le caractere avec un saut de 2 jusqu'au caractere 20
print(Collège[0:20:3]) #afficher le caractere avec un saut de 3 jusqu'au caractere 20

print(len(Collège))#longueur
print(Collège[:])#afficher toute la chaine de caractere
print(Collège[::])#mm chose avec debut à la fin puis la troisieme c'est le pas
print(Collège[::-1])#print(Collège[start:end:step]) (saut/le pas)

