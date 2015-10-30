from evaluation import *

inf = float('Inf')

def arbre(d, pi, pip, depth, sol=[], debug=False, alpha=0, elagage=True):
    """ Méthode arborescente utilisant une fonction évaluation basé sur la borne
    inférieure """
    if depth == d[:,0].size:
        return pi+list(pip), evaluation(d, pi+list(pip), [])
    eval_sol = +inf
    for k in pip:
        #if debug and sol: print(pi+[k], pip[pip != k], evaluation(d, pi+[k], pip[pip != k]), sol, evaluation(d, sol, []) if sol else None, evaluation(d, pi+[k], pip[pip != k]) > evaluation(d, sol, []) and evaluation(d, pi+[k], pip[pip != k]) < (1+alpha)*evaluation(d, sol, []))
        if not elagage or evaluation(d, pi+[k], pip[pip != k]) < (1-alpha)*eval_sol:
            rsol, reval_sol = arbre(d, pi+[k], pip[pip != k], depth+1, sol, debug, alpha)
            if reval_sol < eval_sol:
                eval_sol = reval_sol
                sol = rsol
    return sol, eval_sol



if __name__ == "__main__":
    # TEST DE LA METHODE ARBORESCENTE (INDEPENDANT)#
    from instances import *
    import time
    import johnson

    # Verification sur un jeu de donnée connu
    depth, sol = 0, None
    d = instance4()
    pi, piprime = [], np.array(range(np.size(d, 0)))
    sol, duration = arbre(d, pi, piprime, depth, sol, True, 0)
    assert duration == 18

    # Test de la durée d'exection avec et sans élagage
    earned = []
    for k in range(100):
        d = instance3(8,3)
        sol1, time1 = johnson.johnson(d)
        #print(sol1,time1, "Johnson")
        pi, piprime = [], np.array(range(np.size(d, 0)))
        s = time.clock()
        sol, duration = arbre(d, pi, piprime, depth, sol, True, 0, True)
        #print(sol, duration)
        final1 = time.clock() - s
        #print(final1, "Aucun Elagage")
        pi, piprime = [], np.array(range(np.size(d, 0)))
        s = time.clock()
        sol, duration = arbre(d, pi, piprime, depth, sol, True, 0.3, True)
        #print(sol, duration)
        final2 = time.clock() - s
        #print(final2, "Elagage")
        earned.append(final1-final2)
    print(sum(earned)/len(earned)*100,'%')
