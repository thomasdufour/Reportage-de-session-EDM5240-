# Reportage-de-session-EDM5240-
Voici les codes utilisés au cours de ce projet


# 1 - Utilisation de l'api de la BAnQ pour obtenir les pays cités par le Devoir
Le code dont le nom est traitementDevoir1910-2011.py sert à aller chercher toutes les éditions du Devoir depuis 1910. Les url des différentes éditions sont dans devoir-api.csv et ont été obtenus grace à un autre dossier Github dont le lien est ici --> https://github.com/jhroy/CdJ_LeDevoir.

Le csv compilationFinale.csv regroupe tous les pays cités pour chaque édition.

# 2 - Combiner les documents.
Nous avons fait roulé le code sur différents serveurs, nous devions donc fusionner les documents csv par la suite. C'est ce que fait le code intitulé combinerDocuments.py.

# 3 - Modification pour Poly.
modificationPourPoly.py est utilisé pour changer le format des données pour les intégrer dans un article web.

# 4 - moissonDevoir2011-2019.py
Ce code permet d'aller chercher le reste des éditions du Devoir que ne sont pas disponible pas le biais de l'API de la BAnQ. 
