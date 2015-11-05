# -*- coding: utf-8 -*-
import numpy as np
import random
import copy
import matplotlib.pyplot as plt
import timeit
import evaluation
from johnson import johnson
from arbre import arbre
from instances import *

def john_(k, n, m=3, debug=False, d=None, **kwargs):
    """
    Fonction interface avec la méthode approchée de Johnson.
    Récupère un type d'instance et effectue l'ordonnancement
    sur une instance de ce type (n=#taches, m=#machines).
    Il est aussi possible d'envoyer directement un jeu de donnée.
    """

    if d == None: d = instances_dict[k][0](n, m)
    if debug: print(d)
    sol, time = johnson(d)
    return sol, time

def arbre_(k, n, m=3, debug=False, d=None, **kwargs):
    """
    Fonction interface avec la méthode exacte.
    Récupère un type d'instance et effectue l'ordonnancement
    sur une instance de ce type (n=#taches, m=#machines).
    Il est aussi possible d'envoyer directement un jeu de donnée.
    Possibilité d'envoyer en argument un alpha pour avoir
    une solution approchée avec garantie de qualité (a-approchée)
    par cette méthode.
    """

    if d == None: d = instances_dict[k][0](n, m)
    if debug: print(d)
    pi, piprime = [], np.array(range(np.size(d, 0)))
    depth, sol = 0, None
    sol, time = arbre(d, pi, piprime, depth, sol, debug, kwargs.get('alpha',0))
    return sol, time

def test(a=0):
    """
    Vérifie si la méthode exacte renvoie bien des durées
    inférieures à celles de la méthode approchée de Johnson.
    a : solution approchée avec garantie de qualité (a-approchée)
    par la méthode arborescente.
    """

    ass = []
    debug = False
    n, m = 6, 3
    for k in range(200):
        k = np.random.randint(len(instances_dict))
        d = instances_dict[k][0](n, m)
        sol1, time1 = john_(k, n, m, debug, d)
        sol2, time2 = arbre_(k, n, m, debug, d, alpha=a)
        ass.append(int(time1 >= time2))
    print(sum(ass)/len(ass)*100,"%")

def main(algo, max_n, alpha=0):
    """
    Trace les courbes du temps d'éxecution d'une méthode pour chaque type
    d'instance en fonction du nombre de tâche.
    algo : Nom de la méthode et de sa fonction.
    max_n : Nombre maximum de tâches d'un jeu de donnée.
    alpha : Utile pour rendre approchée la méthode arborescente. (Voir fonction)
    """

    print(algo)
    s = "from __main__ import {}".format(algo)
    tailles = range(1, max_n)
    exectime = [[timeit.timeit('{}({}, {}, alpha={})'.format(algo, k, n, alpha), number=100, setup=s) for n in tailles] for k in range(len(instances_dict))]
    fig = plt.figure()
    ax = plt.subplot(111)
    for i, c in enumerate(exectime):
        ax.plot(tailles, c, label='{}'.format(instances_dict[i][1]))
    ax.legend()
    plt.ylabel('{}exec_time'.format(algo))
    plt.xlabel('nb_taches')

if __name__ == "__main__":
    # Elagage des noeuds dont leur score est 10%
    # inférieur au score de la solution courante
    a = 0.4
    # test(a)
    max_taches = 7
    #main(john_.__name__, max_taches)
    main(arbre_.__name__, max_taches, alpha=0)
    plt.show()
