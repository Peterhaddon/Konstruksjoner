
def fim_fordeltlast():

    q1 = q2 = l = 1

    # deler opp lasten i to trekantlaster
    fim_ende1 = (-1/20) * (q1*l**2) + ( 1/30) * (q2*l**2)
    fim_ende2 = ( 1/20) * (q1*l**2) + (-1/30) * (q2*l**2)
    
    return(fim_ende1, fim_ende2)

def lastvektor():

    return()