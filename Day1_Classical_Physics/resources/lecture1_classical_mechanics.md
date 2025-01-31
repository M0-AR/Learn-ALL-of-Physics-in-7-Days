# Classical Mechanics: From Newton to Hamilton

## 1. Newtonian Mechanics

### Newton's Laws
1. **First Law (Inertia)**
   - An object remains at rest or in uniform motion unless acted upon by a force
   - Mathematical form: ∑F = 0 ⟹ v = constant

2. **Second Law (F = ma)**
   - Force equals mass times acceleration
   - Mathematical form: F = ma = m(dv/dt) = m(d²x/dt²)

3. **Third Law (Action-Reaction)**
   - For every action, there is an equal and opposite reaction
   - Mathematical form: F₁₂ = -F₂₁

### Conservation Laws
1. **Conservation of Linear Momentum**
   - p = mv
   - dp/dt = 0 (in absence of external forces)

2. **Conservation of Angular Momentum**
   - L = r × p
   - dL/dt = 0 (in absence of external torques)

3. **Conservation of Energy**
   - E = T + V (Kinetic + Potential)
   - dE/dt = 0 (in closed systems)

## 2. Lagrangian Mechanics

### The Principle of Least Action
- Action: S = ∫L dt
- Lagrangian: L = T - V
- Euler-Lagrange equation: d/dt(∂L/∂q̇) - ∂L/∂q = 0

### Advantages
1. Automatically incorporates constraints
2. Simplifies complex problems
3. Reveals symmetries and conservation laws

## 3. Hamiltonian Mechanics

### Hamilton's Equations
- H(q, p, t) = pq̇ - L
- dq/dt = ∂H/∂p
- dp/dt = -∂H/∂q

### Phase Space
- State space of (q, p)
- Preserves volume (Liouville's theorem)
- Natural framework for quantum mechanics

## 4. Applications

### Example: Simple Harmonic Oscillator
1. **Newtonian Approach**
   - F = -kx
   - mẍ + kx = 0

2. **Lagrangian Approach**
   - L = T - V = ½mẋ² - ½kx²
   - d/dt(mẋ) + kx = 0

3. **Hamiltonian Approach**
   - H = p²/2m + kx²/2
   - ẋ = p/m
   - ṗ = -kx

### Example: Double Pendulum
- See lab1_double_pendulum for practical implementation

## 5. Computational Considerations

### Numerical Integration Methods
1. Euler Method (simple but inaccurate)
2. Runge-Kutta Methods (RK4 commonly used)
3. Symplectic Integrators (preserve energy better)

### Error Analysis
1. Local truncation error
2. Global accumulation of error
3. Energy conservation in numerical solutions
