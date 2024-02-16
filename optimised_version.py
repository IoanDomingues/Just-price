from random import randint


choixe_level = int(input('Choissiez votre niveau 1/2'))

def just_pricee(level):
    erreur = 0
    just_price = randint(0, level)
    choix_price = int(input('Donne un nombre'))
    while choix_price != just_price:
        if choix_price < just_price:
            choix_price = int(input('C est plus grand. Donne un nombre'))
        elif choix_price > just_price:
            choix_price = int(input('C est plus petit. Donne un nombre'))
        erreur += 1
    print(f'Bravo tu a trouvé le nombre mystere qui était {just_price} en seulement {erreur} tentative')


if choixe_level == 1:
    just_pricee(1000)
elif choixe_level == 2:
    just_pricee(1000)
else:
    print('Désoler ce niveaux n existe pas ')
