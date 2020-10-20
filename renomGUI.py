import tkinter
import os
import re
from tkinter import messagebox

# Fct permettant d'afficher ds le terminal l'état des radioButton à chaque changement
def update_observer(*args):
    if var_choix.get():
        print("Confirmation changement OUI")
    else:
        print("Confirmation changement NON")

def renommage(*args):
    increment = ent_increment.get()
    testincr = bool(re.match('\d{1,3}$', increment)) #On test pour voir si l'increment est valide

    if not testincr: #On teste ici l'increment pour voir si l'utilisateur a bien respecté la consigne
        tkinter.messagebox.showerror("Erreur","Mauvais increment")
        app.quit()

    # On récupere le choix de l'utilisateur pour savoir ce qu'il souhaite faire du nom original
    if var_choix.get(): #Si il veut garder le mot on récupere le nombre de caractères souhaités
        original = "o"
        nb=ent_original.get()
        nb=int(nb)
    else:
        original = "n"

    # On gere ici le cas du rajout de la part de l'utilisateur
    if not ent_rajout.get().split(): #Si la zone est vide on ne rajoutera pas de texte
        texte="n"
    else:
        texte="o"
        rajout = ent_rajout.get()

    # Ici on utilise les conditions qui étaient dans la version simple du
    # code avec quelques modif au niveau des variables
    if texte == "o" and original == "o":
        for file in fichier:
            if nb > len(file) - 4:
                tkinter.messagebox.showerror("Erreur","Mauvais nombre de caracteres à garder")
            nfc = os.path.join(rep, file)
            fileName, fileExtension = os.path.splitext(nfc)
            if os.path.isfile(nfc):
                os.rename(nfc, os.path.join(rep, increment + " - " + rajout + " - " + file[nb:-4] + fileExtension))
                increment = int(increment)
                increment = increment + 1
                increment = str(increment)

    elif texte == "o" and original == "n":
        for file in fichier:
            nfc = os.path.join(rep, file)
            fileName, fileExtension = os.path.splitext(nfc)
            if os.path.isfile(nfc):
                os.rename(nfc, os.path.join(rep, increment + " - " + rajout + fileExtension))
                increment = int(increment)
                increment = increment + 1
                increment = str(increment)

    elif texte == "n" and original == "o":
        for file in fichier:
            if nb > len(file) - 4:
                print("Nombre trop grand !")
                break
            nfc = os.path.join(rep, file)
            fileName, fileExtension = os.path.splitext(nfc)
            if os.path.isfile(nfc):
                os.rename(nfc, os.path.join(rep, increment + " - " + file[nb:-4] + fileExtension))
                increment = int(increment)
                increment = increment + 1
                increment = str(increment)

    elif texte == "n" and original == "n":
        for file in fichier:
            nfc = os.path.join(rep, file)
            fileName, fileExtension = os.path.splitext(nfc)
            if os.path.isfile(nfc):
                os.rename(nfc, os.path.join(rep, increment + fileExtension))
                increment = int(increment)
                increment = increment + 1
                increment = str(increment)


rep="renommage"
fichier = os.listdir(rep)
texte = ""
original = ""

app = tkinter.Tk()
#On clacule ici pour que la fenetre pop au milieu de l'écran
screen_x = int(app.winfo_screenwidth())
screen_y = int(app.winfo_screenheight())
window_x = 400
window_y = 350

posX = (screen_x // 2) - (window_x // 2)
posY = (screen_y // 2) - (window_y // 2)

geo = "{}x{}+{}+{}".format(window_x, window_y, posX, posY)
app.geometry(geo)
app.title("Renommage")

# Partie increment

label_increment = tkinter.Label(app, text="Entrez votre increment !")
ent_increment = tkinter.Entry(app)

# Texte original

label_original = tkinter.Label(app, text="Souhaitez vous garder le titre original ?")

var_choix = tkinter.IntVar()
var_choix.trace("w", update_observer)
rad_original1 = tkinter.Radiobutton(app, text="oui", value=1, variable=var_choix)
rad_original2 = tkinter.Radiobutton(app, text="non", value=0, variable=var_choix)

label_original2 = tkinter.Label(app, text="Combien de caractères à garder ?")
ent_original = tkinter.Entry(app)

# Texte à rajouter

label_rajout = tkinter.Label(app, text="Entrez le texte à rajouter (laissez vide sinon)")
ent_rajout = tkinter.Entry(app)

# Bouton pour tout lancer

btn_valider = tkinter.Button(app, text="Valider", command=renommage)

# ajout des différents widgets
label_increment.pack(pady=(20, 0))
ent_increment.pack()

label_original.pack(pady=(30, 0))
rad_original1.pack()
rad_original2.pack()
label_original2.pack()
ent_original.pack()

label_rajout.pack(pady=(40, 0))
ent_rajout.pack()

btn_valider.pack()

app.mainloop()