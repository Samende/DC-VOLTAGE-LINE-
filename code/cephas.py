






import numpy as np
import scipy
import matplotlib.pyplot as plt
import math
R1=0.2
R2=R1
Vm=0.9
X=0.001

#calculating V1
a=np.array([0.9]*9)
b=np.array([1]*9)
c=np.array([0.9]*9)
d=np.array([0.8]*9)
e=np.array([1]*9)

V1=np.concatenate((a,b,c,d,e))# Values of V1

V2=np.array([2*Vm - x for x in V1] ) #calculating V2

I=np.array([Vm-y for y in V2])/R2 #calculating current

P1=V1*I #power supplied

P2=V2*I #power received

P_loss = P1 - P2 #power lost

t=np.concatenate((np.arange(0,9,1),np.arange(8,17,1),np.arange(16,25,1),np.arange(24,33,1),np.arange(32,41,1)))


       
plt.plot(V2,V1)                     # plot of V1 vs V2
plt.xlabel('time (s)')
plt.ylabel('V1 (pu)')
plt.show()

plt.figure(1)
plt.subplot(211)
plt.plot(t,V1)                        # plot of V1 
plt.xlabel('time (s)')
plt.ylabel('V1 (pu)')

plt.subplot(212)
plt.plot(t,V2)                        # plot of  V2
plt.xlabel('time (s)')
plt.ylabel('V2 (pu)')
plt.show()

plt.figure(2)
plt.subplot(211)
plt.plot(t,V2)                        # plot of  V2
plt.xlabel('time (s)')
plt.ylabel('V2 (pu)')

plt.subplot(212)
plt.plot(t,I)                        # plot of I
plt.xlabel('time (s)')
plt.ylabel('I (pu)')
plt.show()


plt.figure(3)
plt.subplot(211)
plt.plot(t,P1)                       # plot of P1
plt.xlabel('time (s)')
plt.ylabel('P1 (pu)')

plt.subplot(212)
plt.plot(t,P2)                       # plot of P2
plt.xlabel('time (s)')
plt.ylabel('P2 (pu)')
plt.show()

plt.plot(t,P_loss)                       # plot of Power loss
plt.xlabel('time (s)')
plt.ylabel('P loss (pu)')
plt.show()


