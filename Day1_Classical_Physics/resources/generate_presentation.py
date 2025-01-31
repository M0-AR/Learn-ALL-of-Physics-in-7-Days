"""
Classical Mechanics Presentation Generator
---------------------------------------
Generates a PDF presentation from the lecture content with
interactive visualizations and equations.
"""

from fpdf import FPDF
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg
import io
import os

class PresentationGenerator(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=15)
        self.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
        self.add_font('DejaVu', 'B', 'DejaVuSansCondensed-Bold.ttf', uni=True)
        
    def header(self):
        self.set_font('DejaVu', 'B', 12)
        self.cell(0, 10, 'Classical Mechanics: From Newton to Hamilton', 0, 1, 'C')
        self.ln(10)
        
    def footer(self):
        self.set_y(-15)
        self.set_font('DejaVu', '', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')
        
    def chapter_title(self, title):
        self.set_font('DejaVu', 'B', 16)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(10)
        
    def chapter_body(self, text):
        self.set_font('DejaVu', '', 12)
        self.multi_cell(0, 10, text)
        self.ln()
        
    def add_equation(self, equation):
        self.set_font('DejaVu', '', 12)
        self.cell(0, 10, equation, 0, 1, 'C')
        self.ln(5)
        
    def add_plot(self, fig):
        # Convert matplotlib figure to PNG image
        img_bytes = io.BytesIO()
        canvas = FigureCanvasAgg(fig)
        canvas.print_png(img_bytes)
        img_bytes.seek(0)
        
        # Add to PDF
        self.image(img_bytes, x=10, w=190)
        plt.close(fig)
        self.ln(10)

def generate_plots():
    plots = []
    
    # 1. Simple Harmonic Oscillator
    def plot_sho():
        fig, ax = plt.subplots(figsize=(10, 5))
        t = np.linspace(0, 10, 1000)
        x = np.cos(t)
        v = -np.sin(t)
        
        ax.plot(t, x, label='Position')
        ax.plot(t, v, label='Velocity')
        ax.set_title('Simple Harmonic Oscillator')
        ax.set_xlabel('Time')
        ax.set_ylabel('Amplitude')
        ax.grid(True)
        ax.legend()
        return fig
    
    # 2. Phase Space Plot
    def plot_phase_space():
        fig, ax = plt.subplots(figsize=(8, 8))
        theta = np.linspace(0, 2*np.pi, 100)
        x = np.cos(theta)
        p = -np.sin(theta)
        
        ax.plot(x, p)
        ax.set_title('Phase Space: Simple Harmonic Oscillator')
        ax.set_xlabel('Position (x)')
        ax.set_ylabel('Momentum (p)')
        ax.grid(True)
        ax.axis('equal')
        return fig
    
    # 3. Conservation of Energy
    def plot_energy():
        fig, ax = plt.subplots(figsize=(10, 5))
        t = np.linspace(0, 10, 1000)
        KE = np.sin(t)**2
        PE = np.cos(t)**2
        E = KE + PE
        
        ax.plot(t, KE, label='Kinetic Energy')
        ax.plot(t, PE, label='Potential Energy')
        ax.plot(t, E, label='Total Energy')
        ax.set_title('Conservation of Energy')
        ax.set_xlabel('Time')
        ax.set_ylabel('Energy')
        ax.grid(True)
        ax.legend()
        return fig
    
    plots.extend([plot_sho(), plot_phase_space(), plot_energy()])
    return plots

def main():
    # Create PDF
    pdf = PresentationGenerator()
    
    # Generate plots
    plots = generate_plots()
    
    # Title Page
    pdf.add_page()
    pdf.set_font('DejaVu', 'B', 24)
    pdf.cell(0, 60, 'Classical Mechanics:', 0, 1, 'C')
    pdf.cell(0, 20, 'From Newton to Hamilton', 0, 1, 'C')
    pdf.set_font('DejaVu', '', 14)
    pdf.cell(0, 20, 'A Modern Computational Approach', 0, 1, 'C')
    
    # Newton's Laws
    pdf.add_page()
    pdf.chapter_title("1. Newton's Laws")
    pdf.chapter_body("Newton's laws form the foundation of classical mechanics:")
    pdf.add_equation("1. F = 0 ⟹ v = constant (Law of Inertia)")
    pdf.add_equation("2. F = ma (Force Law)")
    pdf.add_equation("3. F₁₂ = -F₂₁ (Action-Reaction)")
    
    # Conservation Laws
    pdf.add_page()
    pdf.chapter_title("2. Conservation Laws")
    pdf.chapter_body("These fundamental principles govern the behavior of physical systems:")
    pdf.add_equation("Linear Momentum: p = mv")
    pdf.add_equation("Angular Momentum: L = r × p")
    pdf.add_equation("Energy: E = T + V")
    pdf.add_plot(plots[2])  # Energy conservation plot
    
    # Simple Harmonic Oscillator
    pdf.add_page()
    pdf.chapter_title("3. Simple Harmonic Oscillator")
    pdf.chapter_body("A fundamental system demonstrating periodic motion:")
    pdf.add_equation("mẍ + kx = 0")
    pdf.add_plot(plots[0])  # SHO plot
    
    # Phase Space
    pdf.add_page()
    pdf.chapter_title("4. Phase Space Analysis")
    pdf.chapter_body("Phase space reveals the complete state of a system:")
    pdf.add_plot(plots[1])  # Phase space plot
    
    # Save PDF
    output_path = 'classical_mechanics_presentation.pdf'
    pdf.output(output_path)
    print(f"Presentation generated: {output_path}")

if __name__ == '__main__':
    main()
