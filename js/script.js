// Global Features

document.addEventListener('DOMContentLoaded', () => {
  // Theme Toggle
  const themeToggleParam = document.getElementById('theme-toggle');
  const currentTheme = localStorage.getItem('theme');
  
  if (currentTheme) {
    document.documentElement.setAttribute('data-theme', currentTheme);
    if(themeToggleParam) {
      themeToggleParam.textContent = currentTheme === 'dark' ? '☀️' : '🌙';
    }
  }

  if (themeToggleParam) {
    themeToggleParam.addEventListener('click', () => {
      let theme = document.documentElement.getAttribute('data-theme');
      if (theme === 'dark') {
        document.documentElement.removeAttribute('data-theme');
        localStorage.setItem('theme', 'light');
        themeToggleParam.textContent = '🌙';
      } else {
        document.documentElement.setAttribute('data-theme', 'dark');
        localStorage.setItem('theme', 'dark');
        themeToggleParam.textContent = '☀️';
      }
    });
  }

  // Mobile Navigation
  const hamburger = document.getElementById('hamburger');
  const mobileMenu = document.getElementById('mobile-menu');
  
  if (hamburger && mobileMenu) {
    hamburger.addEventListener('click', () => {
      const isOpen = mobileMenu.style.display === 'flex';
      
      if (isOpen) {
        mobileMenu.style.display = 'none';
        
        // Reset hamburger lines
        const lines = hamburger.querySelectorAll('.hamburger-line');
        if(lines.length === 3){
             lines[0].style.transform = 'none';
             lines[1].style.opacity = '1';
             lines[2].style.transform = 'none';
        }
      } else {
        mobileMenu.style.display = 'flex';
        
        // Animate hamburger lines matching React layout props
        const lines = hamburger.querySelectorAll('.hamburger-line');
        if(lines.length === 3){
             lines[0].style.transform = 'translateY(7px) rotate(45deg)';
             lines[1].style.opacity = '0';
             lines[2].style.transform = 'translateY(-7px) rotate(-45deg)';
        }
      }
    });
  }

  // Copy Prompt Functionality
  const copyButtons = document.querySelectorAll('.copy-btn');
  copyButtons.forEach(btn => {
    btn.addEventListener('click', (e) => {
      const targetId = e.target.getAttribute('data-target');
      const textToCopy = document.getElementById(targetId).textContent;
      
      navigator.clipboard.writeText(textToCopy).then(() => {
        const originalText = e.target.textContent;
        e.target.textContent = 'Copied!';
        setTimeout(() => {
          e.target.textContent = originalText;
        }, 2000);
      }).catch(err => {
        console.error('Failed to copy text: ', err);
      });
    });
  });

  // Login Functionality
  const loginForm = document.getElementById('login-form');
  if (loginForm) {
    loginForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const user = document.getElementById('username').value;
      const pass = document.getElementById('password').value;
      const errorMsg = document.getElementById('login-error');

      if (user === 'admin' && pass === '1234') {
        // Redirect to admin dashboard
        window.location.href = 'admin.html';
      } else {
        errorMsg.style.display = 'block';
        errorMsg.textContent = 'Invalid username or password';
      }
    });
  }
});
