# Simulating satellite orbiting a planet

import math
import matplotlib.pyplot as plt
import turtle

G = 6.673*(10**-11)
M = 5.972*(10**24)
m = 1000
iteration = 500

x = 0
y = 100000
r = math.sqrt((x**2) + (y**2))

v_x = math.sqrt((G*M)/r)
v_y = 0

dt = 0.1
t_elapsed = 0

li_r = []
li_x = [x]
li_y = [y]

li_time = []
li_energy = []

for i in range(iteration):
    r = math.sqrt((x**2) + (y**2))
    T_energy = m*(0.5*(v_x**2 + v_y**2) - (G*M/r))
    
    li_r.append(r)
    li_time.append(t_elapsed)
    li_energy.append(T_energy)
    
    acc = (G*M)/(r**2)
    acc_x = acc*(x/r)
    acc_y = acc*(y/r)
    v_x += -(acc_x*dt)
    v_y += -(acc_y*dt)
    x += v_x*dt
    y += v_y*dt
    
    li_x.append(x)
    li_y.append(y)
        
    t_elapsed += dt

plt.plot(li_time, li_r)

turtle.speed(0)
for j in range(iteration):
    turtle.penup()
    turtle.goto(li_x[j]/1000, li_y[j]/1000)
    turtle.dot()
    turtle.delay(dt*1000)