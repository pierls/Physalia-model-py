Sp = 0.2 #taux de survie polype par an
d = 0.1 # taux de division polype
b = 0.6 # taux de rencontre des polypes pour faire méduse
Q = 1 # quantité de prédateur
a = 0.1 # taux de rencontre méduse/prédateur
Sm = 1 # paramètre extérieur tiers pour l'instant nul
f = 0.9 #taux de fécondation méduse
PO = 5000 # Quantité de polype initial
years = 10 # Nombre d'année d'étude

"""This model is the compute part of the app: it contain the model , and a tiny wrapper that does all the computation around it.
"""

def model(PO, Sp, d, b, Q, a, Sm, f, α):
    """this model should only be used by the ``compute()`` function.

    Args:
        PO (int): Quantity of polyps at the year -1.
        Sp (double): Chance of survival for each polyp this year.
        d (double): Chance of a polyp to duplicate.
        b (double): Chance of two polyps mating and create a Cnidaria.
        Q (int): Number of predators.
        a (double): Chance of Cnidaria/predator encounter.
        Sm (double): Chance of survival for each Cnidaria this year.
        f (double): Chance of reproducting for each Cnidaria.

    Returns:
        int: the number of polyps for the given year.
    """
    P1 = (Sp + 2*d-α*PO)*PO -2*b*(PO**2)+ 2*b*(PO**2)*Sm*(1-a*Q)*f
    return (P1)

  
def compute(PO, Sp, d, b, Q, a, Sm, f, α, years):
    """This is a tiny wrapper around the model to give a simple way to do computations.

    Args:
        PO (int): Quantity of polyps at the year -1.
        Sp (int): Chance of survival for each polyp this year.
        d (int): Chance of a polyp to duplicate.
        b (int): Chance of two polyps mating and create a Cnidaria.
        Q (int): Number of predators.
        a (int): Chance of Cnidaria/predator encounter.
        Sm (int): Chance of survival for each Cnidaria this year.
        f (int): Chance of reproducting for each Cnidaria.
        years (int): number of year which the model runs.

    Returns:
        int[]: a year-lengh array that result of the computation of this model.
    """
    polype = [] 
    polype.append(PO)
    P1 = PO
    for annee in range(years): # boucle pour définir P2 en fonction de P1
        if(P1 >100000000): # Security if the function goes too high
            pass
        if(P1 <0):
            P1 = 0
            pass

        polype.append(model(P1, Sp, d, b, Q, a, Sm, f, α))
        P1 = model(P1, Sp, d, b, Q, a, Sm, f, α)
    return polype
  
