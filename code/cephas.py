#==============================================================================#
import math
import matplotlib.pyplot as plt
import numpy as np
#.........Defining some parameters...........................
Vm=0.9
Imax=1.000
Isc=(10/100*Imax)+Imax          #short circuit current
Vmax=1.0                        #maximum converter output voltage deviation
Vmin=0.8                        #minimum converter output voltage deviation
Vn=1.0                          #nominal converter input voltage 
Vgmin=0.947                     #minimum converter input voltage deviation

#................Line parameters..................................
R=0.2

#...............Main control strategy.............................

#========================================================================================

#                          CONTROL OF Vref OF CONVERTER 1 FOR VARYING V2

#========================================================================================
g=lambda V2:(2*(Vm-V2)/R)       #calculating load current from the values of V2

h=lambda I:Vm+I*R/2             #calculating V1 reference from values of current
    

#..............Variables.........................................

tf=40                           #end of simulation time
dt=1                            #change in time
t0=0                            #start of simulation time
t=[]                            #to hold values of simulation time
V2=[]                           #to hold values of load voltage,V2
Vref=[]                         #to hold values of reference voltage at V1
current=[]                      #to hold values of load current
Vgrid=[]                        #to hold values of instatenous input grid voltage

#......................Control Strategy Algorithm....................
i=0
while t0<=tf:                   #creating load and grid input voltage profile 
    if 0<=t0<=5:
        V2.append(Vm)
        Vgrid.append(1.3)
    elif 5<=t0<=10:
        V2.append(0.88)
        Vgrid.append(1.4)
    elif 10<=t0<=15:
        V2.append(0.84)
        Vgrid.append(1.06)
    elif 15<=t0<=20:
        V2.append(0.97)           
        Vgrid.append(0.98)
    elif 20<=t0<=25:
        V2.append(0.95)
        Vgrid.append(0)
    elif 25<=t0<=30:
        V2.append(0.8)
        Vgrid.append(1.9)
    elif 30<=t0<=35:
        V2.append(0.89)
        Vgrid.append(1.1)
    else:
        V2.append(0.9)
        Vgrid.append(1.05)
    i+=1
    t.append(t0)
    t0+=dt

time=t  

#======================================================================

# =========EXPLANATION OF THE PROGRAM BELOW OF A GRID SUPPLYING AN INDEPENDENT VOLTAGE SOURCE=======================

"""Let Vref be the reference voltage of the output of the converter connected to grid and V2 be the the voltage of the 
independent source. Vmax and Vmin are the voltage deviation limits at the output of the converter. Vgrid is the instantenous 
voltage of the grid, Vn is the grid nominal voltage,Vgmin is the minimum grid volatge deviation.

Now, if Vgrid = Vn, this implies that the grid is self-sufficient(cannot not generate more and does not need any power) reseting
Vref to Vm (the middle voltage of the line). If Vgrid > Vn, the grid has a surplus and willing to supply the surplus hence
increasing Vref to (Vm + I*R1) and power is exported. When Vgmin<=Vgrid<Vn, the grid has a shortage and Vref =Vm-I*R1. Power 
is received from the external grid. However, if none of the conditions above holds, Vref = Vm and this happens when there is a short
circuit.

The assumption is that the grids are self managed such that if Vgrid = Vgmin, dumping of loads should happen by either through load shedding

"""

n=0
while n<=40:                                   #continuosly sense current for 40 seconds

    V=V2[n]                               
    current.append(g(V))                       #created load profile    
    I=current[n]                               #sensed current
    
    if I>=0:                                   #Boost mode
    
        if Vgrid[n]>Vn and I<=Imax:            #check if the grid has surplus generation and current is within acceptable range
           Vref.append(h(I))                   #increase output reference voltage according to the current requested
           if Vref[n]>=Vmax:                   #check if the reference voltage is more than max. voltage and reset to Vmax
              Vref[n]=Vmax                          
           
        elif Vgrid[n]>Vn and Imax<I<Isc:        #check if the current is not as a result of a short circuit 
             Vref.append(Vmax)                  #Limit voltage output for any load greater than Imax but less than Isc
        else:
            Vref.append(Vm)                     #reset Vref to Vm if Vgrid =Vn (autonomuos mode) or Vgrid <=Vgmin (faulty grid/insuffiecient generation)
            
    elif I<0:                                   #buck converter mode
    
        if Vgmin<=Vgrid[n]<Vn  and abs(I)<=Imax: #check the voltage on the bus and restore if less than the minimum voltage
           Vref.append(h(I))
           if Vref[n]<=Vmin:                    #check if the reference voltage is less than min. voltage and reset to Vmin
               Vref[n]=Vmin
           
        elif Vgmin<=Vgrid[n]<Vn and Imax<abs(I)<Isc: #check if its not a short circuit
             Vref.append(Vmin)                      #Limit voltage output for any load greater than Imax but less than the Isc
        else:
            Vref.append(Vm)                         #reset Vref to Vm if Vgrid =Vn (restored mode) or Vgrid <Vgmin (faulty grid/insuffiecient generation from external)
            
    else:
        Vref.append(Vm)                         # Fault condition, converter shut down
        
       
    n+=1
    
    
plt.subplot(211)
plt.step(time,Vgrid)
plt.xlabel('time(s)')
plt.ylabel('Vgrid (pu)')

plt.subplot(212)
plt.step(time,current)
plt.xlabel('time(s)')
plt.ylabel('Current (pu)')
plt.show()

      
plt.subplot(211)
plt.step(time,Vref)
plt.xlabel('time(s)')
plt.ylabel('Vref (pu)')

plt.subplot(212)
plt.step(time,V2)
plt.xlabel('time(s)')
plt.ylabel('V2 (pu)')
plt.show()

plt.step(time,Vref)
plt.xlabel('time(s)')
plt.ylabel('Vref (pu)')
plt.ylim(0.7,1.0)

plt.step(V2,Vref)
plt.xlabel('V2(s)')
plt.ylabel('Vref (pu)')



