#Q. Write a python for simulating angular momentum of earth.

#import necessary libraries
import math
import matplotlib.pyplot as plt

#define constants
G = 6.67408e-11 #gravitational constant
M_earth = 5.972e24 #mass of earth
R_earth = 6.371e6 #radius of earth

#calculate angular momentum
L_earth = math.sqrt(G*M_earth*R_earth)

#simulate angular momentum over time
time = [0, 1, 2, 3, 4, 5]
L_earth_sim = [L_earth, L_earth*1.1, L_earth*1.2, L_earth*1.3, L_earth*1.4, L_earth*1.5]

#plot the results
plt.plot(time, L_earth_sim)
plt.xlabel('Time (s)')
plt.ylabel('Angular Momentum (kg m^2/s)')
plt.title('Simulated Angular Momentum of Earth')
plt.show()
