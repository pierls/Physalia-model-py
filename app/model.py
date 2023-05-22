

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
        if(P1 <0):
            P1 = 0
            pass

        polype.append(model(P1, Sp, d, b, Q, a, Sm, f, α))
        P1 = model(P1, Sp, d, b, Q, a, Sm, f, α)
    return polype
  
