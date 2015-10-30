# -*- coding: utf-8 -*-
import numpy as np
import random
import copy
import matplotlib.pyplot as plt
import timeit
import evaluation
import johnson
from arbre import arbre
import instances

inf = float('Inf')
A, B, C = range(0,3)

def arbre_(n, m=3):
    d = instance4(n, m)
    pi = []
    piprime = np.array(range(np.size(d, 0)))
    depth = 0
    sol, time = arbre(d, pi, piprime, depth)

def main():
    arbo_exectime = [timeit.timeit('arbre_({})'.format(n), number=100) for n in range()]
    plt.plot(arbo_exectime)
    plt.ylabel('Arbo')
    plt.show()

if __name__ == "__main__":
    main()
