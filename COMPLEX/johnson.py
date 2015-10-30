import numpy as np
import evaluation

def johnson(d, debug=False):
    assert np.size(d, 1) > 1, "2 machines au moins"
    if debug and np.size(d, 1) != 2: print("Attention: Seul les deux premières machines sont pris en compte.")
    n, m = np.size(d, 0), 3
    A, B, C = range(0,m)
    X = list(range(0,n))
    G = list()
    D = list()
    while X:
        pos = np.nanargmin([[d[i,j] if i in X else np.nan for j in [A,B]] for i in range(n)])
        i, j = pos//(m-1), pos%(n-1)
        G.append(i) if j == A else D.insert(0, i)
        X.remove(i)
    return G + D, evaluation.evaluation(d, G+D, [])

if __name__ == "__main__":
    from instances import *
    d = instance2(50,3)
    sol, time = johnson(d, True)
    print(sol, time)
