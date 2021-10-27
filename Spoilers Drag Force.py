import numpy as np
import math
import plotly.graph_objects as go

V =np.arange(1,15,1)    # freestream velocity (m/s)
y = float(input('Overall Spoiler Height:')) #m
x= float(input('Overall Spoiler Length:'))  #m
L = float(input('Distance from leading edge to spoiler hinge:'))   #m
Cd = float(input('Spoiler Drag Coeficient:'))    
theta =  float(input('Deplyment Angle:'))  #Deployment Angle
n = 6      # Based on flat plate approximation

VBl = np.sqrt((n/(n+2))*(V**2))   # Velocity in Boundary Layer (m/s)
rho =  1.225    #Density ((kg/m3)
mu = 1.81e-5    # Dynamic Viscosity (kg/ms)
Re = ((rho*V*L)/mu)  # Reynolds Number
delta = (5*(L/Re))   # BL height (Delta 0.99)
Heff = y - delta     # Effective spoiler height outside BL
FT= (0.5 * Cd * rho * (V**2) * (Heff*x)) + ((delta*x) *(n/(n+2)) *0.5 *(V**2)*rho)   # N  Force on spoiler when perpendicular to surface
alpha = 90 -theta   #Effective angle

thetaI= math.radians(alpha)   #Degrees to radians conversion
U= math.cos(thetaI)  # Value of cos(θI)
F = FT*U     # Actual Force on plate
print ('Spoiler Drag:', F , 'N') 

fig =go.Figure(data=go.Scatter(x=V, y= F))
fig.update_layout(title='Force Against Velocity', xaxis_title='elocity m/s', yaxis_title='Force N')
fig.show()
