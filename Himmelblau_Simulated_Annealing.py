import numpy as np
import matplotlib.pyplot as plt
import random
import math
# this function has four global minimum with the value of zero
# based on the initial point, a solution closer to that point will be achieved
x0=-2                                   # determining an initial value for variable X
y0=2                                    # determining an initial value for variable X
cp=0.9                                  # determining the cooling parameter
t0=1000                                 # determining the initial temperature
m=20                                    # determining the number of times the algorithm will try to move to another position
                                        # ... at a spesific temperature
T=350                                   # determining the number of times cooling process will be done
mt=t0                                   # maximum temperature   

def obj(x,y):
    z=((x**2)+y-11)**2+(x+(y**2)-7)**2   # Himmelblau Function
    return z

t=[]                                     # a list to store all the temperatures the system will experience
z=[]                                     # a list to store all the values obtained for variable z 

for i in range(T):
    t.append(t0)                      # Storing the records of temperature
    for j in range(m):

        randx=random.uniform(0,1)        # random number to choose a direction to move along the x-axis
        randy=random.uniform(0,1)        # random number to choose a direction to move along the y-axis
        
        if randx >= 0.5:
            delta_x= random.uniform(0,0.1)  # moving towards larger values along the x-axis (step size < 0.1)
        else:
            delta_x= -random.uniform(0,0.1) # moving towards smaller values along the x-axis (step size < 0.1)
            
        if randy >= 0.5:
            delta_y= random.uniform(0,0.1)  # moving towards larger values along the y-axis (step size < 0.1)
        else:
            delta_y= -random.uniform(0,0.1) # moving towards smaller values along the y-axis (step size < 0.1)
            
        x= x0 + delta_x                     # updated x
        y= y0 + delta_y                     # updated y
        
        objnew=obj(x,y)                     # Recalculating the new z value
        
        objold=obj(x0,y0)                   # calculating the old z value
       
        try:                                # the probability of choosing a position worse than before
            pr = math.exp((objold-objnew)/t0)
        except OverflowError:
            pr = float('inf')  
        
        if objnew <= objold or random.uniform(0,1)<=pr:   # updating the initial points for the following iteration over m
            x0=x
            y0=y
    
    z.append(objold)                        # storing the obtained objective values based on each move
    t0=cp*t0                                # Updating the temperature of the system
    
    
print( " X equals [ %.4f ]" % x0)
print( " Y equals [ %.4f ]" % y0)
print( " Final objective value equals %.4f " % objold)

# Plot the objectie values based on each temperature
plt.plot(t,z, 'green', linewidth=2)
plt.title(" Z(X,Y) for each temperature", fontweight='bold')
plt.xlabel("Temperature", fontweight='bold')
plt.ylabel("Z", fontweight='bold')
plt.xlim(mt,0)
plt.xticks(np.arange(min(t),max(t),100),fontweight='bold')
plt.yticks(fontweight='bold')

# CONTOUR PLOT
x = np.arange(-4.5, 4.5, 0.01)
y = np.arange(-4.5, 4.5, 0.01)
[X, Y] = np.meshgrid(x, y)

# Contour Lines  
fig, ax = plt.subplots(1, 1)
ax.contour(X, Y, obj(X,Y))
ax.set_title('Contour Lines')
ax.set_xlabel('X')
ax.set_ylabel('Y')

# Filled Contour Plot
fig, ax = plt.subplots(1, 1)
ax.contourf(X, Y, obj(X,Y))
ax.set_title('Filled Contour Plot')
ax.set_xlabel('X')
ax.set_ylabel('Y')
  
plt.show()