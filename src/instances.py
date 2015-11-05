import numpy as np
import random

def instance1(n,m):
    """
    Données non-corrélées
    """
    print("1: nb_taches:", n)
    a, b = np.ones((n,m)), 100*np.ones((n,m))
    return np.int32(np.random.uniform(a, b))

def instance2(n,m):
    """
    Corrélation sur les durées d'éxecution
    """
    print("2: nb_taches:", n)
    r = np.array([random.sample({0,1,2,3,4}, 1) for k in range(n)])
    a, b = 20*r*np.ones((n,m)), 20*r*np.ones((n,m)) + 20
    return np.int32(np.random.uniform(a, b))

def instance3(n,m):
    """
    Corrélation sur les machines
    """
    print("3: nb_taches:", n)
    a, b = (np.hstack([1*np.ones((n,1)), 2*np.ones((n,1)), 3*np.ones((n,1))]),)*2
    a, b = 15*(a-1)+1, 15*(b-1)+100
    return np.int32(np.random.uniform(a, b))

def instance4(n=None,m=None):
    """
    Exemple du sujet ou exemples connus
    """
    d = np.array([[2, 3, 4],[2, 3, 5], [9, 4, 1]]) # durées taches/machines
    #d = np.array([[1, 8, 4],[2, 4, 5], [6, 2, 8], [3, 9, 2]]) # durées taches/machines
    #d = np.array([[22, 39, 45], [75, 35, 66], [ 7, 53, 31]])
    return d


instances_dict = [(instance1,"Données non-corrélées"),
                  (instance2,"Corrélation sur les durées d'éxecution"),
                  (instance3, "Corrélation sur les machines")]
                  #,(instance4, "Exemple du sujet")]
