def chiffrePorteBonheur(nb):
    ch=str(nb)
    somme=100
    while somme >= 10:
        somme=0
        for i in ch:
            somme += int(i) ** 2
        ch=str(somme)

    if somme==1:
        return str(nb)+" est un nombre chanceux"
    else:
        return str(nb)+" n'est pas un nombre chanceux"

print(chiffrePorteBonheur(913))

# SORTIE
# 913  est un nombre chanceux