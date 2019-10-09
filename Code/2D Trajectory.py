#from math import *
import numpy as np
import matplotlib.pyplot as plt

g=9.81            
vinf=6.42          
theta0=(46*np.pi)/180 
v0=16   

def tracetrajectoire():            
    t=0
    vx=v0*np.cos(theta0)
    vy=v0*np.sin(theta0)  
    v=np.sqrt(vx**2+vy**2)    
    h=4.0/100000
    temps=[0]
    Vitessex=[v0*np.cos(theta0)]
    Vitessey=[v0*np.sin(theta0)]
    Vitesse=[np.sqrt(vx**2+vy**2)]
    for i in range(100000):
        vx,vy,v=vx+h*(-g*v*vx*(vinf)**(-2)),vy+h*(-g-g*v*vy*(vinf)**(-2)), np.sqrt((vx+h*(-g*v*vx*(vinf)**(-2)))**2+(vy+h*(-g-g*v*vy*(vinf)**(-2)))**2)
        t=t+h
        temps.append(t)
        Vitessex.append(vx)
        Vitessey.append(vy)
        Vitesse.append(v)
    plt.figure(1)
    plt.subplot(121)
    plt.plot(temps,Vitesse,color='red')
    plt.plot([0, 4], [vinf,vinf], color='green')  
    plt.title('Evolution de la vitesse du volant en fonction du temps')
    plt.xlabel("temps (s)")
    plt.ylabel("vitesse (m/s)")   
    x=2
    y=1
    Positionx=[2]
    Positiony=[1]
    for j in range(100000):
        if Positiony[j]<0:
            ximpact=Positionx[j-1]
            vimpact=np.sqrt(Vitessex[j-1]**2.0+Vitessey[j-1]**2.0)
            tempsvol=(j-1)*(4.0/100000)
            break
        else:
            x,y=x+h*Vitessex[j],y+h*Vitessey[j]
            Positionx.append(x)
            Positiony.append(y)
    plt.plot([tempsvol,],[vimpact,],'ro')
    plt.show()
    print ("la portee du volant est de", ximpact-Positionx[0], "m")
    print ("la vitesse d'impact au sol est de", vimpact, "m/s")
    print ("le temps de vol est de", tempsvol, "s")
    plt.subplot(122)
    plt.plot(Positionx,Positiony,color='orange')
    plt.plot([0,13.4],[0,0],color='blue')      #terrain de badminton
    plt.plot([6.7,6.7],[0,1.55],color='grey')  #filet
    plt.title('Trajectoire du volant de badminton')
    plt.xlabel("x (m)")
    plt.ylabel("y (m)")
    plt.show()
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    