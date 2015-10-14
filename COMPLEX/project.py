# -*- coding: utf-8 -*-
import numpy as np
import random
inf = float('Inf')

def Johnson(d):
    n = np.size(d, 0)
    m = np.size(d, 1)
    A, B, C = range(0,m)
    X = list(range(0,n))
    G = list()
    D = list()
    while X:
        pos = np.argmin([[d[i,j] if i in X else +inf for j in [A,B]] for i in range(n)])
        i, j = pos//(n-1), pos%(n-1)
        G.append(i) if j == A else D.insert(0, i)
        X.remove(i)
    return G + D

# Données type
n, m = 3, 3 # nb taches, nb machines
d = np.array([[2, 3, 4],[2, 3, 5], [9, 4, 1]]) # durées taches/machines

# Données non-corrélées
a, b = np.ones((n,m)), 100*np.ones((n,m))

# Corrélation sur les durées d'éxecution
r = np.array([random.sample({0,1,2,3,4}, 1) for k in range(n)])
a, b = 20*r*np.ones((n,m)), 20*r*np.ones((n,m)) + 20

# Corrélation sur les machines
a, b = (np.hstack([1*np.ones((n,1)), 2*np.ones((n,1)), 3*np.ones((n,1))]),)*2
a, b = 15*(a-1)+1, 15*(b-1)+100

# Constrution des durées
d = np.int32(np.random.uniform(a, b))

print(d)
print(Johnson(d))
