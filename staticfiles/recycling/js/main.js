document.addEventListener('DOMContentLoaded', (event) => {
    const burgerMenu = document.getElementById('burger-menu');
    const menu = document.getElementById('menu');
  
    burgerMenu.addEventListener('click', () => {
      menu.classList.toggle('active');
    });
  });
  

  