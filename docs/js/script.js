// Efectos visuales y comportamiento para el sitio web de Chat GPT Local

document.addEventListener('DOMContentLoaded', function() {
  // Añadir efecto de terminal escribiendo para ciertos textos
  const typingElements = document.querySelectorAll('.typing-effect');
  
  typingElements.forEach(element => {
    const text = element.textContent;
    element.textContent = '';
    
    let i = 0;
    const typing = setInterval(() => {
      if (i < text.length) {
        element.textContent += text.charAt(i);
        i++;
      } else {
        clearInterval(typing);
      }
    }, 50);
  });

  // Navegación suave al hacer scroll
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      e.preventDefault();
      
      document.querySelector(this.getAttribute('href')).scrollIntoView({
        behavior: 'smooth'
      });
    });
  });

  // Animaciones al hacer scroll
  const animateOnScroll = () => {
    const elements = document.querySelectorAll('.animate-on-scroll');
    
    elements.forEach(element => {
      const elementPosition = element.getBoundingClientRect().top;
      const windowHeight = window.innerHeight;
      
      if (elementPosition < windowHeight - 50) {
        element.classList.add('animate');
      }
    });
  }
  
  window.addEventListener('scroll', animateOnScroll);
  animateOnScroll(); // Ejecutar una vez al cargar la página
  
  // Añadir efecto cyberpunk de scanline a elementos con la clase scanner
  const scannerElements = document.querySelectorAll('.scanner');
  
  scannerElements.forEach(element => {
    const scanline = document.createElement('div');
    scanline.classList.add('scanline');
    element.appendChild(scanline);
  });
});

// Efecto de parallax para el fondo
window.addEventListener('mousemove', function(e) {
  const parallaxElements = document.querySelectorAll('.parallax');
  
  parallaxElements.forEach(element => {
    const speed = element.getAttribute('data-speed');
    const x = (window.innerWidth - e.pageX * speed) / 100;
    const y = (window.innerHeight - e.pageY * speed) / 100;
    
    element.style.transform = `translateX(${x}px) translateY(${y}px)`;
  });
});