from matplotlib import pyplot as plt
dt = 0.01
T = 0
T_max = 1000
x_M, y_M = 0, 0

def grav_force(M, m, x_M, y_M, x_m, y_m):
    force_xm = -M*m*(x_m-x_M)/((x_m-x_M)**2+(y_m-y_M)**2)**1.5
    force_ym = -M*m*(y_m-y_M)/((x_m-x_M)**2+(y_m-y_M)**2)**1.5
    
    return force_xm,force_ym

M = float(input("Enter mass of star"))
m1, m2 = map(float, input("Enter mass of planet 1 and planet 2 ").split())
x1, y1 = map(float, input("Enter x,y coordinates of planet 1 ").split())
x2, y2 = map(float, input("Enter x,y coordinates of planet 2").split())
u_x1, u_y1 = map(float, input("Enter initial x,y velocities of planet 1").split())
u_x2, u_y2 = map(float, input("Enter initial x,y velocities of planet2").split())

v_x1, v_y1 = u_x1, u_y1
v_x2, v_y2 = u_x2, u_y2


position_x1, position_y1 = [], []
position_x2, position_y2 = [], []
position_x1.append(x1)
position_y1.append(y1)
position_x2.append(x2)
position_y2.append(y2)


while T<=T_max:
   f1x_star, f1y_star = grav_force(M, m1, x_M ,y_M, x1, y1)
   f2x_star, f2y_star = grav_force(M, m2, x_M, y_M, x2, y2)
   f12x, f12y = grav_force(m2, m1, x2, y2, x1, y1)
   
   v_x1 = v_x1 + dt*((f1x_star+f12x)/m1)
   v_y1 = v_y1 + dt*((f1y_star+f12y)/m1)
   x1 = x1 + v_x1*dt
   y1 = y1 + v_y1*dt
   
   v_x2 = v_x2 + dt*((f2x_star-f12x)/m2)
   v_y2 = v_y2 + dt*((f2y_star-f12y)/m2)
   x2 = x2 + v_x2*dt
   y2 = y2 + v_y2*dt
   
   position_x1.append(x1)
   position_y1.append(y1)
   position_x2.append(x2)
   position_y2.append(y2)

   T += dt
  
    
plt.plot(position_x1,position_y1, label = "Planet 1")
plt.plot(position_x2,position_y2, label = "Planet 2")
plt.plot(0, 0, 'yo', markersize=10)
plt.title("Orbit")
plt.xlabel("Horizontal Displacement")
plt.ylabel("Vertical Displacement")
plt.legend()
plt.show()

