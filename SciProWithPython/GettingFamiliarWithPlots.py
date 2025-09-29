#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 28 14:20:21 2025

@author: Dr_Bright
"""

#%%

#2 plots in Vpython

from vpython import *

graph1 = graph(align='left',width=400,height=400,background=color.white,foreground=color.black)
Plot1 = gcurve(color=color.red)
for x in arange(0,8.1,0.1):
        Plot1.plot(pos=(x,5*cos(2*x)*exp(-0.4*x)))
graph2 = graph(align='right',width=400,height=400,background=color.white,foreground=color.black,
               title='2-D plot',xtitle='x',ytitle='f(x)')
Plot2 = gdots(color=color.black)
for x in arange(-5,5,0.1):
    Plot2.plot(pos=(x,cos(x)))
    
#%%

#plotting 2-D x-y plots

from vpython import *

string = "blue: sin^2(x), black = cos^2(x), cyan: sin(x)cos(x)"
graph1 = graph(title=string,xtitle='x',ytitle='y',background=color.white,foreground=color.black)
y1=gcurve(color=color.blue) #curve
y2=gvbars(color=color.black) #vertical bars
y3=gdots(color=color.cyan) #dots
for x in arange(-5,5,0.1):
    y1.plot(pos=(x,sin(x)**2))
    y2.plot(pos=(x,cos(x)**2))
    y3.plot(pos=(x,sin(x)*cos(x)))

#%%

from pylab import *

Xmin = -5. ; Xmax = 5. ; Npoints = 500
DelX = (Xmax-Xmin)/Npoints
x = arange(Xmin,Xmax,DelX)
y = sin(x)*sin(x*x)
print('arange => x[0],x[1],x[499] = %8.2f %8.2f %8.2f'%(x[0],x[1],x[499]))
print('arange => y[0],y[1],y[499] = %8.2f %8.2f %8.2f'%(y[0],y[1],y[499]))
print("\n doing plotting for figure 1")
xlabel('x'); ylabel('y'); title('y vs x'); text(-1.75,0.75,'MatplotLib \n Example') #text on plot
plot(x,y,'-',lw=2)
grid(True)
show()

#%%

#grade inflation vs years in college plot


import pylab as p
from numpy import *

p.title("Grade inflation")
p.xlabel("Years in college")
p.ylabel("GPA")
xa = array([-1,5])
ya = array([0,0])
p.plot(xa,ya)
x0 = array([0,1,2,3,4])
y0 = array([-1.4,1.1,2.2,3.3,4.0])
p.plot(x0,y0,'bo')
p.plot(x0,y0,'g')
x1 = arange(0,5,1)
y2 = array([4.0,2.7,-1.8,-0.9,2.6])
p.plot(x1,y1,'r')
errTop = array([1.0,0.3,1.2,0.4,0.1])
errBot = array([2.0,0.6,2.3,1.8,0.4])
p.errorbar(x1, y1, [errBot,errTop],fmt='o')
p.grid(True)
p.show()

#%%

#array operations and their applications to matplotlib

from pylab import *

Xmin = -5; Xmax = 5; Npoints = 500
DelX = (Xmax-Xmin)/Npoints
x1 = arange(Xmin,Xmax,DelX)
x2 = arange(Xmin,Xmax,DelX/20) #different x2 range
y1 = -sin(x1)*cos(x1*x1) #look an array can have hadamard operations performed on it
y2 = exp(-x2/4.)*sin(x2)
figure(1)
subplot(2,1,1)
plot(x1,y1,'r',lw=2)
xlabel('x'); ylabel('f(x)'); title('$-\sin(x)*\cos(x^2)$') #internal parser
grid(True)
subplot(2,1,2)
plot(x2,y2,'-',lw=2)
xlabel('x'); ylabel('f(x)'); title('exp(-x/4)*sin(x)')
figure(2)
subplot(2,1,1)
plot(x1,y1*y1,'r',lw=2)
xlabel('x'); ylabel('f(x)'); title('$\sin^2(x)*\cos(x^2)$')
subplot(2,1,2)
plot(x2,y2*y2,'-',lw=2)
xlabel('x'); ylabel('f(x)'); title('$\exp(-x/2)*\sin^2(x)$')
grid(True)
show()

#%%

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # still needed to register 3D projection

delta = 0.1
x = np.arange(-3., 3., delta)
y = np.arange(-3., 3., delta)
X, Y = np.meshgrid(x, y)
Z = np.sin(X) * np.cos(Y)  # Surface Height

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d') 
'''Axes3d has been replaced with this'''

# Plot surface and wireframe
ax.plot_surface(X, Y, Z)
ax.plot_wireframe(X, Y, Z, color='r')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()

#%%

'''Monte Carlo integration via Von Neumann rejection'''

""" Monte Carlo with Von Neumann rejection
 is just throwing random darts at a box and counting 
 how many land under the curve to guess the area.
 """

import numpy as np, matplotlib.pyplot as plt

N,Npts = 5,5000;
analyt=np.pi**2
x1 = np.arange(0, 2*np.pi+2*np.pi/N, 2*np.pi/N)
xi = [];
yi = [];
xo = [];
yo = []

fig,ax = plt.subplots()

y1 = x1*np.sin(x1)**2 #integrand

ax.plot(x1,y1,'c',linewidth=4)
ax.set_xlim((0,2*np.pi))
ax.set_ylim((0,5))
ax.set_xticks([0,np.pi,2*np.pi])
ax.set_xticklabels(['0','$\pi$','2$\pi$'])
ax.set_ylabel('$f(x) = x\,\sin^2 x$',fontsize=20)
ax.set_xlabel('x',fontsize=20)
fig.patch.set_visible(False)

def f(x):
    return x*np.sin(x)**2  #integrand

j = 0 #inside curve counter
xx = 2 * np.pi * np.random.rand(Npts) #x is between 0 and 2pi
yy = 5 * np.random.rand(Npts) #y is between 0 and 5

boxarea = 2 * np.pi * 5 #box area

for i in range(1,Npts):
    #plt.pause(0.0001)
    if(yy[i] <= f(xx[i])):
        xi.append(xx[i])
        yi.append(yy[i])
        j+=1
    else:
        yo.append(yy[i])
        xo.append(xx[i])
    area = boxarea * j / (Npts-1) #area under the curve

ax.plot(xo,yo,'bo',markersize=1) 
ax.plot(xi,yi,'ro',markersize=1)
ax.set_title('Answers: Analytic = %5.3f, MC = %5.3f'%(analyt,area))
plt.show()

#%%
from vpython import *
from numpy import arange
from math import sin, cos, asin, pi

#Forces on two moving strings

posy = 100; Lcord = 250;
Hweight = 50; W = 10 #cylinder height, cylinder weight

#scene = display(height = 600,width=600,range=380)
scene = canvas(width=600, height=600, range=380)

alt = curve(pos=[vector(-300,posy,0), vector(300,posy,0)])
divi = curve(pos=[vector(0,-150,0), vector(0,posy,0)])



#kilogr = cylinder(pos=(0,posy-Lcord,0),radius=20,axis=(0,-Hweight,0),color=color.red) #kg as a cylinder

kilogr = cylinder(
    pos=vector(0, posy-Lcord, 0),
    radius=20,
    axis=vector(0, -Hweight, 0),
    color=color.red
)


cord1 = cylinder(pos=vector(0,posy,0), axis=vector(0,-Lcord,0), color=color.yellow, radius=2)
cord2 = cylinder(pos=vector(0,posy,0), axis=vector(0,-Lcord,0), color=color.yellow, radius=2)

arrow1 = arrow(pos=vector(0, posy, 0), color=color.orange)
arrow2 = arrow(pos=vector(0, posy, 0), color=color.orange)

magF=W/2.0 #initial force of each student
v = 2.0 #m/s velocity 
x1 = 0.0

anglabel = label(pos=vector(0,240,0), text='angle(deg)', box=0)
angultext = label(pos=vector(20,210,0), box=0)

Flabel1 = label(pos=vector(200,240,0), text='Force', box=0)
Ftext1  = label(pos=vector(200,210,0), box=0)
Flabel2 = label(pos=vector(-200,240,0), text='Force', box=0)
Ftext2  = label(pos=vector(-200,210,0), box=0)


local_light(pos=vector(-10,0,20),color=color.yellow)

for t in arange(0.,100.0,0.2):
    rate(50) #slowmotion
    x1=v*t
    theta=asin(x1/Lcord)
    poscil=posy-Lcord*cos(theta)
    #kilogr.pos(0,poscil,0)
    kilogr.pos = vector(0, poscil, 0)

    magF=W/(2.*cos(theta))
    angle = 180.*theta/pi
    
    cord1.pos = vector(x1, posy, 0)
    cord1.axis = vector(-Lcord*sin(theta), -Lcord*cos(theta), 0)
    
    cord2.pos = vector(-x1, posy, 0)
    cord2.axis = vector(Lcord*sin(theta), -Lcord*cos(theta), 0)
    
    arrow1.pos = cord1.pos
    arrow1.axis = vector(8*magF*sin(theta), 8*magF*cos(theta), 0)
    arrow2.pos = cord2.pos
    arrow2.axis = vector(-8*magF*sin(theta), 8*magF*cos(theta), 0)
    
    angultext.text = '%4.2f'%angle
    force = magF
    
    Ftext1.text = '%8.2f'%force
    Ftext2.text= '%8.2f'%force
    
#%%

#central value theorem


import random, matplotlib.mlab as mlab
import numpy as np, matplotlib.pyplot as plt

N = 1000; NR = 10000; #sum N variables, distribution of sums
SumList = []

def SumRandoms(): #sum N random numbers in 0,1
    summation = 0.0
    for i in range(0,N):
        summation+=random.random()
    return summation

def normal_dist_param(): #average distribution
    add = sum2 = 0
    for i in range(0,NR):
        add+=SumList[i]
    mu=add/NR
    for i in range(0,NR):
        sum2+=(SumList[i]-mu)**2
    sigma=np.sqrt(sum2/NR)
    return mu,sigma

for i in range(0,NR):
    dist=SumRandoms()
    SumList.append(dist)
plt.hist(SumList,bins=50,color="white",density=True)
mu,sigma = normal_dist_param()
x=np.arange(450,550)

rho = np.exp(-(x-mu)**2/(2*sigma**2))/np.sqrt(2*np.pi*sigma**2)

plt.plot(x,rho,'g-',linewidth=3.0)
plt.xlabel('Random number x 1000')
plt.ylabel('Average of random numbers')
plt.title('Generated vs analytic normal distribution')
plt.show()