import numpy as np

A, B, C = range(0,3)

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

def evaluation(d, pi, pip):
    m = np.size(d, 1)
    if len(pip) == 0: # feuille de l'arbre
        return gamma(d, len(pi)-1, pi) # zbest = date de fin de l'ordonnancement
    tA, tB, tC = alpha(d, len(pi)-1, pi), beta(d, len(pi)-1, pi), gamma(d, len(pi)-1, pi)
    bA = tA + sum(d[pip,A]) + min(d[pip,B] + d[pip,C])
    bB = max(tB, tA + min(d[pip,A])) + sum(d[pip,B]) + min(d[pip,C])
    bC = max(tC, tB + min(d[pip,B]), tA + min(d[pip,A] + d[pip,B])) + sum(d[pip,C])
    return max(bA, bB, bC) # zlb = Borne inférieure

if __name__ == "__main__":
    # TEST DE L'EVALUATION (INDEPENDANT)#
    assert evaluation(np.array([[2, 3, 4],[2, 3, 5], [9, 4, 1]]), [0,1,2], []) == 18
