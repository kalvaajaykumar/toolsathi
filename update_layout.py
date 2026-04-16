import os
import re

HEADER_TEMPLATE_ROOT = """  <!-- Navigation -->
  <header class="glass-nav z-50" style="transition: all 0.3s; z-index: 50;">
    <div style="max-width: 72rem; margin: 0 auto; padding: 0 1rem; height: 4rem; display: flex; align-items: center; justify-content: space-between;">
      <a href="[[PREFIX]]index.html" class="logo flex items-center cursor-pointer hover:opacity-80 transition-opacity group" style="text-decoration: none; gap: 0.5rem;" >
        <img src="[[PREFIX]]assets/images/app_logo.png" alt="Toolsathi Logo" width="32" height="32" class="flex-shrink-0" style="border-radius: 0.25rem;" loading="lazy" onerror="this.onerror=null; this.outerHTML='<span style=\\'display:flex; width:32px; height:32px; align-items:center; justify-content:center; background:var(--accent-violet); color:white; border-radius:0.25rem; font-weight:bold;\\'>T</span>'" />
        <span class="font-display font-semibold text-lg tracking-tight" style="color: var(--text-primary);">Toolsathi</span>
      </a>

      <!-- Desktop Nav -->
      <nav class="nav-links" id="nav-links" style="align-items: center; gap: 0.25rem;">
        <a href="[[PREFIX]]index.html" class="nav-item" style="padding: 0.5rem 1rem; border-radius: 0.5rem; font-size: 0.875rem; font-weight: 500; transition: all 0.2s; color: var(--text-secondary); text-decoration: none;">Home</a>
        <a href="[[PREFIX]]ai-tools.html" class="nav-item" style="padding: 0.5rem 1rem; border-radius: 0.5rem; font-size: 0.875rem; font-weight: 500; transition: all 0.2s; color: var(--text-secondary); text-decoration: none;">AI Tools</a>
        <a href="[[PREFIX]]blog.html" class="nav-item" style="padding: 0.5rem 1rem; border-radius: 0.5rem; font-size: 0.875rem; font-weight: 500; transition: all 0.2s; color: var(--text-secondary); text-decoration: none;">Blog</a>
        <a href="[[PREFIX]]about.html" class="nav-item" style="padding: 0.5rem 1rem; border-radius: 0.5rem; font-size: 0.875rem; font-weight: 500; transition: all 0.2s; color: var(--text-secondary); text-decoration: none;">About</a>
        
        <div class="dropdown-wrapper" style="position: relative;">
          <a href="[[PREFIX]]index.html#tools" class="nav-item flex-center gap-1 dropdown-toggle" style="padding: 0.5rem 1rem; border-radius: 0.5rem; font-size: 0.875rem; font-weight: 500; transition: all 0.2s; color: var(--text-secondary); text-decoration: none; cursor: pointer;">
            Tools
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M6 9l6 6 6-6" /></svg>
          </a>
          <div class="dropdown-content" style="position: absolute; top: 100%; right: 0; margin-top: 0.25rem; width: 13rem; border-radius: 0.75rem; overflow: hidden; box-shadow: 0 25px 50px -12px rgba(0,0,0,0.25); background: rgba(13,17,32,0.97); border: 1px solid var(--border-subtle); backdrop-filter: blur(20px);">
            <a href="[[PREFIX]]tools/age-calculator.html" class="nav-item-tool" style="display: flex; align-items: center; padding: 0.625rem 1rem; font-size: 0.875rem; transition: all 0.2s; color: var(--text-secondary); text-decoration: none;">🎂 Age Calculator</a>
            <a href="[[PREFIX]]tools/cgpa-calculator.html" class="nav-item-tool" style="display: flex; align-items: center; padding: 0.625rem 1rem; font-size: 0.875rem; transition: all 0.2s; color: var(--text-secondary); text-decoration: none;">🎓 CGPA Calculator</a>
            <a href="[[PREFIX]]tools/emi-calculator.html" class="nav-item-tool" style="display: flex; align-items: center; padding: 0.625rem 1rem; font-size: 0.875rem; transition: all 0.2s; color: var(--text-secondary); text-decoration: none;">💰 EMI Calculator</a>
            <a href="[[PREFIX]]tools/percentage-calculator.html" class="nav-item-tool" style="display: flex; align-items: center; padding: 0.625rem 1rem; font-size: 0.875rem; transition: all 0.2s; color: var(--text-secondary); text-decoration: none;">📊 Percentage Calc</a>
            <a href="[[PREFIX]]tools/bmi-calculator.html" class="nav-item-tool" style="display: flex; align-items: center; padding: 0.625rem 1rem; font-size: 0.875rem; transition: all 0.2s; color: var(--text-secondary); text-decoration: none;">⚖️ BMI Calculator</a>
            <a href="[[PREFIX]]tools/discount-calculator.html" class="nav-item-tool" style="display: flex; align-items: center; padding: 0.625rem 1rem; font-size: 0.875rem; transition: all 0.2s; color: var(--text-secondary); text-decoration: none;">🏷️ Discount Calc</a>
          </div>
        </div>
      </nav>

      <!-- Right side -->
      <div style="display: flex; align-items: center; gap: 0.75rem;">
        <button class="theme-toggle flex-center transition-all hover-scale" id="theme-toggle" aria-label="Toggle dark mode" style="width: 2.25rem; height: 2.25rem; border-radius: 0.5rem; transition: transform 0.2s; background: var(--bg-card); border: 1px solid var(--border-subtle); cursor: pointer; display: flex; align-items: center; justify-content: center;">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" class="sun-icon" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="color: #FCD34D;"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>
        </button>
        <button class="hamburger md:hidden" id="hamburger" style="width: 2.25rem; height: 2.25rem; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 5px; background: transparent; border: none; cursor: pointer;">
          <span class="hamburger-line" style="width: 1.5rem; height: 2px; background: var(--text-primary); transition: all 0.3s transform;"></span>
          <span class="hamburger-line" style="width: 1.5rem; height: 2px; background: var(--text-primary); transition: all 0.3s opacity;"></span>
          <span class="hamburger-line" style="width: 1.5rem; height: 2px; background: var(--text-primary); transition: all 0.3s transform;"></span>
        </button>
      </div>    
    </div>

    <!-- Mobile menu -->
    <div class="mobile-menu" id="mobile-menu" style="position: absolute; top: 100%; left: 0; right: 0; background: rgba(8,11,20,0.97); backdrop-filter: blur(20px); border-bottom: 1px solid var(--border-subtle); display: none; flex-direction: column; padding: 1rem; gap: 0.25rem;">
      <a href="[[PREFIX]]index.html" class="nav-item" style="padding: 0.75rem 1rem; border-radius: 0.5rem; font-size: 0.875rem; font-weight: 500; color: var(--text-secondary); text-decoration: none;">Home</a>
      <a href="[[PREFIX]]ai-tools.html" class="nav-item" style="padding: 0.75rem 1rem; border-radius: 0.5rem; font-size: 0.875rem; font-weight: 500; color: var(--text-secondary); text-decoration: none;">AI Tools</a>
      <a href="[[PREFIX]]blog.html" class="nav-item" style="padding: 0.75rem 1rem; border-radius: 0.5rem; font-size: 0.875rem; font-weight: 500; color: var(--text-secondary); text-decoration: none;">Blog</a>
      <a href="[[PREFIX]]about.html" class="nav-item" style="padding: 0.75rem 1rem; border-radius: 0.5rem; font-size: 0.875rem; font-weight: 500; color: var(--text-secondary); text-decoration: none;">About</a>
      <div style="padding: 0.5rem 1rem; font-size: 0.75rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.1em; color: var(--text-muted); margin-top: 0.5rem;">Tools</div>
      <a href="[[PREFIX]]tools/age-calculator.html" class="nav-item-tool" style="padding: 0.625rem 1rem; border-radius: 0.5rem; font-size: 0.875rem; color: var(--text-secondary); text-decoration: none;">🎂 Age Calculator</a>
      <a href="[[PREFIX]]tools/cgpa-calculator.html" class="nav-item-tool" style="padding: 0.625rem 1rem; border-radius: 0.5rem; font-size: 0.875rem; color: var(--text-secondary); text-decoration: none;">🎓 CGPA Calculator</a>
      <a href="[[PREFIX]]tools/emi-calculator.html" class="nav-item-tool" style="padding: 0.625rem 1rem; border-radius: 0.5rem; font-size: 0.875rem; color: var(--text-secondary); text-decoration: none;">💰 EMI Calculator</a>
      <a href="[[PREFIX]]tools/percentage-calculator.html" class="nav-item-tool" style="padding: 0.625rem 1rem; border-radius: 0.5rem; font-size: 0.875rem; color: var(--text-secondary); text-decoration: none;">📊 Percentage Calc</a>
      <a href="[[PREFIX]]tools/bmi-calculator.html" class="nav-item-tool" style="padding: 0.625rem 1rem; border-radius: 0.5rem; font-size: 0.875rem; color: var(--text-secondary); text-decoration: none;">⚖️ BMI Calculator</a>
      <a href="[[PREFIX]]tools/discount-calculator.html" class="nav-item-tool" style="padding: 0.625rem 1rem; border-radius: 0.5rem; font-size: 0.875rem; color: var(--text-secondary); text-decoration: none;">🏷️ Discount Calc</a>
    </div>
  </header>"""

FOOTER_TEMPLATE_ROOT = """  <!-- Footer -->
  <footer class="relative z-10" style="position: relative; z-index: 10; border-top: 1px solid var(--border-subtle);">
    <div style="max-width: 72rem; margin: 0 auto; padding: 2.5rem 1rem;">
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 2rem; margin-bottom: 2rem;">
        
        <!-- Brand -->
        <div>
          <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.75rem;">
            <img src="[[PREFIX]]assets/images/app_logo.png" alt="Toolsathi Logo" width="24" height="24" class="flex-shrink-0" style="border-radius: 0.25rem;" loading="lazy" onerror="this.onerror=null; this.outerHTML='<span style=\\'display:flex; width:24px; height:24px; align-items:center; justify-content:center; background:var(--accent-violet); color:white; border-radius:0.25rem; font-weight:bold; font-size:12px;\\'>T</span>'" />
            <span class="font-display font-semibold text-sm" style="font-size: 0.875rem; color: var(--text-primary);">Toolsathi</span>
          </div>
          <p class="text-xs leading-relaxed" style="font-size: 0.75rem; line-height: 1.625; color: var(--text-muted);">
            Free tools for students. Built by Kalva Ajay Kumar — CSE student & YouTuber.
          </p>
        </div>

        <!-- Pages -->
        <div>
          <p class="text-xs font-semibold uppercase tracking-widest mb-3" style="font-size: 0.75rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 0.75rem; color: var(--text-muted);">Pages</p>
          <div style="display: flex; flex-direction: column; gap: 0.5rem;">
            <a href="[[PREFIX]]index.html" class="nav-item" style="display: block; font-size: 0.875rem; color: var(--text-muted); text-decoration: none; transition: color 0.2s;" onmouseover="this.style.color='white'" onmouseout="this.style.color='var(--text-muted)'">Home</a>
            <a href="[[PREFIX]]ai-tools.html" class="nav-item" style="display: block; font-size: 0.875rem; color: var(--text-muted); text-decoration: none; transition: color 0.2s;" onmouseover="this.style.color='white'" onmouseout="this.style.color='var(--text-muted)'">AI Tools</a>
            <a href="[[PREFIX]]blog.html" class="nav-item" style="display: block; font-size: 0.875rem; color: var(--text-muted); text-decoration: none; transition: color 0.2s;" onmouseover="this.style.color='white'" onmouseout="this.style.color='var(--text-muted)'">Blog</a>
            <a href="[[PREFIX]]about.html" class="nav-item" style="display: block; font-size: 0.875rem; color: var(--text-muted); text-decoration: none; transition: color 0.2s;" onmouseover="this.style.color='white'" onmouseout="this.style.color='var(--text-muted)'">About</a>
          </div>
        </div>

        <!-- Tools -->
        <div>
          <p class="text-xs font-semibold uppercase tracking-widest mb-3" style="font-size: 0.75rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 0.75rem; color: var(--text-muted);">Tools</p>
          <div style="display: flex; flex-direction: column; gap: 0.5rem;">
            <a href="[[PREFIX]]tools/age-calculator.html" class="nav-item" style="display: block; font-size: 0.875rem; color: var(--text-muted); text-decoration: none; transition: color 0.2s;" onmouseover="this.style.color='white'" onmouseout="this.style.color='var(--text-muted)'">Age Calculator</a>
            <a href="[[PREFIX]]tools/cgpa-calculator.html" class="nav-item" style="display: block; font-size: 0.875rem; color: var(--text-muted); text-decoration: none; transition: color 0.2s;" onmouseover="this.style.color='white'" onmouseout="this.style.color='var(--text-muted)'">CGPA Calculator</a>
            <a href="[[PREFIX]]tools/emi-calculator.html" class="nav-item" style="display: block; font-size: 0.875rem; color: var(--text-muted); text-decoration: none; transition: color 0.2s;" onmouseover="this.style.color='white'" onmouseout="this.style.color='var(--text-muted)'">EMI Calculator</a>
            <a href="[[PREFIX]]tools/percentage-calculator.html" class="nav-item" style="display: block; font-size: 0.875rem; color: var(--text-muted); text-decoration: none; transition: color 0.2s;" onmouseover="this.style.color='white'" onmouseout="this.style.color='var(--text-muted)'">Percentage Calc</a>
            <a href="[[PREFIX]]tools/bmi-calculator.html" class="nav-item" style="display: block; font-size: 0.875rem; color: var(--text-muted); text-decoration: none; transition: color 0.2s;" onmouseover="this.style.color='white'" onmouseout="this.style.color='var(--text-muted)'">BMI Calculator</a>
            <a href="[[PREFIX]]tools/discount-calculator.html" class="nav-item" style="display: block; font-size: 0.875rem; color: var(--text-muted); text-decoration: none; transition: color 0.2s;" onmouseover="this.style.color='white'" onmouseout="this.style.color='var(--text-muted)'">Discount Calc</a>
          </div>
        </div>

        <!-- Creator -->
        <div>
          <p class="text-xs font-semibold uppercase tracking-widest mb-3" style="font-size: 0.75rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 0.75rem; color: var(--text-muted);">Creator</p>
          <div style="display: flex; flex-direction: column; gap: 0.5rem;">
            <p class="text-sm font-semibold" style="font-size: 0.875rem; font-weight: 600; color: var(--text-secondary); margin: 0;">Kalva Ajay Kumar</p>
            <p class="text-xs" style="font-size: 0.75rem; color: var(--text-muted); margin: 0;">CSE Student · YouTuber</p>
            <div style="display: flex; gap: 0.75rem; margin-top: 0.75rem;">
              <a href="#" aria-label="YouTube" style="color: var(--text-muted); transition: color 0.2s;" onmouseover="this.style.color='#F87171'" onmouseout="this.style.color='var(--text-muted)'">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M23.495 6.205a3.007 3.007 0 0 0-2.088-2.088c-1.87-.501-9.396-.501-9.396-.501s-7.507-.01-9.396.501A3.007 3.007 0 0 0 .527 6.205a31.247 31.247 0 0 0-.522 5.805 31.247 31.247 0 0 0 .522 5.783 3.007 3.007 0 0 0 2.088 2.088c1.868.502 9.396.502 9.396.502s7.506 0 9.396-.502a3.007 3.007 0 0 0 2.088-2.088 31.247 31.247 0 0 0 .5-5.783 31.247 31.247 0 0 0-.5-5.805zM9.609 15.601V8.408l6.264 3.602z"/></svg>
              </a>
              <a href="#" aria-label="GitHub" style="color: var(--text-muted); transition: color 0.2s;" onmouseover="this.style.color='white'" onmouseout="this.style.color='var(--text-muted)'">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.374 0 0 5.373 0 12c0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23A11.509 11.509 0 0 1 12 5.803c1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576C20.566 21.797 24 17.3 24 12c0-6.627-5.373-12-12-12z"/></svg>
              </a>
            </div>
          </div>
        </div>
      </div>

      <div style="border-top: 1px solid var(--border-subtle); padding-top: 1.5rem; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 0.75rem;">
        <p class="text-xs" style="font-size: 0.75rem; color: var(--text-muted); margin: 0;">© 2026 Toolsathi — All rights reserved</p>
        <div style="display: flex; gap: 1rem;">
          <a href="[[PREFIX]]login.html" class="text-xs transition-colors" style="font-size: 0.75rem; color: var(--text-muted); text-decoration: none; transition: color 0.2s;" onmouseover="this.style.color='white'" onmouseout="this.style.color='var(--text-muted)'">Admin</a>
          <a href="[[PREFIX]]about.html" class="text-xs transition-colors" style="font-size: 0.75rem; color: var(--text-muted); text-decoration: none; transition: color 0.2s;" onmouseover="this.style.color='white'" onmouseout="this.style.color='var(--text-muted)'">About</a>
        </div>
      </div>
    </div>
  </footer>"""

def process_file(filepath, is_tool=False):
    prefix = "../" if is_tool else ""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Admin UI is different enough that replacing its header might break its sidebar structure entirely.
    if "admin.html" in filepath:
        return

    # Replace header block
    header_pattern = re.compile(r'<!-- Navigation -->\s*<header.*?</header>', re.DOTALL)
    header_replacement = HEADER_TEMPLATE_ROOT.replace('[[PREFIX]]', prefix)
    
    if header_pattern.search(content):
        content = header_pattern.sub(header_replacement, content)
        
    # Replace footer block
    footer_pattern = re.compile(r'<!-- Footer -->\s*<footer.*?</footer\s*>', re.DOTALL)
    # also handle old structure which might not have <!-- Footer -->
    old_footer_pattern = re.compile(r'<footer class="site-footer".*?</footer\s*>', re.DOTALL)
    
    footer_replacement = FOOTER_TEMPLATE_ROOT.replace('[[PREFIX]]', prefix)
    
    if footer_pattern.search(content):
        content = footer_pattern.sub(footer_replacement, content)
    elif old_footer_pattern.search(content):
        content = old_footer_pattern.sub(footer_replacement, content)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

base_dir = r"d:\Toolsathi"

import glob

for filename in glob.glob(os.path.join(base_dir, "*.html")):
    process_file(filename, False)

tool_dir = os.path.join(base_dir, "tools")
for filename in glob.glob(os.path.join(tool_dir, "*.html")):
    process_file(filename, True)

print("Updated HTML layout blocks natively.")
