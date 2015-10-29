# -*- coding: utf-8 -*-
import numpy as np
import random
import copy

inf = float('Inf')
A, B, C = range(0,3)

def Johnson(d):
    n = np.size(d, 0)
    m = np.size(d, 1)
    A, B, C = range(0,m)
    X = list(range(0,n))
    G = list()
    D = list()
    while X:
        pos = np.argmin([[d[i,j] if i in X else +inf for j in [A,B]] for i in range(n)])
        i, j = pos//(m-1), pos%(n-1)
        G.append(i) if j == A else D.insert(0, i)
        X.remove(i)
    return G + D

def evaluation(d, pi, pip):
    def alpha(d, k, pi):
        if not pi: return 0
        if k == 0: return d[pi[0],A]
        return alpha(d, k-1, pi) + d[pi[k], A]
    def beta(d, k, pi):
        if not pi: return 0
        if k == 0: return sum(d[pi[0],(A,B)])
        return max(alpha(d, k, pi), beta(d, k-1, pi)) + d[pi[k], B]
    def gamma(d, k, pi):
        if not pi: return 0
        if k == 0: return sum(d[pi[0],(A,B,C)])
        return max(beta(d, k, pi), gamma(d, k-1, pi)) + d[pi[k], C]
    dk = sum(d[pi[-1],:])
    bA = alpha(d, len(pi)-1, pi) + dk + sum(min(d[i,A], d[i,C]) for i in pip)
    bB = beta(d, len(pi)-1, pi) + dk + sum(min(d[i,A], d[i,B]) for i in pip)
    bC = gamma(d, len(pi)-1, pi) + dk + sum(d[pip,C])
    return max(bA, bB, bC) # Borne inférieure

def Arbo(d, pi, pip, depth, sol=-1):
    #print(pi, pip, sol, evaluation(d, sol, []) if sol else None)
    if depth == d[:,0].size:
        return pi+list(pip), evaluation(d, pi+list(pip), [])
    binf = +inf
    for k in pip:
        if sol != 1 or evaluation(d, pi+[k], pip[pip != k]) < evaluation(d, sol, []):
            rsol, rbinf = Arbo(d, pi+[k], pip[pip != k], depth+1, sol)
            if rbinf < binf:
                binf = rbinf
                sol = rsol
    return sol, binf

S = []
for T in range(50):
    # Données type
    n, m = 7, 3 # nb taches, nb machines
    d = np.array([[2, 3, 4],[2, 3, 5], [9, 4, 1]]) # durées taches/machines

    # Données non-corrélées
    a, b = np.ones((n,m)), 100*np.ones((n,m))

    # Corrélation sur les durées d'éxecution
    r = np.array([random.sample({0,1,2,3,4}, 1) for k in range(n)])
    a, b = 20*r*np.ones((n,m)), 20*r*np.ones((n,m)) + 20

    # Corrélation sur les machines
    #a, b = (np.hstack([1*np.ones((n,1)), 2*np.ones((n,1)), 3*np.ones((n,1))]),)*2
    #a, b = 15*(a-1)+1, 15*(b-1)+100

    # Constrution des durées
    d = np.int32(np.random.uniform(a, b))
    #d = np.array([[2, 3, 4],[2, 3, 5], [9, 4, 1]]) # durées taches/machines
    #d = np.array([[1, 8, 4],[2, 4, 5], [6, 2, 8], [3, 9, 2]]) # durées taches/machines
    #d = np.array([[22, 39, 45], [75, 35, 66], [ 7, 53, 31]])

    print("Data: \n{}\n".format(d))

    # Algorithme approché avec garantie de performance (notre solution est 3-approché)
    solution1 = Johnson(d)
    print("Johnson: {}\n".format((solution1, evaluation(d, solution1, []))))

    # Méthode exacte
    ## Initialisation
    d, pi, pi_prime, profondeur = d, [], np.array(range(np.size(d, 0))), 0
    ## Algorithme arborescent
    solution2 = Arbo(d, pi, pi_prime, profondeur)
    print("Méthode exacte: {}\n".format(solution2))
    S.append(int(solution1[1] <= solution2[1]))
    print("Résultat cohérent ? {}\n".format(bool(S[-1])))
print(100*sum(S)/len(S),'%')
