from matplotlib import pyplot as plt

class Body:
    def __init__(self, mass, x, y, vx, vy):
        self.mass = mass
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
    
    def grav_force(self, other):
         epsilon = 0.1
         forcex = (-self.mass*other.mass*(self.x-other.x))/((self.x-other.x)**2+(self.y-other.y)**2+epsilon**2)**1.5
         forcey = (-self.mass*other.mass*(self.y-other.y))/((self.x-other.x)**2+(self.y-other.y)**2+epsilon**2)**1.5
        
         return forcex, forcey
     
     
    def update(self, fx, fy, dt):
        self.vx = self.vx + dt*((fx/self.mass))
        self.vy = self.vy + dt*((fy/self.mass))
        
        self.x = self.x + self.vx*dt
        self.y = self.y + self.vy*dt

dt = 0.01
T = 0
T_max = 1000

M = float(input("Enter mass of star"))
m1, m2 = map(float, input("Enter mass of planet 1 and planet 2").split())
x1, y1 = map(float, input("Enter x and y coordinates of planet 1").split())
x2, y2 = map(float, input("Enter x and y coordinates of planet 2").split())
u_x1, u_y1 = map(float, input("Enter x and y velocities of planet 1").split())
u_x2, u_y2 = map(float, input("Enter x and y velocities of planet 2").split())

position_x1, position_y1 = [], []
position_x2, position_y2 = [], []
position_x1.append(x1)
position_y1.append(y1)
position_x2.append(x2)
position_y2.append(y2)

star = Body(M, 0, 0, 0, 0)
planet1 = Body(m1, x1, y1, u_x1, u_y1)
planet2 = Body(m2, x2, y2, u_x2, u_y2)

while T<=T_max:
    fxplanet1, fyplanet1 = planet1.grav_force(planet2)
    fxstar1, fystar1 = planet1.grav_force(star)
    fxstar2, fystar2 = planet2.grav_force(star)
    
    netxplanet1 = fxplanet1 + fxstar1
    netyplanet1 = fyplanet1 + fystar1
    netxplanet2 = -fxplanet1 + fxstar2
    netyplanet2 = -fyplanet1 + fystar2
    
    planet1.update(netxplanet1, netyplanet1, dt)
    planet2.update(netxplanet2, netyplanet2, dt)
    
    position_x1.append(planet1.x)
    position_y1.append(planet1.y)
    position_x2.append(planet2.x)
    position_y2.append(planet2.y)
    
    T+=dt
    
plt.plot(position_x1, position_y1, label = "Planet 1")
plt.plot(position_x2, position_y2, label = "Planet 2")
plt.plot(0, 0, 'yo', markersize=10)
plt.title("Orbit 2")
plt.xlabel("Horizontal Displacmement")
plt.ylabel("Vertical Displacment")
plt.legend()
plt.show()