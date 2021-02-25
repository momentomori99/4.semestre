import numpy as np
import matplotlib.pyplot as plt
"""
# Signal parametere
f_sig = 1 #frek for signalet
omega_sig = 2*np.pi*f_sig #frekvenshastighet til signalet

#Samplings parametere
N_perioder = 2 #Antall perioder vi ønsker å studere
T = (2*np.pi/omega_sig) * N_perioder #tid det tar per 1 periode ganget med antall perioder
N = 16 #Antall punkter i samplingen
dt = T/N
f_samp = 1/dt
"""


#Signal parametere
f_sig = 100
A = 1

#Sampling parametere
T = 1 #sekund
f_samp = 1000 #Hz
N = T*f_samp #Antall samplings punkter i løpet av 1 sekund
dt = T/N

t = np.linspace(0, T, N)
x_n = A*np.sin(2*np.pi*f_sig*t)

X_k = np.fft.fft(x_n)
freq = np.fft.fftfreq(N,dt)

#plt.plot(freq, X_k)
plt.xlabel('Tid [t]')
plt.ylabel('g(t)')
plt.title('Samplede tidsserien')

plt.plot(freq, np.real(X_k))
plt.xlabel('frekvenser')
plt.ylabel('X_k')
plt.title('Fourier transformert')
plt.grid(True)
plt.show()
