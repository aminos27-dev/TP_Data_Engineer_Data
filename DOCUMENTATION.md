# Modélisation des données de la compagnie aérienne

Entre le 1er et le 2 septembre 2025, les deux fichiers contiennent les mêmes 80 aéroports, avec des informations identiques. Pour les vols, 419 identifiants sont présents les deux jours avec les mêmes caractéristiques. Deux vols apparaissent dans le second fichier et un vol du premier en est absent. Je prévois de conserver ce vol dans l’entrepôt en le marquant inactif afin que les réservations passées puissent toujours être reliées à leur vol.

Les deux sources de passagers utilisent des noms de colonnes et des formats de date différents. Pour les réunir dans une même table, je vais harmoniser les noms des colonnes et convertir les dates de naissance dans un type commun.


## Exploration des passagers et des réservations

Dans les fichiers de passagers EN et FR comparés, aucun identifiant de passager n’est commun aux deux sources.

Le fichier de réservations du 1er septembre 2025 contient uniquement des réservations datées du 1er. Celui du 2 septembre contient uniquement des réservations datées du 2. Aucun `booking_id` n’apparaît dans les deux fichiers.
Sur ces deux jours, on observe donc un export quotidien. En Silver, nous cumulerons les réservations et utiliserons `booking_id` pour éviter les doublons si une même journée est chargée deux fois.

[Voir le code des vérifications](analyses/exploration_sources.py)

