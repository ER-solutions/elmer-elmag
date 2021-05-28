import math

x1 = 0.1
x2 = 0.18
z1 = -0.04
z2 = 0.04

N = 8153
conductivity = 1e10

A_tot = (x2-x1)*(z2-z1)
A = A_tot/N
l = 2*math.pi*(x2+x1)/2

V_tot = A_tot*l

l_tot = N * l

Resistance = 1./conductivity * l_tot/A

print ("Wire length = ", l_tot)
print ("Area = ", A_tot)
print ("Volume = ", V_tot)
print ("Resistance = ", Resistance)
