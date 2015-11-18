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
        if debug: print("{}{}, {}, {}, {}, {}, {}".format(pi+[k], pip[pip != k], evaluation(d, pi+[k], pip[pip != k]) < (1-alpha)*eval_sol, sol, eval_sol, evaluation(d, pi+[k], pip[pip != k]), (1-alpha)*eval_sol))
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

    DEBUG = True

    # Verification sur un jeu de donnée connu
    depth, sol = 0, None
    d = instance5()
    d = d.T
    if DEBUG: print(d)
    pi, piprime = [], np.array(range(np.size(d, 0)))
    sol, duration = arbre(d, pi, piprime, depth, sol, True, 0)
    print("Arbre - Solution: ", sol, "Durée:", duration)
    sol1, time1 = johnson.johnson(d)
    print("Johnson - Solution: ", sol1, "Durée:", time1)

    # # Test de la durée d'exection avec et sans élagage
    # earned = []
    # durations = []
    # n_iteration = 1
    # alpha = 0.1
    # n, m = 3, 3
    # for k in range(n_iteration):
    #     sol, pi, piprime = None, [], np.array(range(np.size(d, 0)))
    #     k = np.random.randint(len(instances_dict))
    #     d = instances_dict[k][0](n, m)
    #     if DEBUG: print(d)
    #     sol1, time1 = johnson.johnson(d)
    #     #print(sol1,time1, "Johnson")
    #     pi, piprime = [], np.array(range(np.size(d, 0)))
    #     s = time.clock()
    #     sol, duration_exact = arbre(d, pi, piprime, depth, sol, DEBUG, 0, True)
    #     #print(sol, duration)
    #     final1 = time.clock() - s
    #     print(final1, "alpha=", 0)
    #     pi, piprime = [], np.array(range(np.size(d, 0)))
    #     s = time.clock()
    #     sol = None
    #     sol, duration_approchee = arbre(d, pi, piprime, depth, sol, DEBUG, alpha, True)
    #     #print(sol, duration)
    #     final2 = time.clock() - s
    #     print(final2, "alpha=", alpha)
    #     earned.append(100*(final1-final2)/final1)
    #     durations.append((abs(duration_exact-duration_approchee)/duration_exact)*100)
    # print(sum(earned)/len(earned),'% de temps gagné avec élagation à alpha={}'.format(alpha))
    # print(sum(durations)/len(durations),'% écart à la solution en moyenne sur {} itérations'.format(n_iteration))
