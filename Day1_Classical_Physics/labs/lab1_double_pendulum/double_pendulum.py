"""
Double Pendulum Simulation
-------------------------
This simulation demonstrates chaos in a double pendulum system using
numerical integration of the equations of motion.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import matplotlib.animation as animation

class DoublePendulum:
    def __init__(self, m1=1.0, m2=1.0, L1=1.0, L2=1.0, g=9.81):
        self.m1, self.m2 = m1, m2  # masses
        self.L1, self.L2 = L1, L2  # lengths
        self.g = g  # gravitational acceleration
        
    def derivatives(self, state, t):
        """Calculate derivatives of the state variables."""
        theta1, omega1, theta2, omega2 = state
        
        # Auxiliary quantities
        delta = theta2 - theta1
        den = (self.m1 + self.m2) * self.L1 - self.m2 * self.L1 * np.cos(delta) * np.cos(delta)
        
        # Derivatives
        theta1_dot = omega1
        theta2_dot = omega2
        
        omega1_dot = (self.m2 * self.L1 * omega1 * omega1 * np.sin(delta) * np.cos(delta)
                     + self.m2 * self.g * np.sin(theta2) * np.cos(delta)
                     + self.m2 * self.L2 * omega2 * omega2 * np.sin(delta)
                     - (self.m1 + self.m2) * self.g * np.sin(theta1)) / den
        
        omega2_dot = (-self.m2 * self.L2 * omega2 * omega2 * np.sin(delta) * np.cos(delta)
                     + (self.m1 + self.m2) * (self.g * np.sin(theta1) * np.cos(delta)
                     - self.L1 * omega1 * omega1 * np.sin(delta)
                     - self.g * np.sin(theta2))) / den
        
        return [theta1_dot, omega1_dot, theta2_dot, omega2_dot]
    
    def get_positions(self, theta1, theta2):
        """Calculate the (x,y) positions of both masses."""
        x1 = self.L1 * np.sin(theta1)
        y1 = -self.L1 * np.cos(theta1)
        
        x2 = x1 + self.L2 * np.sin(theta2)
        y2 = y1 - self.L2 * np.cos(theta2)
        
        return (x1, y1), (x2, y2)
    
    def simulate(self, initial_state, t_span, dt):
        """Simulate the double pendulum motion."""
        t = np.arange(0, t_span, dt)
        solution = odeint(self.derivatives, initial_state, t)
        return t, solution
    
    def animate(self, solution, dt):
        """Create animation of the double pendulum motion."""
        fig = plt.figure(figsize=(8, 8))
        ax = fig.add_subplot(111, aspect='equal')
        ax.grid()
        
        # Set the plot limits
        limit = self.L1 + self.L2 + 0.5
        ax.set_xlim(-limit, limit)
        ax.set_ylim(-limit, limit)
        
        # Initialize the line objects
        line, = ax.plot([], [], 'o-', lw=2)
        trace, = ax.plot([], [], 'r-', lw=1, alpha=0.2)
        
        # Trace of the second mass
        trace_x, trace_y = [], []
        
        def init():
            line.set_data([], [])
            trace.set_data([], [])
            return line, trace
        
        def animate(i):
            theta1, _, theta2, _ = solution[i]
            (x1, y1), (x2, y2) = self.get_positions(theta1, theta2)
            
            line.set_data([0, x1, x2], [0, y1, y2])
            
            trace_x.append(x2)
            trace_y.append(y2)
            trace.set_data(trace_x, trace_y)
            
            return line, trace
        
        anim = animation.FuncAnimation(fig, animate, init_func=init,
                                     frames=len(solution), interval=dt*1000,
                                     blit=True)
        plt.show()
        return anim

def main():
    # Create pendulum instance
    pendulum = DoublePendulum()
    
    # Initial conditions: [theta1, omega1, theta2, omega2]
    initial_state = [np.pi/2, 0, np.pi/2, 0]
    
    # Simulation parameters
    t_span = 30  # seconds
    dt = 0.02    # time step
    
    # Run simulation
    t, solution = pendulum.simulate(initial_state, t_span, dt)
    
    # Create animation
    pendulum.animate(solution, dt)
    
    # Plot energy over time (optional)
    plt.figure(figsize=(10, 5))
    plt.plot(t, solution[:, 1], label='Angular velocity 1')
    plt.plot(t, solution[:, 3], label='Angular velocity 2')
    plt.xlabel('Time (s)')
    plt.ylabel('Angular velocity (rad/s)')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    main()
