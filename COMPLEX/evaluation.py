import numpy as np

def evaluation(d, pi, pip):
    m = np.size(d, 1)
    A, B, C = range(0,m)
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
    if len(pip) == 0: # feuille de l'arbre
        return gamma(d, len(pi)-1, pi)
    dk = sum(d[pi[-1],:])
    bA = alpha(d, len(pi)-1, pi) + dk + sum(min(d[i,A], d[i,C]) for i in pip)
    #bB = beta(d, len(pi)-1, pi) + dk + sum(min(d[i,B], d[i,C]) for i in pip)
    #bC = gamma(d, len(pi)-1, pi) + dk + sum(d[pip,C])
    return bA # Borne inférieure
