import numpy as np
import matplotlib.pyplot as plt

def u_exact(t, I, w):
	return I*np.cos(w*t)
def visualize(u, t, I, w,dt):
	
	plt.plot(t, u, 'r-o')
	t_fine = np.linspace(0, t[-1], 1001) # very fine mesh for u_e
	u_e = u_exact(t_fine, I, w)
	# plt.hold('on')
	plt.plot(t_fine, u_e, 'b-')
	plt.legend(['numerical', 'exact'], loc='upper left')
	plt.xlabel('t')
	plt.ylabel('u')
	#dt = t[1] - t[0]
	plt.title('dt=%g' % dt)
	umin = 1.2*u.min(); umax = -umin
	plt.axis([t[0], t[-1], umin, umax])
	#plt.savefig('tmp1.png'); plt.savefig('tmp1.pdf')
	plt.show()
