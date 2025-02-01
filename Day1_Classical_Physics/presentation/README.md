# Classical Physics Interactive Presentation

An interactive web-based presentation for teaching Classical Physics, built with Reveal.js and Three.js. This presentation includes dynamic visualizations and animations to help students understand complex physics concepts.

## 🚀 Features

- **Interactive 3D Animations** powered by Three.js
  - Newton's Laws demonstrations
  - Conservation of momentum visualization
  - Double pendulum simulation
- **Responsive Design** that works on all devices
- **Keyboard Navigation** for smooth presentation flow
- **Mathematical Equations** support
- **Modern UI** with smooth transitions

## 📖 Content Covered

1. **Classical Mechanics**
   - Newton's Laws
   - Conservation Laws
   - Lagrangian Mechanics

2. **Interactive Labs**
   - Double Pendulum Simulation
   - Planetary Motion
   - Hamiltonian Systems

3. **Code Challenges**
   - Advanced Projectile Motion
   - N-Body Gravitational Problem
   - Chaos in Simple Systems

## 🛠️ Technical Stack

- **Reveal.js** - For presentation framework
- **Three.js** - For 3D animations and physics simulations
- **HTML5/CSS3** - For structure and styling
- **JavaScript** - For interactivity and animations

## 🎯 Getting Started

1. **Opening the Presentation**
   - Open `index.html` in a modern web browser
   - For best experience, use Chrome or Firefox

2. **Navigation**
   - Use arrow keys (←/→) to navigate between slides
   - Press 'F' for fullscreen mode
   - Press 'S' for speaker notes
   - Press 'ESC' for slide overview

3. **Recording**
   - Use any screen recording software to capture the presentation
   - Recommended: OBS Studio for high-quality recording

## ⚙️ Customization

### Adding New Slides
Add new sections to `index.html`:
```html
<section>
    <h2>Your New Topic</h2>
    <ul>
        <li>Point 1</li>
        <li>Point 2</li>
    </ul>
</section>
```

### Creating New Animations
1. Create a new class in `script.js`:
```javascript
class YourAnimation extends PhysicsAnimation {
    constructor() {
        super('your-animation-container');
        // Your animation setup
    }
    
    animate() {
        requestAnimationFrame(() => this.animate());
        // Your animation logic
        this.renderer.render(this.scene, this.camera);
    }
}
```

2. Initialize it in the DOM content loaded event:
```javascript
document.addEventListener('DOMContentLoaded', () => {
    new YourAnimation();
});
```

## 🎨 Styling

- Edit `style.css` to customize the presentation's appearance
- Current theme uses a dark background with light text
- Animations containers are styled for optimal visibility

## 📝 Dependencies

- Reveal.js 4.3.1
- Three.js r128
- Modern web browser with WebGL support

## 🔍 Browser Support

- Chrome (recommended)
- Firefox
- Safari
- Edge

## 📱 Responsive Design

The presentation is fully responsive and works on:
- Desktop computers
- Laptops
- Tablets
- Mobile devices

## 🤝 Contributing

Feel free to:
1. Fork the repository
2. Create new animations
3. Add more interactive elements
4. Improve existing visualizations
5. Submit pull requests

## 📄 License

This presentation is available under the MIT License. Feel free to use and modify it for your educational purposes.
