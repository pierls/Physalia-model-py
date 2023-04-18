# Projet appliqué à la modélisation : l’évolution démographique inquiétante de Physalia physalis


## Contexte 
Dans le cadre de la matière "Evaluation et sélection de modèle" dirigé par le Pr. Sébastiens Gourbiere, nous avons été invité à réaliser une étude de modèle biologique sur le sujet de nôtre choix par petit groupe d'étudiant (4-5). Le sujet qui à été choisi par le groupe (E.Christine, M.Berges, A.Reina, I.Salmi et moi même Guillaume Petit) reposait sur l'évolution démographique d'un cnidaire (Physalia Physalis) originaire des eaux tropicales. La dificulté majeure étant l'absence quasiment total d'information sur cette organisme. En effet l'interêt scientifique portant sur Physalia Physalis n'est que très récent, aucun dénombrement ainsi qu'aucune information particulière sur son cycle de vie nous à été rapporté. Pour remedier à celà notre étude est resté purement théorique avec comme objectif de cibler les paramètres de vie les plus impactant de cette population. Par des développements mathématiques élémentaires, nous avons réussi à donner un cadre de développement. Cependant, la visualisation du modèle est vite devenue un impératif pour pouvoir vérifier nos conjectures. C'est pourquoi j'ai (Guillaume Petit) décidé de développer une ébauche d'application avec une interface utilisateur dynamique, afin de pouvoir observer le comportement de notre modèle. 

## Abstract

L’équilibre fragile des écosystèmes marins se voit bouleversé par la politique de pêche intensive et non sélective de ces dernières années, ceci ayant pour conséquence la disparition de certaines espèces. De manière générale, l’évolution des écosystèmes tant à avoir plusieurs organismes ayant une même fonction, c’est le principe de redondance fonctionnelle. Grâce à ce principe la disparition d’une espèce n'impactent pas ou très peu l’écosystème, puisque d’autres organismes aux fonctions similaires compenseront cette perte. Cependant la redondance fonctionnelle n’est pas bien établie dans tous les écosystèmes. Physalia physalis est un parfait exemple de ce phénomène, ce cnidaire vivant habituellement dans les eaux tropicales, se retrouvent aujourd’hui à s’échouer sur les côtes Est-Atlantique. Physalia physalis, ou encore appelé la galère portugaise est un supra-organisme produisant des toxines dangereuses pour l’Homme, de ce fait sa présence sur les côtes européennes est un danger pour l’équilibre des écosystèmes déjà présent ainsi que pour le tourisme. Il est de plus en plus fréquent d’en trouver échoué sur les plages françaises dû à l'accentuation de certains courants (notamment le golf stream) provoqué par le dérèglement climatique mais aussi à cause de la surpopulation de cet organisme dans les eaux tropicales. Cette surpopulation est due à la disparition progressive de son unique prédateur : la tortue Caretta caretta, classée comme espèce vulnérable selon le statut de conservation UICN. En effet depuis des années cette tortue est une victime collatérale de la pêche au filet qui s’intensifie dans les régions tropicales et subtropicales. La suppression progressive d’un prédateur permet logiquement une croissance dans la population de sa proie, c’est le cas pour la population de Physalia physalis. Ce document traitera de la problématique suivante : Comment évolue la population de Physalia physalis et qu’elle sera l’impact de la perte progressive de son unique prédateur.

### Liens vers la production initiale réalisé sous la direction du Pr. Sébastiens Gourbiere
[https://github.com/pierls/Physalia-model-py/blob/main/Projet%20appliqué%20à%20la%20modélisation%20_%20l’évolution%20démographique%20inquiétante%20de%20Physalia%20physalis%20G.Petit%2C%20I.Salmi%2C%20E.%20Christine%2C%20M.Berges%2C%20A.Reina.pdf](https://github.com/pierls/Physalia-model-py/blob/main/Projet%20appliqu%C3%A9%20%C3%A0%20la%20mod%C3%A9lisation%20_%20l%E2%80%99%C3%A9volution%20d%C3%A9mographique%20inqui%C3%A9tante%20de%20Physalia%20physalis%20G.Petit%2C%20I.Salmi%2C%20E.%20Christine%2C%20M.Berges%2C%20A.Reina.pdf)



## Partie biologique (réalisé dans le cadre de la matière "Evaluation et sélection de modèle" dispensé au S5)
La partie biologique disponible sur le git n'a pas était modifié depuis son rendu (même si le développement de mon application a permis de mettre en lumière des erreurs).
Les contributeur de cette partie son (Reina Amandine, Berges Marie, Christine Emma, Salmi Illian, Petit Guillaume).

## Partie informatique
Cette partie à pour but d'aider à visualiser l'impact potentiel de chaques paramètres biologiques sur l'évolution de la population de Physalia Physalis. Elle à était réalisé en python dans le cadre de ma candidature au Master bio-informatique de l'UCBL.

### prérequis 
Python 3.10 ou supérieur 
Librairies DearPyGui & Numpy
### quick start 
l'application est déjà hautement pré-configurée, il suffit simplement d'executer le fichier app.py ce trouvant dans le dossier app, avec la commande "python ./app.py"
### Fonctionnement de l'application 
Architecture verticale à 3 composantes : 
#### modèle : modélisation du cycle de vie de Physalia Physalis 
#### front : interface utilisateur 
#### app : affichage dynamique des résultats donnés par le modèle 
### Pour aller plus loin
La composante "model" a initialement était réalisé en R, elle est toujours disponible sur le git. 
### Réalisation 
Guillaume Petit, aka @logyrave
### Reviewer et pair-programmeur
@pierls
