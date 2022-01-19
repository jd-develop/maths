#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import math


def primalite(n, do_i_print: bool = True):
    """ Vérif primalité """
    if n < 0:
        print("Les nombres négatifs ne peuvent être premier")
        return False
    elif n == 1 or n == 0:
        return False
    elif n == 2:
        return True
    if type(n) != int:
        raise TypeError("Le nombre doit être un entier naturel")

    div = 2  # on part de 2 comme diviseur
    if do_i_print:  # on affiche la racine carrée du nombre dont on teste la primalité
        print("La racine carrée de", n, "est environ égale à", int(math.sqrt(n)))
    while div <= math.sqrt(n):
        if n % div == 0:  # n est divisible par div
            if do_i_print:  # si on doit afficher les divisibilités
                if primalite(div, False):
                    # si le diviseur est premier : le reste des cas n'est pas intéressant puisqu'il est compris dans
                    # les nbs premiers (cf. propriété de la décomposition en produits de facteurs premiers)
                    print(n, "est divisible par", div)
            return False  # il n'est pas premier puisqu'il admet comme diviseur un autre nombre que lui-même ou un
        else:
            if do_i_print:
                if primalite(div, False):
                    print(n, "n'est pas divisible par", div)   # idem qu'au dessus
        div += 1
    return True  # à la fin s'il n'y a pas eu de return False c'est que le nombre est forcément premier


print("Entrez stop ou exit pour arrêter le programme")
stops = ["stop", "exit"]
while True:
    try:
        nb = eval(input("Entrez nombre pour tester primalité : "))  # on demande une valeur
        if nb in stops:  # si l'utilisateur entre 'stop', il va appeler la variable 'stops', qui contient les stops
            break
        print(nb, "est premier" if primalite(nb) else "n'est pas premier")  # on affiche le nb puis 'est 1er' s'il l'est
    except Exception as e:
        # il peut survenir des erreurs
        print("Suite à l'erreur", e.__class__.__name__, "votre demande n'a pas pu être traitée. ({})".format(e))
