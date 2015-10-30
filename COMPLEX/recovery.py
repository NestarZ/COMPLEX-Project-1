# -*- coding: utf-8 -*-
import numpy as np
import random
import copy
import matplotlib.pyplot as plt
import timeit
import evaluation
import johnson
import arbre
import instances

inf = float('Inf')
A, B, C = range(0,3)

def main():
    S, EVALJohn, EVALArbo = [],[],[]
    n,m = 3,3
    for T in range(2):
        start = time.time()
        # Constrution des durées
        d = instances.instance3(n, m)
        print("Data: \n{}\n".format(d))
        # Algorithme approché avec garantie de performance (notre solution est 3-approché)
        solution1 = johnson.Johnson(d)
        print("Johnson: {}\n".format((sol1, evaluation.evaluation(d, sol1, []))))
        # Méthode exacte
        ## Initialisation
        pi, piprime, depth = [], np.array(range(np.size(d, 0))), 0
        ## Algorithme arborescent
        solution2 = arbre.Arbo(d, pi, piprime, depth)
        print("Méthode exacte: {}\n".format(solution2))
        S.append(sol1[1] >= sol2[1]))
        print("Résultat cohérent ? {}\n".format(bool(S[-1])))
        end = time.time()
        EVALJohn.append(timeit.timeit())
        EVALArbo.append(timeit.timeit())
        n += 1
    print(100*sum(S)/len(S),'%')
    print(EVALArbo)
    plt.plot(EVALArbo)
    plt.ylabel('Arbo')
    plt.show()

if __name__ == "__main__":
    main()
