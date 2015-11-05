from evaluation import *

inf = float('Inf')

def arbre(d, pi, pip, depth, sol=[], debug=False, alpha=0, elagage=True):
    """
    Méthode arborescente utilisant une fonction évaluation
    basée sur la borne inférieure de chaque noeud.
    Chaque noeud représentant une permutation de taches et les tâches restantes.
    Retourne une permutation et sa durée.
    -------------
    d = jeu de donnée
    pi = permutation effectuée
    pip = tâches restantes à ordonner
    depth = profondeur dans l'arbre
    sol = solution courante
    alpha = critère d'élagation
    elagage = booléen (oui = élagage, non = aucun élagage)
    """

    # Si feuille de l'arbre, je retourne la permutation
    # et la durée de la permutation.
    if depth == d[:,0].size:
        return pi+list(pip), evaluation(d, pi+list(pip), [])

    eval_sol = +inf
    for k in pip:
        if debug: print(pi+[k], pip[pip != k], evaluation(d, pi+[k], pip[pip != k]) < (1-alpha)*eval_sol, sol, eval_sol)
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

    DEBUG = False

    # Verification sur un jeu de donnée connu
    depth, sol = 0, None
    d = instance4()
    pi, piprime = [], np.array(range(np.size(d, 0)))
    sol, duration = arbre(d, pi, piprime, depth, sol, DEBUG, 0)
    assert duration == 18

    # Test de la durée d'exection avec et sans élagage
    earned = []
    durations = []
    n_iteration = 100
    alpha = 0.1
    n, m = 5, 3
    for k in range(n_iteration):
        k = np.random.randint(len(instances_dict))
        d = instances_dict[k][0](n, m)
        sol1, time1 = johnson.johnson(d)
        #print(sol1,time1, "Johnson")
        pi, piprime = [], np.array(range(np.size(d, 0)))
        s = time.clock()
        sol, duration_exact = arbre(d, pi, piprime, depth, sol, DEBUG, 0, True)
        #print(sol, duration)
        final1 = time.clock() - s
        #print(final1, "Aucun Elagage")
        pi, piprime = [], np.array(range(np.size(d, 0)))
        s = time.clock()
        sol, duration_approchee = arbre(d, pi, piprime, depth, sol, DEBUG, alpha, True)
        #print(sol, duration)
        final2 = time.clock() - s
        #print(final2, "Elagage")
        earned.append(100*(final1-final2)/final1)
        durations.append((abs(duration_exact-duration_approchee)/duration_exact)*100)
    print(sum(earned)/len(earned),'% de temps gagné avec élagation à alpha={}'.format(alpha))
    print(sum(durations)/len(durations),'% écart à la solution en moyenne sur {} itérations'.format(n_iteration))
