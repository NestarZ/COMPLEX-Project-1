import numpy as np
import random

def instance1(n,m):
    print(n)
    # Données non-corrélées
    a, b = np.ones((n,m)), 100*np.ones((n,m))
    return np.int32(np.random.uniform(a, b))

def instance2(n,m):
    print(n)
    # Corrélation sur les durées d'éxecution
    r = np.array([random.sample({0,1,2,3,4}, 1) for k in range(n)])
    a, b = 20*r*np.ones((n,m)), 20*r*np.ones((n,m)) + 20
    return np.int32(np.random.uniform(a, b))

def instance3(n,m):
    print(n)
    # Corrélation sur les machines
    a, b = (np.hstack([1*np.ones((n,1)), 2*np.ones((n,1)), 3*np.ones((n,1))]),)*2
    a, b = 15*(a-1)+1, 15*(b-1)+100
    return np.int32(np.random.uniform(a, b))

def instance4(n=None,m=None):
    d = np.array([[2, 3, 4],[2, 3, 5], [9, 4, 1]]) # durées taches/machines
    #d = np.array([[1, 8, 4],[2, 4, 5], [6, 2, 8], [3, 9, 2]]) # durées taches/machines
    #d = np.array([[22, 39, 45], [75, 35, 66], [ 7, 53, 31]])
    return d
