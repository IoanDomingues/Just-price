def level1():
    from random import randint

    # choisir un nombre aleatoire entre 1 et 1000
    just_price = randint(1, 1000)

    # statut du jeu (activé/désactivé)
    running = True

    while running:

        user_price = int(input("Entrer un prix"))

        # si le prix est le meme que le juste prix
        if user_price == just_price:
            print("Trouvé !")
            # fin du jeu
            running = False

        # si le prix de l'utilisateur est supérieur au prix à trouver
        elif user_price > just_price:
            print("C'est moins")

        # si le prix de l'utilisateur est inférieur au prix à trouver
        elif user_price < just_price:
            print("C'est plus")

def level2():
    from random import randint

    # choisir un nombre aleatoire entre 1 et 1000
    just_price = randint(1, 10000)

    # statut du jeu (activé/désactivé)
    running = True

    # tant que le jeu est en cours d'éxécution
    while running:

        user_price = int(input("Entrer un prix"))

        # si le prix est le meme que le juste prix
        if user_price == just_price:
            print("Trouvé !")
            # fin du jeu
            running = False

        # si le prix de l'utilisateur est supérieur au prix à trouver
        elif user_price > just_price:
            print("C'est moins")

        # si le prix de l'utilisateur est inférieur au prix à trouver
        elif user_price < just_price:
            print("C'est plus")

level1()
print("Fin du niveau 1, vous avez gagné !\n Vous passez au niveau suivant !")

level2()
print("Fin du jeu, vous avez gagné !")