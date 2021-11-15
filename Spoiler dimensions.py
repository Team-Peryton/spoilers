import numpy as np
import math as m
F = float(input('Required Drag Force:')) #N
Cd = 1.28 #laminar flat plate Cd
x= 0.10# distance from leading edge to spoiler hinge
V = 14  #Velocity m/s
rho =  1.225    #Density ((kg/m3)
mu = 1.81e-5    # Dynamic Viscosity (kg/ms)
Re = ((rho*V*x)/mu)  # Reynolds Number
n = 6   # Based on flat plate approximation
VBl = np.sqrt((n/(n+2))*(V**2))   # Velocity in Boundary Layer (m/s)
delta = (5*(x/(m.sqrt(Re))))   # BL height (Delta 0.99)
w = 0.12 # spoiler width m
heff = w-delta # spoiler width outside the boundary layer max width
theta= 30*(m.pi/180)    #assuming max deployment angle of 60 degrees (yt video setup) Agle is measured from vertical axis
FT = F * (m.sin(theta))
L = FT/((0.5*rho*Cd)*((heff*V**2)+(delta*VBl**2)))
print('Overall Spoiler Length', L, 'm')
