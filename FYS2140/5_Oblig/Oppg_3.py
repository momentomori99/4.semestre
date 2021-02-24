import numpy as np
import matplotlib.pyplot as plt


a = 1 #nm
m = 0.511 #MeV/c^2
t = 10 * 10**(-15) #s
h_bar = 6.582119569*(10**(-16)) #eV*s
n = 3


q = (n**2*np.pi**2*h_bar)/(2*m*a**2)

x = np.linspace(0,a)

def prob(x):
    return (1/a)*np.sin((np.pi*n*x)/a)**2
plt.subplot(221)
plt.plot(x, prob(x))
plt.xlabel('x/a [nm]')
plt.ylabel('Probability, |psi|^2')
plt.grid(True)


def real(x):
    return np.sqrt(2/a)*np.sin((n*np.pi/a)*x)*np.cos(q*t)

plt.subplot(222)
plt.plot(x,real(x),'r')
plt.xlabel('x/a [nm]')
plt.ylabel('real(Psi)')

plt.grid(True)

def im(x):
    return -np.sqrt(2/a)*np.sin((n*np.pi*x/a))*np.sin(q*t)
plt.subplot(223)
plt.plot(x,im(x),'g')
plt.xlabel('x/a [nm]')
plt.ylabel('Imaginary(Psi)')
plt.grid(True)

plt.show()
