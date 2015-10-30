from evaluation import *

inf = float('Inf')

def arbre(d, pi, pip, depth, sol=[]):
    if depth == d[:,0].size:
        return pi+list(pip), evaluation(d, pi+list(pip), [])
    binf = +inf
    for k in pip:
        print(pi+[k], pip[pip != k], evaluation(d, pi+[k], pip[pip != k]), sol, evaluation(d, sol, []) if sol else None)
        #if not sol or evaluation(d, pi+[k], pip[pip != k]) < evaluation(d, sol, []):
        rsol, rbinf = Arbo(d, pi+[k], pip[pip != k], depth+1, sol)
        if rbinf < binf:
            binf = rbinf
            sol = rsol
    return sol, binf
