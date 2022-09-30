"""
Juan Esteban Barrientos Sierra (000428876) & Daniel Orlando Escorcia Dí­az (000427686)
"""

"""
Se requiere una función llamada alargamiento, que calcule el alargamiento unitario 
mediante la expresión: E=(Lf-lo)/Lo
"""

def alargamiento(x,L0):
    import numpy as np
    n=len(x)
    E=np.zeros(n)
    for i in range(0,n,1):
        E[i]=(x[i]-L0)/L0
    return E

"""
Una función llamada tensión, que calcule la tensión en [N/mm2]
utilizando la expresión: T=F/S
"""

def tension(s,vf):
    import numpy as np
    n=len(vf)
    t=np.zeros(n)
    for i in range(0,n,1):
        t[i]=vf[i]/s
        
    return t
    