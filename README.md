# Projet appliqué à la modélisation : l’évolution démographique inquiétante de Physalia physalis


## Contexte 
<p align="justify"> Dans le cadre de la matière "Evaluation et sélection de modèles" dirigée par le Pr. Sébastiens Gourbiere, nous avons été invités à réaliser une étude de modèle biologique sur le sujet de notre choix par petits groupes d'étudiants (4-5). Le sujet qui à été choisi par mon groupe (E.Christine, M.Berges, A.Reina, I.Salmi et moi même Guillaume Petit) reposait sur l'évolution démographique d'un cnidaire (Physalia physalis) originaire des eaux tropicales. Cet organisme produit des toxines dangereuses pour l'Homme, et on le retrouve de plus en plus échoué sur les plages Est-Atlantique. Pouvant donc représenter un danger pour les écosystèmes marins déjà établis ainsi que pour le tourisme, il est donc important d'anticiper les comportements que pourrait avoir cet organisme. L'intérêt scientifique n'étant que très récent sur cette population, la difficulté majeure de ce projet résidait dans l'absence d'information sur le cycle de vie de cette organisme ainsi que sur le manque de chiffres. Pour remédier à cela notre étude est restée purement mathématique avec comme objectif de cibler les paramètres biologiques les plus impactants de cette population. Par des développements mathématiques élémentaires, nous avons réussi à définir les différentes évolutions possibles de notre population. Cependant, la visualisation du modèle est vite devenue un impératif pour pouvoir vérifier nos conjectures. C'est pourquoi j'ai (Guillaume Petit) décidé de développer une ébauche d'application avec une interface utilisateur dynamique, afin de pouvoir observer le comportement de notre modèle. </p> 

## Introduction

<p align="justify"> L’équilibre fragile des écosystèmes marins se voit bouleversé par la politique de pêche intensive et non sélective de ces dernières années, ceci ayant pour conséquence la disparition de certaines espèces. De manière générale, l’évolution des écosystèmes tend à avoir plusieurs organismes ayant une même fonction, c’est le principe de redondance fonctionnelle. Grâce à ce principe la disparition d’une espèce n'impactent pas ou très peu l’écosystème, puisque d’autres organismes aux fonctions similaires compenseront cette perte. Cependant la redondance fonctionnelle n’est pas bien établie dans tous les écosystèmes. Physalia physalis est un parfait exemple de ce phénomène, ce cnidaire vivant habituellement dans les eaux tropicales, se retrouvent aujourd’hui à s’échouer sur les côtes Est-Atlantique. Physalia physalis, ou encore appelé la galère portugaise est un supra-organisme produisant des toxines dangereuses pour l’Homme, de ce fait sa présence sur les côtes européennes est un danger pour l’équilibre des écosystèmes déjà présent ainsi que pour le tourisme. Il est de plus en plus fréquent d’en trouver échoué sur les plages françaises dû à l'accentuation de certains courants (notamment le golf stream) provoqué par le dérèglement climatique mais aussi à cause de la surpopulation de cet organisme dans les eaux tropicales. Cette surpopulation est due à la disparition progressive de son unique prédateur : la tortue Caretta caretta, classée comme espèce vulnérable selon le statut de conservation UICN. En effet depuis des années cette tortue est une victime collatérale de la pêche au filet qui s’intensifie dans les régions tropicales et subtropicales. La suppression progressive d’un prédateur permet logiquement une croissance dans la population de sa proie, c’est le cas pour la population de Physalia physalis. Ce document traitera de la problématique suivante : Comment évolue la population de Physalia physalis et qu’elle sera l’impact de la perte progressive de son unique prédateur. </p> 

### Liens vers la production initiale réalisé sous la direction du Pr. Sébastiens Gourbiere :
https://github.com/pierls/Physalia-model-py/blob/main/Projet%20appliqué%20à%20la%20modélisation%20_%20l’évolution%20démographique%20inquiétante%20de%20Physalia%20physalis%20G.Petit%2C%20I.Salmi%2C%20E.%20Christine%2C%20M.Berges%2C%20A.Reina.pdf

<p align="justify"> Cette partie n'a pas été modifiée depuis son rendu pour évaluation le 17/12/2022. </p>



## Partie biologique (réalisé dans le cadre de la matière "Evaluation et sélection de modèle" dispensé au S5)
<p align="justify"> Cette partie s'articule autour d'une représentation du cycle de vie de Physalia physalis à l'échelle local par une équation différentiel non-linéaire. Son étude à permis de mettre en évidence la forte capacité de conquête de Physalia physalis. Nous avons conclus que plus la pêche serait forte dans les région tropicals plus notre organisme aura tendance à conquérir d'autre territoire. En d'autre terme, si il y a une explosion démographique, elle ne sera pas ressentis à l'échelle local, mais à l'échelle globale.

Les contributeurs de cette partie son (Reina Amandine, Berges Marie, Christine Emma, Salmi Illian, Petit Guillaume). </p> 

## Partie informatique
<p align="justify"> Cette partie à pour but d'aider à visualiser l'impact potentiel de chaques paramètres biologiques sur l'évolution de la population de Physalia Physalis à l'échelle local. Elle à était réalisé en python dans le cadre de ma candidature au Master bio-informatique de l'UCBL. </p> 

### prérequis 
Python 3.10 ou supérieur 
Librairies DearPyGui & Numpy

### quick start 
<p align="justify"> l'application est déjà hautement pré-configurée, il suffit simplement d'executer le fichier app.py ce trouvant dans le dossier app, avec la commande "python ./app.py" </p> 

### Fonctionnement de l'application 
Architecture verticale à 3 composantes : 

 modèle : modélisation du cycle de vie de Physalia Physalis 

 front : interface utilisateur 

 app : affichage dynamique des résultats donnés par le modèle 


### Pour aller plus loin
La composante "model" a initialement était réalisé en R, elle est toujours disponible sur le git. La documentation technique est elle aussi disponible sur le git.

### Réalisation 
Guillaume Petit, aka @logyrave

### Reviewer et pair-programmeur
@pierls
