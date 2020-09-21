#1

temps = 6.892
distance = 19.7
vitesse = distance/temps
print("La vitesse est ", vitesse)
print("La vitesse est ", round(vitesse,2))

#2

nom = str(input("Entrez un nom\n"))
age = int(input("Entrez un age\n"))
print(nom,age)

#3
import math

valeur=float(input("Entrez un flottant\n"))
if(valeur<0):
    print("ERREUR")
else:
    print(math.sqrt(valeur))

#4

mot1=str(input("Entrez le premier mot\n"))
mot2=str(input("Entrez le deuxième mot\n"))

if mot1<mot2:
    print(mot1)
elif mot2<mot1:
    print(mot2)
else:
    print("Les deux mots entrés sont identiques")


#5

pSeuil = 2.3
vSeuil = 7.41

pUser = float(input("Entrez la pression courante de l'enceinte"))
vUser = float(input("Entrez le volume courant de l'enceinte"))

if pUser>pSeuil and vUser>vSeuil:
    print("ARRET IMMEDIAT")
elif pUser>pSeuil:
    print("Augmenter le volume de l'enceinte")
elif vUser>vSeuil:
    print("Diminuer le volume de l'enceinte")
else:
    print("Tout va bien")


#6

email=input("Entrez votre chaine de caractères\n")
if "@" in email and email.endswith(".com"):
    print("Email valide")
else:
    print("Email invalide")


#7

for i in range(10):
    print("Ce message s'affiche 10 fois")

#8

mot = "Maroc"
for i in mot:
    print(i)

#9

a = 0
b = 10
for i  in range(a,b):
    print(i)

#10

for i in range(10,0,-1):
    if i%2!=0:
        print(i)

#11

filtr = int(input("Entrez une valeur entre 1 et 10 compris\n"))
while filtr<1 or filtr>10:
    filtr = int(input("Veuillez entrer une valeur entre 1 et 10 compris"))

#12

ch = "maroc"
liste= ['r','a','b','a','t',]
for i in ch:
    print(i)
print("\n")
for i in liste:
    print(i)


#13

for i in range(0,15,3):
    print(i)

#14

n = 20
for i in range(0,n+1):
    if i%2==0:
        print(i)

i=0
while i<=n:
    if i%2==0:
        print(i)
    i+=1


#15

liste =[17,38,10,25,72]
liste.sort()
print(liste)
liste.append(12)
print(liste)
liste.reverse()
print(liste)
print(liste.index(17))
liste.remove(38)
print(liste)
print(liste[2:3])
print(liste[:2])
print(liste[2:])
print(liste[:])


#16

chaine = "Maroc"
print(chaine[::-1])


#17

ch ="amma"
if(ch==ch[::-1]):
    print(ch,"est un palindrome")
else:
    print(ch,"n'est pas un palindrome")

#18

mail="nabil@gmail.com"
if "@" in mail  and (mail.endswith("."+mail[-3:]) or mail.endswith("."+mail[-2:]) or mail.endswith("."+mail[-1:])):
    print("Email valide")
else:
    print("Email invalide")

#19

truc = []
machin = [0.0,0.0,0.0,0.0,0.0]
print(truc)
print(machin)

#20

for i in range(0,4):
    print(i)
for i in range(4,8):
    print(i)
for i in range(2,9,2):
    print(i)
chose = [0,1,2,3,4,5]

if 3 in chose:
    print("3 est bien dans chose")
else:
    print("3 n'est pas dans chose")

if 6 in chose:
    print("6 est bien dans chose")
else:
    print("6 n'est pas dans chose")

#21

x = int(input("Entrez un nombre x"))
fichier = open("cours1.txt","a")
for i in range(x) :
    ch = input("Entrez une chaîne de caractère:")
    fichier.write(ch+"\n")
fichier.close()

#22

fichier = open('cours1.txt', "r")
for ligne in fichier:
    if "@" in ligne and ligne.endswith(".com\n"):
        print("Email valide")
    else:
        print("Email non valide")

fichier.close()

#23

def compterMots(ch) :
  dict={}
  for i in ch.split():
        if i in dict:
            dict[i]+=1
        else :
            dict[i]= 1
  return dict

print(compterMots("le maroc est vraiment un beau pays le maroc"))

#24

import math

def volumeSphere(r):
    return 4/3*math.pi*cube(r)

def cube(r):
    return r**3

print(volumeSphere(5))

#25

def somme(a,b,c):
    return a+b+c

a,b,c=(1,2,3)
print(somme(a,b,c))
