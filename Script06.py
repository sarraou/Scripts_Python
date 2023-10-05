# Décrire un programme qui va lire les données d'un employé à partir du clavier
# identifiant, nom, salaire, adresse, marié

identifiant = int(input("Veuillez saisir votre identifiant : \n"))
nom = input("Veuillez saisir votre nom : \n")
salaire = float(input("Veuillez saisir votre salaire : \n"))
adresse = input("Veuillez saisir votre adresse : \n")
marié = bool(input("Est ce que vous êtes marié ? [True/False] \n"))

#print("L'employé ", nom, " qui a l'identifiant ", identifiant, " et le salaire ", salaire, " habite à " , adresse, " est : ", marié, " marié ")
print("svp confirmez vos informations personnelles")
print("L'identifiant de l'employé est : " , identifiant)
print("Le nom de l'employé est : " , nom)
print("Le salaire de l'employé est : " , salaire)
print("L'adresse de l'employé est : " , adresse)
print("Est ce que l'employé est marié ? " , marié)

