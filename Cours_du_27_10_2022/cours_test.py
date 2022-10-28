
def Explication(): # Fonction qui explique le fonctionnement d'un script
    #Ici mon commentaire

    print("Hello World")

    """Exemple e commentaire
    """

    x = 3
    y = "Salut"

    print(x)
    print(y)

    a = float(3)
    print(type(a))
    print(a)

    # a = b = c = 1

    fruit = ["Pomme", "Banane", "Poire"]
    x,y,z = fruit

    print(x,y,z)

    x = "awesome"
    y = "Python is "
    z = "DOG"
    print(y,z,x)

    Changer le type d'une valeur
    a = 5
    b = "Texte"
    print(str(a) + b)

#------------------------------------------------------------------------------------------


def maFaction():
    global x
    x = "Merveilleux"
    print("Python est " + x)

maFaction()

print("Ma variable x est de type : " + str(type(x)) + " et sa valeur est : " + x)

#------------------------------------------------------------------------------------------

for x in "Cerise":
    print(x)

#-------------------------------------------------------------------------------------
    
# afficher le nombre de caractère d'une chaine de caractère
y = "Cerise"
print(len(y))


#-------------------------------------------------------------------------------------

# Comment vérifier qu'un mot est dans ma chaine ?
exemple = "Voici ma chaine"
print("ma" in exemple)

#-------------------------------------------------------------------------------------

# Vérifier si un mot n'est pas dans ma chaine
x = "ma"
if x in "ma chaine":
    print("Le mot est dans la chaine")
else: 
    print("non")


#-------------------------------------------------------------------------------------

#Le slaching 
b = "Hello, World!"
print(b[2:5])


#-------------------------------------------------------------------------------------

# Tout en majuscule
a = "Hello, World!"
print(a.upper())


#-------------------------------------------------------------------------------------

# Comment supprimer les espaces avant et après une chaine de caractère
b = " Hello, World! "
print(b.strip()) # returns "Hello, World!"



#-------------------------------------------------------------------------------------

# Comment remplacer une valeur dans une chaine de caractère
b = "Hello, World!"
print(b.replace("H", "J"))


#-------------------------------------------------------------------------------------

# Exemple d'utilisation d'un split
a = "Hello, World!"
b = a.split(",")
print(b)


#-------------------------------------------------------------------------------------

# ajouter un " " entre 2 chaines
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#-------------------------------------------------------------------------------------

# Exemple d'utilisation d'un format
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))


#-------------------------------------------------------------------------------------

# Exemple d'utilisation d'un format à la suite
taille = 1.80
age = 36
txt = "My name is John, and I am {} and my taille is {} m"
print(txt.format(age, taille))


#-------------------------------------------------------------------------------------

# Changer le sens d'appaition des variables
taille = 1.80
age = 36
txt = "My name is John, and I am {1} and my taille is {0} m"
print(txt.format(age, taille))


#-------------------------------------------------------------------------------------

# Rappel rapide sur les échapements
txt = "We are the so-called \"Vikings\" from the north."
print(txt)


#-------------------------------------------------------------------------------------

# Sur les booléens
print(10 > 9)
print(20 == 20)
print(10 < 9)

a = 200
b = 33
if a > b:
    print("a est plus grand que b")
else:
    print("c'est pas possible !")

#-------------------------------------------------------------------------------------


# Evaluation sur une variable
print(bool("test"))
print(bool(3))
print(bool(True))

#-------------------------------------------------------------------------------------


# Et dans une classe

class maClasse():  # Création d'une classe
    def __init__(self, nom, age): # def __init__ est un constructeur
        self.nom = nom # self est une variable qui représente l'objet lui même
        self.age = age 

monObject = maClasse("Jean", 36)
print(bool(monObject))


#-------------------------------------------------------------------------------------

# La fonction peut retourner en true

def maFonction():
    return True

print(maFonction())

#-------------------------------------------------------------------------------------

# Tester une fonction ou résultat via un if... trivial

def maFonction():
    return True

if maFonction():
    print("C'est vrai")
else:
    print("C'est faux")

#-------------------------------------------------------------------------------------
   
# J'aimerais vérifier si une variable est un nombre entier ou non
print(type(3) == int)
if type(3) == int:
    print("C'est un entier")
else:
    print("Ce n'est pas un entier")

#-------------------------------------------------------------------------------------
    
#Plus court

print(isinstance(3, int))

#-------------------------------------------------------------------------------------

# Les listes
maliste = ["Pomme", "Banane", "Poire"]
print(maliste)
print(len(maliste))
print(type(maliste))

#-------------------------------------------------------------------------------------

# Constructeur de liste
maliste = list(("Pomme", "Banane", "Poire"))
print(maliste)

#-------------------------------------------------------------------------------------

# Comment remplacer une valeur dans une liste ?
maliste = ["Pomme", "Banane", "Poire"]
maliste[2] = "Fraise"
print(maliste)

#-------------------------------------------------------------------------------------

# Comment ajouter une valeur dans une liste ? append = ajout à la fin , extend = ajout à la fin, insert = ajout à l'index ( une liste)
maliste = ["Pomme", "Banane", "Poire"]
exemple = ["Abricot", "Cerise"]
maliste.append("Fraise")
maliste.extend(exemple)
print(maliste)

#-------------------------------------------------------------------------------------

#la methode pour supprimer une valeur dans une liste
maliste = ["Pomme", "Banane", "Poire"]
maliste.pop(1)
print(maliste)

#-------------------------------------------------------------------------------------

#le mot clef del permet de supprimer une element de la liste ou la liste elle même 
maliste = ["Pomme", "Banane", "Poire"]
del maliste[1]
print(maliste)
del maliste
print(maliste)

#-------------------------------------------------------------------------------------

#Vider une liste
maliste = ["Pomme", "Banane", "Poire"]
maliste.clear()
print(maliste)

#-------------------------------------------------------------------------------------

#Parcourir une liste 
maliste = ["Pomme", "Banane", "Poire"]
for x in maliste:
    print(x)

#-------------------------------------------------------------------------------------

# En passant par la longueur de la liste
maliste = ["Pomme", "Banane", "Poire"]
for x in range(len(maliste)):
    print(maliste[x])

#-------------------------------------------------------------------------------------

#Version plus court 
maliste = ["Pomme", "Banane", "Poire"]
[print(x) for x in maliste]

#-------------------------------------------------------------------------------------

#D'autres exemple sans comprehension

maliste = ["Pomme", "Banane", "Poire", "Abricot", "Cerise"]
newliste = []
for x in maliste:
    if "a" in x:
        newliste.append(x)
print(newliste)

#-------------------------------------------------------------------------------------

#Avec comprehension

maliste = ["Pomme", "Banane", "Poire", "Abricot", "Cerise"]
newliste = [x for x in maliste if "a" in x]
print(newliste)

#-------------------------------------------------------------------------------------

#Exercice

list1 = range(3)
list2 = range(5)
print(list1,list2)

#-------------------------------------------------------------------------------------

#Ordonner une chaine de caractère dans l'ordre alphabétique

chaine = ["Vincenzo", "Jean", "Pierre", "Paul", "Jacques", "Marie", "Lucie", "Julie", "Julien", "Juliette"]
chaine_ordonnee = sorted(chaine)
chaine_line = ", ".join(chaine_ordonnee)
print(chaine_line)

#-------------------------------------------------------------------------------------

#Exercice 
"""
Afficher la postion de chaque lettre d'un mot
boucle sur toute la longueur de la chaine 
reutiliser la find ( par exemple string.find(value, start, stop)
faire une recherche à partir de la pos1
"""

chaine = "Bonjour"
for x in range(len(chaine)):
    print(chaine.find(chaine[x], x))

#-------------------------------------------------------------------------------------
