from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt
from math import * 
import numpy as np
from scipy import * 
from pylab import * 

g=9.81            
vinf=...     #Vitesse terminale du volant        
phi0=...     #Angle de direction
        

def impact(v0,theta0):    
    #la trajectoire du volant
    t=0
    vx=v0*cos(theta0)*cos(phi0)
    vy=v0*cos(theta0)*sin(phi0)
    vz=v0*sin(theta0)
    v=np.sqrt(vx**2+vy**2+vz**2)
    h=4.0/100
    temps=[0]
    Vitessex=[v0*cos(theta0)*cos(phi0)]
    Vitessey=[v0*cos(theta0)*sin(phi0)]
    Vitessez=[v0*sin(theta0)]
    Vitesse=[np.sqrt(vx**2+vy**2+vz**2)]
    for i in range(100):
        vx,vy,vz,v=vx+h*(-g*v*vx*(vinf)**(-2)), vy+h*(-g*v*vy*(vinf)**(-2)), vz+h*(-g-g*v*vz*(vinf)**(-2)), np.sqrt((vx+h*(-g*v*vx*(vinf)**(-2)))**2+(vy+h*(-g*v*vy*(vinf)**(-2)))**2+
(vz+h*(-g-g*v*vz*(vinf)**(-2)))**2)
        t=t+h
        temps.append(t)
        Vitessex.append(vx)
        Vitessey.append(vy)
        Vitessez.append(vz)
        Vitesse.append(v)
    x=3.05
    y=4.6
    z=1
    Positionx=[3.05]
    Positiony=[4.6]
    Positionz=[1]
    for j in range(100):
        if Positionz[j]<0:
            yimpact=Positiony[j-1]
            break
        else:
            x,y,z=x+h*Vitessex[j],y+h*Vitessey[j],z+h*Vitessez[j]
            Positionx.append(x)
            Positiony.append(y)
            Positionz.append(z)
    return yimpact
      
def vitesseoptimale():
    v0=0
    theta0=0.02
    Vitesse=[]
    Angle=[]
    while theta0<pi/2.0:
        Angle.append(180*theta0/pi)
        v0=0
        while (impact(v0,theta0)<8.8):
            v0=v0+0.01
        Vitesse.append(v0)
        theta0=theta0+0.01
    plt.plot(Angle,Vitesse)
    plt.xlabel("Angle de projection")
    plt.ylabel("Vitesse de frappe optimale")
    plt.grid(True)
    xlim(0,60)
    ylim(0,100)
    plt.show()
         


   








      
