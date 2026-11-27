# Modélisation des données de la compagnie aérienne

Entre le 1er et le 2 septembre 2025, les deux fichiers contiennent les mêmes 80 aéroports, avec des informations identiques. Pour les vols, 419 identifiants sont présents les deux jours avec les mêmes caractéristiques. Deux vols apparaissent dans le second fichier et un vol du premier en est absent. Je prévois de conserver ce vol dans l’entrepôt en le marquant inactif afin que les réservations passées puissent toujours être reliées à leur vol.

Les deux sources de passagers utilisent des noms de colonnes et des formats de date différents. Pour les réunir dans une même table, je vais harmoniser les noms des colonnes et convertir les dates de naissance dans un type commun.


