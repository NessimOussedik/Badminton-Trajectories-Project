import numpy as np
import matplotlib.pyplot as plt

#T=(V0/Vinf)^2
def g(x,T):
    return 4*(T**2)*np.sin(x)
    
# Expression de la dérivée
def f(x,T):
    return np.arctan(np.sqrt((g(x,T))/((1+g(x,T))*np.log(1+g(x,T)))))-x
 
#Annulation de la dérivée pour un T donné
def zero(T,precision):
    a=0.02                          
    b=np.pi/2.0
    while b-a>2.0*precision:
        milieu=(a+b)/2.0
        if f(a,T)*f(milieu,T)<0.0:
            b=milieu
        else:
            a=milieu
    return milieu
    
#Balayage des annulations des dérivées  
def traceoptimal():
    origine=0.01
    abs=[0.01]
    ord=[180*zero(0.01,0.00000001)/np.pi]
    h=0.0014999                            #pas pour balayer juqu'à T=150
    for i in range(100000):
        origine=origine+h
        abs.append(origine)
        ord.append(180*zero(origine,0.00000001)/np.pi)
    plt.plot(abs,ord,'r')
    plt.grid(True)
    plt.xscale('log')       
    plt.show() 
        
  
    