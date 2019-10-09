from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt
#from math import *
import numpy as np

g=9.81            
vinf=6.42          
theta0=(27.3*np.pi)/180    
phi0=(90*np.pi)/180      
v0=27

def tracetrajectoire3d():
    fig = plt.figure()
    ax = Axes3D(fig)
    
    x = [0,0,6.1,6.1]
    y = [0,13.4,13.4,0]
    z = [0,0,0,0]
    verts = [zip(x,y,z)]
    ax.add_collection3d(Poly3DCollection(verts,color='limegreen'))
    
    x1=[-1,-1,0,0]
    y1=[-2,15.5,15.5,-2]
    z1=[0,0,0,0]
    verts1 = [zip(x1,y1,z1)]
    x2=[0,7,7,0]
    y2=[-2,-2,-0.2,-0.2]
    z2=[0,0,0,0]
    verts2=[zip(x2,y2,z2)]
    x3=[6.2,6.2,7,7]
    y3=[-0.2,15.5,15.5,-0.2]
    z3=[0,0,0,0]
    verts3=[zip(x3,y3,z3)]
    x4=[0,6.2,6.2,0]
    y4=[13.4,13.4,15.5,15.5]
    z4=[0,0,0,0]
    verts4=[zip(x4,y4,z4)]
    ax.add_collection3d(Poly3DCollection(verts1,color='cornflowerblue'))
    ax.add_collection3d(Poly3DCollection(verts2,color='cornflowerblue'))
    ax.add_collection3d(Poly3DCollection(verts3,color='cornflowerblue'))
    ax.add_collection3d(Poly3DCollection(verts4,color='cornflowerblue'))
    
    plt.plot([0,0,6.1,6.1,0], [0,13.4,13.4,0,0],[0,0,0,0,0], 
             color='w',linewidth=2)
    plt.plot([0.46,0.46], [0,13.4],[0,0], color='w',linewidth=2)
    plt.plot([6.1-0.46,6.1-0.46], [0,13.4],[0,0], color='w',linewidth=2)
    plt.plot([0,6.1], [6.7-1.98,6.7-1.98],[0,0], color='w',linewidth=2)
    plt.plot([0,6.1], [6.7+1.98,6.7+1.98],[0,0], color='w',linewidth=2)
    plt.plot([0,6.1], [6.7,6.7],[0,0], color='w',linewidth=2)
    plt.plot([0,6.1], [0.76,0.76],[0,0], color='w',linewidth=2)
    plt.plot([0,6.1], [13.4-0.76,13.4-0.76],[0,0], color='w',linewidth=2)
    plt.plot([3.05,3.05], [0,6.7-1.98],[0,0], color='w',linewidth=2)
    plt.plot([3.05,3.05], [6.7+1.98,13.4],[0,0], color='w',linewidth=2)
    plt.plot([0,0], [6.7,6.7],[0,1.55], color='grey',linewidth=2)
    plt.plot([6.1,6.1], [6.7,6.7],[0,1.55], color='grey',linewidth=2)
    
    xfilet = [0,3.05,6.1,6.1,0]
    yfilet = [6.7,6.7,6.7,6.7,6.7]
    zfilet = [1.55,1.524,1.55,0.95,0.95]
    vertsfilet = [zip(xfilet,yfilet,zfilet)]
    ax.add_collection3d(Poly3DCollection(vertsfilet,color='darkgrey'))
    
    t=0
    vx=v0*np.cos(theta0)*np.cos(phi0)
    vy=v0*np.cos(theta0)*np.sin(phi0)
    vz=v0*np.sin(theta0)
    v=np.sqrt(vx**2+vy**2+vz**2)
    h=4.0/100000
    temps=[0]
    Vitessex=[v0*np.cos(theta0)*np.cos(phi0)]
    Vitessey=[v0*np.cos(theta0)*np.sin(phi0)]
    Vitessez=[v0*np.sin(theta0)]
    Vitesse=[np.sqrt(vx**2+vy**2+vz**2)]
    for i in range(100000):
        vx,vy,vz,v=vx+h*(-g*v*vx*(vinf)**(-2)), vy+h*(-g*v*vy*(vinf)**(-2)), vz+h*(-g-g*v*vz*(vinf)**(-2)), np.sqrt((vx+h*(-g*v*vx*(vinf)**(-2)))**2+(vy+h*(-g*v*vy*(vinf)**(-2)))**2+(vz+h*(-g-g*v*vz*(vinf)**(-2)))**2)
        t=t+h
        temps.append(t)
        Vitessex.append(vx)
        Vitessey.append(vy)
        Vitessez.append(vz)
        Vitesse.append(v)
    x=4
    y=1
    z=1
    Positionx=[4]
    Positiony=[1]
    Positionz=[1]
    for j in range(100000):
        if Positionz[j]<0:
            yimpact=Positiony[j-1]
            vimpact=np.sqrt(Vitessex[j-1]**2.0+Vitessey[j-1]**2.0+
            Vitessez[j-1]**2.0)
            tempsvol=(j-1)*(4.0/100000)
            break
        else:
            x,y,z=x+h*Vitessex[j],y+h*Vitessey[j],z+h*Vitessez[j]
            Positionx.append(x)
            Positiony.append(y)
            Positionz.append(z)
    print ("la portee du volant est de", yimpact-Positiony[0], "m")
    print ("la vitesse d'impact au sol est de", vimpact, "m/s")
    print ("le temps de vol est de", tempsvol, "s")
    ax.plot(Positionx,Positiony,Positionz,color='orange',linewidth=5)
    ax.set_zlim(0,6)
    ax.set_xlim(-1,7)
    ax.set_ylim(-2,15.5)
    plt.show()
    
   




































