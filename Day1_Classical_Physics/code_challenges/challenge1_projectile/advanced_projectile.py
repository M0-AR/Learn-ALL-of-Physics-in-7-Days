"""
Advanced Projectile Motion Simulator
----------------------------------
This simulation includes:
- Air resistance (quadratic drag)
- Magnus force (spin effects)
- Coriolis effect
- Variable air density with altitude
"""

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class AdvancedProjectile:
    def __init__(self, mass=0.145, radius=0.037, spin_rate=50.0):
        # Physical parameters
        self.mass = mass  # kg
        self.radius = radius  # m
        self.area = np.pi * radius**2  # m²
        self.spin_rate = spin_rate  # rad/s
        
        # Environmental constants
        self.g = 9.81  # m/s²
        self.rho_0 = 1.225  # kg/m³ (sea level air density)
        self.H = 7400  # m (scale height)
        self.omega_earth = 7.2921e-5  # rad/s (Earth's angular velocity)
        
        # Aerodynamic coefficients
        self.Cd = 0.47  # drag coefficient
        self.Cl = 0.33  # lift coefficient
        
    def air_density(self, y):
        """Calculate air density at height y."""
        return self.rho_0 * np.exp(-y / self.H)
    
    def forces(self, t, state):
        """Calculate all forces acting on the projectile."""
        x, y, z, vx, vy, vz = state
        v = np.array([vx, vy, vz])
        speed = np.linalg.norm(v)
        
        # Unit vector in velocity direction
        if speed > 0:
            v_hat = v / speed
        else:
            v_hat = np.zeros(3)
        
        # Air density at current height
        rho = self.air_density(y)
        
        # Drag force
        F_drag = -0.5 * rho * self.area * self.Cd * speed**2 * v_hat
        
        # Magnus force (due to spin)
        spin_vector = np.array([0, 1, 0]) * self.spin_rate
        F_magnus = (self.Cl * self.area * rho * speed *
                   np.cross(spin_vector, v))
        
        # Coriolis force
        latitude = 45.0  # degrees (example latitude)
        omega = np.array([0, 
                         self.omega_earth * np.cos(np.radians(latitude)),
                         self.omega_earth * np.sin(np.radians(latitude))])
        F_coriolis = -2 * self.mass * np.cross(omega, v)
        
        # Gravitational force
        F_gravity = np.array([0, -self.mass * self.g, 0])
        
        # Total force
        F_total = F_drag + F_magnus + F_coriolis + F_gravity
        
        # Acceleration
        a = F_total / self.mass
        
        return [vx, vy, vz, a[0], a[1], a[2]]
    
    def simulate(self, initial_state, t_span, dt):
        """Simulate the projectile motion."""
        t_eval = np.arange(0, t_span, dt)
        solution = solve_ivp(self.forces, [0, t_span], initial_state,
                           t_eval=t_eval, method='RK45')
        return solution.t, solution.y
    
    def plot_trajectory(self, t, solution):
        """Plot the 3D trajectory with time-colored path."""
        fig = plt.figure(figsize=(12, 8))
        ax = fig.add_subplot(111, projection='3d')
        
        # Extract positions
        x, y, z = solution[0], solution[1], solution[2]
        
        # Color points by time
        colors = plt.cm.viridis(t/t[-1])
        
        # Plot trajectory
        ax.scatter(x, z, y, c=t, cmap='viridis')
        
        # Add color bar
        sm = plt.cm.ScalarMappable(cmap='viridis')
        sm.set_array(t)
        plt.colorbar(sm, label='Time (s)')
        
        # Labels and title
        ax.set_xlabel('X (m)')
        ax.set_ylabel('Z (m)')
        ax.set_zlabel('Y (m)')
        ax.set_title('Advanced Projectile Motion')
        
        plt.show()

def main():
    # Create projectile instance
    projectile = AdvancedProjectile()
    
    # Initial conditions: [x, y, z, vx, vy, vz]
    v0 = 50.0  # m/s
    angle = 45.0  # degrees
    initial_state = [0, 0, 0,  # initial position
                    v0 * np.cos(np.radians(angle)), # initial velocity x
                    v0 * np.sin(np.radians(angle)), # initial velocity y
                    0]                              # initial velocity z
    
    # Simulation parameters
    t_span = 10.0  # seconds
    dt = 0.01      # time step
    
    # Run simulation
    t, solution = projectile.simulate(initial_state, t_span, dt)
    
    # Plot results
    projectile.plot_trajectory(t, solution)
    
    # Print maximum height and distance
    max_height = np.max(solution[1])
    max_distance = solution[0][-1]
    print(f"Maximum height: {max_height:.2f} m")
    print(f"Maximum distance: {max_distance:.2f} m")

if __name__ == '__main__':
    main()
