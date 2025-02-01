// Initialize Reveal.js
Reveal.initialize({
    controls: true,
    progress: true,
    center: false,
    hash: true,
    transition: 'slide',
    // Learn about plugins: https://revealjs.com/plugins/
    plugins: []
});

// Three.js Animations
class PhysicsAnimation {
    constructor(containerId) {
        this.container = document.getElementById(containerId);
        this.scene = new THREE.Scene();
        this.camera = new THREE.PerspectiveCamera(75, this.container.clientWidth / this.container.clientHeight, 0.1, 1000);
        this.renderer = new THREE.WebGLRenderer({ antialias: true });
        
        this.renderer.setSize(this.container.clientWidth, this.container.clientHeight);
        this.container.appendChild(this.renderer.domElement);
        
        this.camera.position.z = 5;
        
        // Handle window resize
        window.addEventListener('resize', () => this.onWindowResize(), false);
    }

    onWindowResize() {
        this.camera.aspect = this.container.clientWidth / this.container.clientHeight;
        this.camera.updateProjectionMatrix();
        this.renderer.setSize(this.container.clientWidth, this.container.clientHeight);
    }
}

// Newton's Laws Animation
class NewtonAnimation extends PhysicsAnimation {
    constructor() {
        super('newton-animation');
        
        // Add a cube to represent an object
        const geometry = new THREE.BoxGeometry();
        const material = new THREE.MeshBasicMaterial({ color: 0x58a6ff });
        this.cube = new THREE.Mesh(geometry, material);
        this.scene.add(this.cube);
        
        this.animate();
    }

    animate() {
        requestAnimationFrame(() => this.animate());
        
        // Rotate the cube
        this.cube.rotation.x += 0.01;
        this.cube.rotation.y += 0.01;
        
        this.renderer.render(this.scene, this.camera);
    }
}

// Conservation Laws Animation
class ConservationAnimation extends PhysicsAnimation {
    constructor() {
        super('conservation-animation');
        
        // Add two spheres to demonstrate conservation of momentum
        const geometry = new THREE.SphereGeometry(0.5);
        const material1 = new THREE.MeshBasicMaterial({ color: 0x58a6ff });
        const material2 = new THREE.MeshBasicMaterial({ color: 0xff5858 });
        
        this.sphere1 = new THREE.Mesh(geometry, material1);
        this.sphere2 = new THREE.Mesh(geometry, material2);
        
        this.sphere1.position.x = -2;
        this.sphere2.position.x = 2;
        
        this.scene.add(this.sphere1);
        this.scene.add(this.sphere2);
        
        this.animate();
    }

    animate() {
        requestAnimationFrame(() => this.animate());
        
        // Animate the spheres
        this.sphere1.position.x = -2 * Math.cos(Date.now() * 0.001);
        this.sphere2.position.x = 2 * Math.cos(Date.now() * 0.001);
        
        this.renderer.render(this.scene, this.camera);
    }
}

// Double Pendulum Animation
class PendulumAnimation extends PhysicsAnimation {
    constructor() {
        super('pendulum-simulation');
        
        // Create pendulum arms
        const geometry = new THREE.CylinderGeometry(0.1, 0.1, 2);
        const material = new THREE.MeshBasicMaterial({ color: 0x58a6ff });
        
        this.arm1 = new THREE.Mesh(geometry, material);
        this.arm2 = new THREE.Mesh(geometry, material);
        
        this.arm1.position.y = 1;
        this.arm2.position.y = -1;
        
        this.scene.add(this.arm1);
        this.arm1.add(this.arm2);
        
        this.animate();
    }

    animate() {
        requestAnimationFrame(() => this.animate());
        
        // Animate the pendulum
        this.arm1.rotation.z = Math.sin(Date.now() * 0.001) * 0.5;
        this.arm2.rotation.z = Math.cos(Date.now() * 0.001) * 0.5;
        
        this.renderer.render(this.scene, this.camera);
    }
}

// Initialize animations when the DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new NewtonAnimation();
    new ConservationAnimation();
    new PendulumAnimation();
});
