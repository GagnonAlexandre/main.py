# TP2
# creer par Alexandre Gagnon le jeudi le 13 oct
# on import random
import random


def jeuxdevinette():
    # on crée une variable qui s'appellera NOMBRE
    lol = int(input("Entrez votre premier nombre "))
    lol2 = int(input("Entrez votre deuxième nombre "))

    NOMBRE = random.randint(lol, lol2)
    # on crée une autre variable"le_nombre_de_essai" et le nombre d'essai est le nombre de fois que la personne va faire un essaye
    le_nombre_de_essai = 0
    # on fabrique une autre variable pour le nombre d'essaie max,
    # on crée une variable qui s'appelle try comme ca à chaque fois que le joueur esseyera une autre fois, on ajoute tryy au nombre d'essaie, on fait cela continuellement
    tryy = 1
    # on crée une variable qui s'appelle x qui sera le nombre choisi par le joueur, donc on fera un input avec ceci et il entra le nombre choisi pour le guess
    x = 0
    # on va créer une variable qui s'applle retryy afin que la peersonne écris o/n
    retryy = ""
    # jouer = vrai
    jouer = True
    # print la phrase de bienvenue
    print('Bonjour, le but du jeux est de deviner le nombre choisi entre', lol, '-', lol2,
          ' par le systeme en le moin de coup possible, vous avez 10 chance au max')
    # on crée un while jouer, tous se retrouve dedans, tant qu'il est vrai
    while jouer:
        # tant que x est inégale au nombre de l'ordi et que le nombre d'essaie est plus que dix
        while x != NOMBRE and le_nombre_de_essai <= maxessai:
            # x = a un integer que le jouer va entrez dans intput
            x = int(input("Entrez votre nombre:"))
            # si le nombre entrez est plus grand
            if int(x) > NOMBRE:
                # on additionne un essaie
                le_nombre_de_essai = le_nombre_de_essai + tryy
                # print que le nombre est plus grand
                print("Votre nombre est plus grand que celui de l'ordi!")
                # print le nombre d'essaie du joueur
                print(" Vous êtes à", le_nombre_de_essai, "nombres d'essais")
            # si x < que le nombre de l,ordi
            elif int(x) < NOMBRE:
                # on additione 1 au nombre d'essaie a chaque fois il essaie.
                le_nombre_de_essai = le_nombre_de_essai + tryy
                # print le nombre plus petit
                print("Votre nombre est plus petit que celui de l'ordi!")
                # le nombre d,essaie il est rendu
                print(" Vous êtes à", le_nombre_de_essai, "nombres d'essais")
                # autre
            else:
                # print message gagnant
                print('Vous avez deviner le nombre, lol vous êtes trop fort!')
                # print nombre d'essais utiliser
                print("Vous avez utiliser", le_nombre_de_essai, "nombre d'essaie")

                # vouler vous reéssayer de jouer
                retryy = input("ah Nice vous avez gagné, vous êtes très bon, get bad, voulez vous recommencer o/n!:")
            if retryy == "n":
                print('byebye')
                jouer = False
            elif retryy == "o":
                jeuxdevinette()

            if le_nombre_de_essai >= maxessai and x != NOMBRE:
                print('le nombre est', NOMBRE)
                retryy = input(
                    "ah cest chien vous avez utiliser tous vos essaie, o/n!:")


jeuxdevinette()
import random


def jeuxdevinette():