# Exercice 1
Dans cet exercice, nous allons charger le dataset et l'enrichir. Nous finirons par mesurer sa qualité et l'explorer légèrement.

Vous devrez modifier chaque fonction présent dans le fichier exercice_1.py. Faites attention à ne pas renommer ces fonctions car nous ne serions pas en mesure de vous évaluer (vous pouvez bien entendu en créer d'autre au besoin).

## Charger les données
Chargez le fichier '2016_sampled.csv' et retournez un dataframe pandas.

Fonction: load_data

## Enrichir les données
Charger le fichier préparé en utilisant la librairie python pandas et calculer la colonne suivante :

*  Colonne capacity_bytes : cette colonne contient la taille en octet du disque dur. Pour faciliter le traitement ensuite, calculer cette taille en TB. Vous devrez arrondir à 0,1 TB.
*  fonction: add_capacity_tb

## Mesurer les valeurs manquantes

Vérifier, pour chaque colonmne, le nombre de valeurs manquantes. Pour cet exercice, il vous faudra nous retourner un dataframe pandas contenant le nom original de chaque colonne en ligne ainsi que deux colonnes:

* null_values: nombre de valeur nulles
* null_values_ratio: pourcentage de valeurs nulles
* fonction: missing_values

## Visualiser les données
Représenter les différentes colonnes sous forme d’histogrammes ou de distributions afin d’identifier les valeurs extrêmes et d’améliorer votre connaissance du dataset.

Pour cet exercice, impressionnez-nous avec vos visualisation. Votre code pourra être revu par la société générale, un code de qualité sera apprécié.

* Fonction: visualize
