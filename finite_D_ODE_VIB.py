import numpy as np
from finite_D_ODE_VIB_visual import visualize
"""
Solve u + w**2*u = 0 for t in (0,T], u(0)=I and u(0)=0,
by a central finite difference method with time step dt.
"""

def solver():

	T = float(input("Enter Period:"))
	dt = float(input("Input dt:"))
	I = float(input("Input the Amplitude:"))
	w = (2*(np.pi))/T
	Nt = int(round(T/dt))
	t = np.linspace(0, Nt*dt, Nt+1) # mesh points in time
	#dt = t[1] - t[0] # constant time step
	u = np.zeros(Nt+1) # solution
	u[0] = I
	u[1] = u[0] - 0.5*dt**2*w**2*u[0]

	
	for n in range(1, Nt):
		u[n+1] = 2*u[n] - u[n-1] - dt**2*w**2*u[n]
	return visualize(u,t,I,w,dt)
 