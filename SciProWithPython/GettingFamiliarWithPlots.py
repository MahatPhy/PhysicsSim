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
xlabel('x'); ylabel('f(x)'); title('-\sin(x)*\cos(x^2)') #internal parser
grid(True)
subplot(2,1,2)
plot(x2,y2,'-',lw=2)
xlabel('x'); ylabel('f(x)'); title('exp(-x/4)*sin(x)')
figure(2)
subplot(2,1,1)
plot(x1,y1*y1,'r',lw=2)
xlabel('x'); ylabel('f(x)'); title('\sin^2(x)*\cos(x^2)')
subplot(2,1,2)
plot(x2,y2*y2,'-',lw=2)
xlabel('x'); ylabel('f(x)'); title('\exp(-x/2)*\sin^2(x)')
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
ax.set_xticklabels(['0','\pi','2\pi'])
ax.set_ylabel('f(x) = x\,\sin^2 x',fontsize=20)
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
ax.set_title('Answers')
plt.show()

