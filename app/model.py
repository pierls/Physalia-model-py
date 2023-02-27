Sp = 0.2 #taux de survie polype par an
d = 0.1 # taux de division polype
b = 0.6 # taux de rencontre des polypes pour faire méduse
Q = 1 # quantité de prédateur
a = 0.1 # taux de rencontre méduse/prédateur
Sm = 1 # paramètre extérieur tiers pour l'instant nul
f = 0.9 #taux de fécondation méduse
PO = 5000 # Quantité de polype initial

annee_iteree = 10 # Nombre d'année d'étude
def model(PO, Sp, d, b, Q, a, Sm, f, α):
    P1 = (Sp + 2*d-α*PO)*PO -2*b*(PO**2)+ 2*b*(PO**2)*Sm*(1-a*Q)*f
    return (P1)

  
def compute(PO, Sp, d, b, Q, a, Sm, f, α, years):
    polype = [] 
    polype.append(PO)
    P1 = PO
    for annee in range(years): # boucle pour définir P2 en fonction de P1
        if(P1 >100000000): # Security if the function goes too high
            pass
        polype.append(model(P1, Sp, d, b, Q, a, Sm, f, α))
        P1 = model(P1, Sp, d, b, Q, a, Sm, f, α)
    return polype
  
