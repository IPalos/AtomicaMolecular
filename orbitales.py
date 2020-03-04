#!/usr/bin/env python

#=========================
#IMPORTS
#=========================
import numpy
import scipy.special
import scipy.misc
from mayavi import mlab
mlab.init_notebook()

#=========================
#COORDENADAS ESFERICAS
#=========================

r = lambda x,y,z: numpy.sqrt(x**2+y**2+z**2)
theta = lambda x,y,z: numpy.arccos(z/r(x,y,z))
phi = lambda x,y,z: numpy.arctan(y/x)

#R = lambda r,n,l: -sqrt((2/n*a)**3*(factorial(n-l-1)/(2*n*(factorial(n+l))**3)))*exp(-r/(n*a))*((2*r)/(n*a))**l*genlaguerre(n+l,2*l+1)(2*r/n)

a0 = 1. #RADIO DE BOHR

R = lambda r,n,l: (2*r/n/a0)**l * numpy.exp(-r/n/a0) * scipy.special.genlaguerre(n-l-1,2*l+1)(2*r/n/a0)/2 #FUNCION RADIAL
WF = lambda r,theta,phi,n,l,m: R(r,n,l) * scipy.special.sph_harm(m,l,phi,theta) #FUNCION DE ONDA
absWF = lambda r,theta,phi,n,l,m: abs(WF(r,theta,phi,n,l,m))**2 #MODULO AL CUADRADO

x,y,z = numpy.ogrid[-24:24:55j,-24:24:55j,-24:24:55j]

#=========================
#PARAMETROS DE CORTE
#=========================
a= numpy.pi/5
b=numpy.pi/3
c=[]
for i in range(0,50):
	c.append(i*0.0005)
print (c)


mlab.figure() 

mask = numpy.select([theta(x,y,z)>a],[numpy.select([abs(phi(x,y,z))<b],[numpy.nan],default=1)],default=1)
#mask =1

w = absWF(r(x,y,z),theta(x,y,z),phi(x,y,z),2,1,0)
mlab.contour3d(w*mask, contours=c, transparent=False)
#for n in range(1,5):
#	for l in range(1,n):
#		for m in range(-l,l+1,1):
#			w = absWF(r(x,y,z),theta(x,y,z),phi(x,y,z),n,l,m)
#			mlab.contour3d(w*mask,contours=c,transparent=True)

mlab.colorbar()
mlab.outline()
mlab.show()
