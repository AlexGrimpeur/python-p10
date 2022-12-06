# exo 3.3
# Suite de l'exercice précédent.
# Calculez combien de bonbons Bob va distribuer par personne et stockez le résultat dans la variable `candies_per_person`.
# Calculez combien de chocolats Bob va distribuer par personne et stockez les résultats dans la variable `chocolates_per_person`.
# Affichez ces résultats.
#
# Indice : si vous séchez, reprenez le temps d'examiner la liste des opérateurs arithémtiques.
# Il y en a un qui va tout de suite vous donner la réponse.

candies = 15
chocolates = 17
friends = 3

candies_per_person = candies/friends
print(candies_per_person)

chocolates_rest = chocolates%friends
chocolates_per_personne = (chocolates - chocolates_rest)/friends
print(chocolates_per_personne)
print("Et il reste " + str(chocolates_rest)+ " chocolats")
# réponse 3.3

