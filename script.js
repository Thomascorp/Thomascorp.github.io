document.addEventListener("DOMContentLoaded", () => {
    const elements = document.querySelectorAll("h1, p, li");
  
    elements.forEach((el, index) => {
      el.style.opacity = 0;
      el.style.transform = "translateY(20px)";
      el.style.transition = "opacity 0.6s ease-out, transform 0.6s ease-out";
      
      setTimeout(() => {
        el.style.opacity = 1;
        el.style.transform = "translateY(0)";
      }, index * 100);
    });
  });
  
  document.querySelectorAll("a").forEach(link => {
    link.addEventListener("mouseover", () => {
      link.style.transition = "transform 0.3s ease";
      link.style.transform = "scale(1.1)";
    });
  
    link.addEventListener("mouseout", () => {
      link.style.transform = "scale(1)";
    });
  });
  
document.addEventListener("DOMContentLoaded", function() {
  const scrollButton = document.getElementById('scroll-button');
  scrollButton.addEventListener('click', function(event) {
    event.preventDefault();
    const specialitesSection = document.getElementById('specialites');
        specialitesSection.scrollIntoView({
      behavior: 'smooth',
      block: 'start'
    });
  });
});

const items = document.querySelectorAll('.scroll-item');

const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
});

items.forEach(item => observer.observe(item));