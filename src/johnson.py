import numpy as np
from evaluation import *

def johnson(d, debug=False):
    """
    Méthode approchée avec garantie de performance (Johnson)
    d = Jeu de donnée
    """

    assert np.size(d, 1) > 1, "2 machines au moins"
    if debug and np.size(d, 1) != 2: print("Attention: Seul les deux premières machines sont pris en compte.")

    n, m = np.size(d, 0), 3
    A, B, C = range(0,m)
    X = list(range(0,n))
    G = list()
    D = list()

    while X:
        # Chaque tâche ayant été traité voit ses durées mettre à NaN.
        # np.nanargmin récupère ensuite la position dans la matrice
        # où la durée minimum est située.
        pos = np.nanargmin([[d[i,j] if i in X else np.nan for j in [A,B]] for i in range(n)])

        # Je déduit ensuite la ligne et la colonne correspondant à cette position
        # i.e. la machine et la tâche.
        i, j = pos//(m-1), pos%(n-1)

        # Si la durée de la tâche appartient à la machine A
        # je la met dans ma liste de gauche G, sinon je l'insère
        # dans ma liste de droite en première position.
        G.append(i) if j == A else D.insert(0, i)

        # Ma tâche en cours est traitée
        X.remove(i)

    return G + D, evaluation(d, G+D, [])

if __name__ == "__main__":
    from instances import *
    d = instance2(50,3)
    sol, time = johnson(d, True)
    print(sol, time)
