# COMPLEX-Project-1
## Partie Théorique : Questions 4 à 6

pi = début de la permutation des tâches
t_A^pi = durée pour traiter pi tâches sur M_A
t_B^pi = durée pour traiter pi tâches sur M_A et M_B
t_C^pi = durée pour traiter pi tâches sur M_A et M_B et M_C

b_A^pi = t_A^pi + sum(i in pi prime).d_A^i + min{d_B^i + d_C^i}
=> On choisit une tache i in pi prime tq  d_B^i + d_C^i soit min pour " finir rapidement à la fin"
de même

b_B^pi = t_B^pi + sum(i in pi prime).d_B^i + min{d_C^i}
b_A^pi = t_C^pi + sum(i in pi prime).d_C^i 

Question 4

soit delta = t_A^pi + sum(i in pi prime).d_A^i - t_B^pi

La tache i ne peut pas commencer dans la machine B avant sa fin dans la machine A
donc 

b_B^pi = t_B^pi + sum(i in pi prime excluding min(i)).d_B^i + d_B^min(i) + delta + min{d_C^i}
