#==========================VOLTAGE CONTROL=========================================

#==========================SAMENDE  CEPHAS==========================================

import numpy as np
import scipy
import matplotlib.pyplot as plt
import math
R1=0.2                                       # Resistance of half of the line
R2=R1
Vm=0.9
X1=X2=0.1                                   #Reactance of half of the line

# forming slices of V1

a=np.array([0.9]*9)
b=np.array([1]*9)
c=np.array([0.9]*9)
d=np.array([0.8]*9)
e=np.array([1]*9)

V1=np.concatenate((a,b,c,d,e))                #forming an array, V1 from the slices
V2=np.array([2*Vm - x for x in V1] )          #Calculating V2
I=np.array([Vm-y for y in V2])/complex(R2,X2) #Calculating current
P1=V1*I                                       #Power supplied
P2=V2*I                                       #Power received
P_loss = P1 - P2                              #Power lost

t=np.concatenate((np.arange(0,9,1),np.arange(8,17,1),np.arange(16,25,1),np.arange(24,33,1),np.arange(32,41,1)))

plt.plot(V2,V1)                                # Plot of V1 vs V2
plt.xlabel('time (s)')
plt.ylabel('V1 (pu)')
plt.show()

plt.figure(1)
plt.subplot(211)
plt.plot(t,V1)                                 # Plot of V1 
plt.xlabel('time (s)')
plt.ylabel('V1 (pu)')

plt.subplot(212)
plt.plot(t,V2)                                 # Plot of  V2
plt.xlabel('time (s)')
plt.ylabel('V2 (pu)')
plt.show()

plt.figure(2)
plt.subplot(211)
plt.plot(t,V2)                                 # Plot of  V2
plt.xlabel('time (s)')
plt.ylabel('V2 (pu)')

plt.subplot(212)
plt.plot(t,I)                                  # Plot of I
plt.xlabel('time (s)')
plt.ylabel('I (pu)')
plt.show()


plt.figure(3)
plt.subplot(211)
plt.plot(t,P1)                                 # Plot of P1
plt.xlabel('time (s)')
plt.ylabel('P1 (pu)')

plt.subplot(212)
plt.plot(t,P2)                                 # Plot of P2
plt.xlabel('time (s)')
plt.ylabel('P2 (pu)')
plt.show()

plt.plot(t,P_loss)                             # Plot of Power loss
plt.xlabel('time (s)')
plt.ylabel('P loss (pu)')
plt.show()


