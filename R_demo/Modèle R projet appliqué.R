Sp = 0.2 #taux de survie polype par an
d = 0.1 # taux de division polype
b = 0.6 # taux de rencontre des polypes pour faire méduse
Q = 1 # quantité de prédateur
a = 0.1 # taux de rencontre méduse/prédateur
Sm = 1 # paramètre extérieur tiers pour l'instant nul
f = 0.9 #taux de fécondation méduse
PO = 5000 # Quantité de polype initial

annee_iteree = 10 # Nombre d'année d'étude

modele = function(PO){
    P1 <- (Sp + 2*d)*PO + 2*b*Sm*(1-a*Q)*f*PO^2
    return (P1)
}

polype = NULL # Ecrasement du tableau polype pour relancer le programme avec annee différente
polype[1] = PO 
for(annee in 1:annee_iteree){ # boucle pour définir P2 en fonction de P1
  polype[annee+1] = modele(polype[annee])
}

plot(c(0:annee_iteree), 
     polype,main = "population",
     xlab = "Année",
     ylab = "Quantité de polype",
      type = "b",)

polype[9] # Qtt de polype a T8 

