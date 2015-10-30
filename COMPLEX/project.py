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

instances_dict = [(instance1,"Données non-corrélées"),
                  (instance2,"Corrélation sur les durées d'éxecution"),
                  (instance3, "Corrélation sur les machines")]
                  #,(instance4, "Exemple du sujet")]

def john_(k, n, m=3, debug=False, d=None):
    if d == None: d = instances_dict[k][0](n, m)
    if debug: print(d)
    sol, time = johnson(d)
    return sol, time

def arbre_(k, n, m=3, debug=False, d=None):
    if d == None: d = instances_dict[k][0](n, m)
    if debug: print(d)
    pi, piprime = [], np.array(range(np.size(d, 0)))
    depth, sol = 0, None
    sol, time = arbre(d, pi, piprime, depth, sol, debug, 0.3)
    return sol, time

def main(algo, max_n):
    print(algo)
    s = "from __main__ import {}".format(algo)
    tailles = range(1, max_n)
    exectime = [[timeit.timeit('{}({}, {})'.format(algo, k, n), number=100, setup=s) for n in tailles] for k in range(len(instances_dict))]
    fig = plt.figure()
    ax = plt.subplot(111)
    for i, c in enumerate(exectime):
        ax.plot(tailles, c, label='{}'.format(instances_dict[i][1]))
    ax.legend()
    plt.ylabel('{}exec_time'.format(algo))
    plt.xlabel('nb_taches')

def test():
    ass = []
    debug = False
    n, m = 5, 3
    for k in range(200):
        k = np.random.randint(len(instances_dict))
        d = instances_dict[k][0](n, m)
        sol1, time1 = john_(k, n, m, debug, d)
        sol2, time2 = arbre_(k, n, m, debug, d)
        ass.append(int(time1 >= time2))
    print(sum(ass)/len(ass)*100,"%")

if __name__ == "__main__":
    #test()
    max_taches = 20
    main(john_.__name__, max_taches)
    main(arbre_.__name__, max_taches)
    plt.show()
