import os
import re

HEADER_TEMPLATE_ROOT = """  <!-- Navigation -->
  <header class="glass-nav">
    <div class="header-container flex-between">
      <a href="[[PREFIX]]index.html" class="logo group">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="color: var(--accent-violet);"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
        <span class="font-display font-semibold text-lg" style="color: var(--text-primary);">Toolsathi</span>
      </a>

      <!-- Desktop Nav -->
      <nav class="nav-links" id="nav-links">
        <a href="[[PREFIX]]index.html" class="nav-item">Home</a>
        <div class="dropdown-wrapper">
          <a href="[[PREFIX]]index.html#tools" class="nav-item flex-center gap-1 dropdown-toggle">
            Tools
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M6 9l6 6 6-6" /></svg>
          </a>
          <div class="dropdown-content glass-card">
            <a href="[[PREFIX]]tools/age-calculator.html">🎂 Age Calculator</a>
            <a href="[[PREFIX]]tools/cgpa-calculator.html">🎓 CGPA Calculator</a>
            <a href="[[PREFIX]]tools/emi-calculator.html">💰 EMI Calculator</a>
            <a href="[[PREFIX]]tools/percentage-calculator.html">📊 Percentage Calc</a>
            <a href="[[PREFIX]]tools/bmi-calculator.html">⚖️ BMI Calculator</a>
            <a href="[[PREFIX]]tools/discount-calculator.html">🏷️ Discount Calc</a>
          </div>
        </div>
        <a href="[[PREFIX]]ai-tools.html" class="nav-item">AI Tools</a>
        <a href="[[PREFIX]]blog.html" class="nav-item">Blog</a>
        <a href="[[PREFIX]]about.html" class="nav-item">About</a>
      </nav>

      <!-- Right side -->
      <div class="flex-center gap-3">
        <button class="theme-toggle flex-center" id="theme-toggle" aria-label="Toggle dark mode">
          <!-- Toggle icon swapped dynamically by JS, default moon -->
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="color: #FCD34D;"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>
        </button>
        <button class="hamburger" id="hamburger">
          <span class="hamburger-line"></span>
          <span class="hamburger-line"></span>
          <span class="hamburger-line"></span>
        </button>
      </div>
    </div>
  </header>"""

FOOTER_TEMPLATE_ROOT = """  <footer class="site-footer" style="border-top: 1px solid var(--border-subtle); margin-top: 4rem;">
    <div class="footer-container" style="max-width: 1200px; margin: 0 auto; padding: 3rem 5%; position: relative; z-index: 10;">
      <div class="footer-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 2rem; margin-bottom: 2rem;">
        
        <div class="footer-col">
          <div class="flex-center gap-2 mb-3" style="justify-content: flex-start; margin-bottom: 0.75rem;">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="color: var(--accent-violet);"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
            <span class="font-display font-semibold text-sm" style="color: var(--text-primary); font-size: 0.875rem; font-weight: 600;">Toolsathi</span>
          </div>
          <p class="text-xs" style="color: var(--text-muted); font-size: 0.75rem; line-height: 1.6;">Free tools for students. Built by Kalva Ajay Kumar — CSE student & YouTuber.</p>
        </div>

        <div class="footer-col">
          <p class="text-xs uppercase tracking-widest" style="color: var(--text-muted); font-size: 0.75rem; font-weight: 600; letter-spacing: 0.1em; margin-bottom: 0.75rem; text-transform: uppercase;">Pages</p>
          <div style="display: flex; flex-direction: column; gap: 0.5rem;">
            <a href="[[PREFIX]]index.html" style="color: var(--text-muted); font-size: 0.875rem;">Home</a>
            <a href="[[PREFIX]]ai-tools.html" style="color: var(--text-muted); font-size: 0.875rem;">AI Tools</a>
            <a href="[[PREFIX]]blog.html" style="color: var(--text-muted); font-size: 0.875rem;">Blog</a>
            <a href="[[PREFIX]]about.html" style="color: var(--text-muted); font-size: 0.875rem;">About</a>
          </div>
        </div>

        <div class="footer-col">
          <p class="text-xs uppercase tracking-widest" style="color: var(--text-muted); font-size: 0.75rem; font-weight: 600; letter-spacing: 0.1em; margin-bottom: 0.75rem; text-transform: uppercase;">Tools</p>
          <div style="display: flex; flex-direction: column; gap: 0.5rem;">
            <a href="[[PREFIX]]tools/age-calculator.html" style="color: var(--text-muted); font-size: 0.875rem;">Age Calculator</a>
            <a href="[[PREFIX]]tools/cgpa-calculator.html" style="color: var(--text-muted); font-size: 0.875rem;">CGPA Calculator</a>
            <a href="[[PREFIX]]tools/emi-calculator.html" style="color: var(--text-muted); font-size: 0.875rem;">EMI Calculator</a>
            <a href="[[PREFIX]]tools/percentage-calculator.html" style="color: var(--text-muted); font-size: 0.875rem;">Percentage Calc</a>
            <a href="[[PREFIX]]tools/bmi-calculator.html" style="color: var(--text-muted); font-size: 0.875rem;">BMI Calculator</a>
            <a href="[[PREFIX]]tools/discount-calculator.html" style="color: var(--text-muted); font-size: 0.875rem;">Discount Calc</a>
          </div>
        </div>

        <div class="footer-col">
          <p class="text-xs uppercase tracking-widest" style="color: var(--text-muted); font-size: 0.75rem; font-weight: 600; letter-spacing: 0.1em; margin-bottom: 0.75rem; text-transform: uppercase;">Creator</p>
          <div style="display: flex; flex-direction: column; gap: 0.25rem;">
            <p style="color: var(--text-secondary); font-size: 0.875rem; font-weight: 600;">Kalva Ajay Kumar</p>
            <p style="color: var(--text-muted); font-size: 0.75rem;">CSE Student · YouTuber</p>
          </div>
        </div>

      </div>

      <div class="flex-between" style="border-top: 1px solid var(--border-subtle); padding-top: 1.5rem; flex-wrap: wrap; gap: 1rem;">
        <p style="color: var(--text-muted); font-size: 0.75rem;">© 2026 Toolsathi — All rights reserved</p>
        <div style="display: flex; gap: 1rem;">
          <a href="[[PREFIX]]login.html" style="color: var(--text-muted); font-size: 0.75rem;">Admin</a>
          <a href="[[PREFIX]]about.html" style="color: var(--text-muted); font-size: 0.75rem;">About</a>
        </div>
      </div>
    </div>
  </footer>"""

def process_file(filepath, is_tool=False):
    prefix = "../" if is_tool else ""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Admin UI is different enough that replacing its header might break its sidebar structure entirely.
    # It has `<aside>` instead of `<header>`. Let's skip admin.html header, but replace login.html's if it exists.
    if "admin.html" in filepath:
        return

    # Replace header block
    # Matches <header class="glass-nav">...</header>
    header_pattern = re.compile(r'<!-- Navigation -->\s*<header.*?</header>', re.DOTALL)
    header_replacement = HEADER_TEMPLATE_ROOT.replace('[[PREFIX]]', prefix)
    
    # If file doesn't have the normal header structure (like login.html which might not), skip header replacement
    if header_pattern.search(content):
        content = header_pattern.sub(header_replacement, content)
        
    # Replace footer block
    footer_pattern = re.compile(r'<footer.*?</footer\s*>', re.DOTALL)
    footer_replacement = FOOTER_TEMPLATE_ROOT.replace('[[PREFIX]]', prefix)
    
    if footer_pattern.search(content):
        content = footer_pattern.sub(footer_replacement, content)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

base_dir = r"d:\Toolsathi"

import glob

for filename in glob.glob(os.path.join(base_dir, "*.html")):
    process_file(filename, False)

tool_dir = os.path.join(base_dir, "tools")
for filename in glob.glob(os.path.join(tool_dir, "*.html")):
    process_file(filename, True)

print("Updated HTML files.")
