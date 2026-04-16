// Global Features

document.addEventListener('DOMContentLoaded', () => {
  // ── Theme Toggle ──────────────────────────────────────────
  const btn = document.getElementById('theme-toggle');
  const stored = localStorage.getItem('toolsathi-theme');
  let dark = stored !== 'light'; // default: dark

  function setTheme(isDark) {
    dark = isDark;
    document.documentElement.setAttribute('data-theme', isDark ? 'dark' : 'light');
    localStorage.setItem('toolsathi-theme', isDark ? 'dark' : 'light');

    if (btn) {
      // Swap icon: show sun when dark, show moon when light
      btn.innerHTML = isDark
        ? `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#FCD34D" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>`
        : `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#A78BFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>`;
    }
  }

  // Apply on page load
  setTheme(dark);

  // Toggle on click
  if (btn) {
    btn.addEventListener('click', () => setTheme(!dark));
  }

  // Scroll effect on glass-nav header
  const header = document.querySelector('header.glass-nav');
  if (header) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 20) {
        header.style.background = 'rgba(8,11,20,0.85)';
        header.style.borderBottom = '1px solid var(--border-subtle)';
      } else {
        header.style.background = 'var(--nav-bg)';
        header.style.borderBottom = '1px solid var(--card-border)';
      }
    }, { passive: true });
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
