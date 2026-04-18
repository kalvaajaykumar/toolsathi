
# 1. Add feedback JS to index.html
feedback_js = """
  <script>
    // ── Feedback System ──────────────────────────────────────
    let fbRating = 0;

    function setRating(val) {
      fbRating = val;
      document.getElementById('fb-rating').value = val;
      document.querySelectorAll('.fb-star').forEach(s => {
        const sv = parseInt(s.getAttribute('data-val'));
        s.style.filter = sv <= val ? 'grayscale(0)' : 'grayscale(1)';
        s.style.transform = sv <= val ? 'scale(1.15)' : 'scale(1)';
      });
    }

    function renderTestimonials() {
      const feedbacks = JSON.parse(localStorage.getItem('ts-feedback') || '[]');
      const approved = feedbacks.filter(f => f.approved !== false);
      const wrap = document.getElementById('testimonials-wrap');
      const grid = document.getElementById('testimonials-grid');
      if (!approved.length) { wrap.style.display = 'none'; return; }
      wrap.style.display = 'block';
      grid.innerHTML = approved.slice(-6).reverse().map(f => {
        const stars = '⭐'.repeat(f.rating || 5);
        return `<div class="glass-card" style="border-radius:1rem; padding:1.5rem;">
          <div style="font-size:1.25rem; margin-bottom:0.5rem;">${stars}</div>
          <p style="font-size:0.9rem; color:var(--text-secondary); line-height:1.6; margin-bottom:1rem;">"${f.message}"</p>
          <div style="display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:0.5rem;">
            <span style="font-weight:700; font-size:0.875rem; color:var(--text-primary);">${f.name}</span>
            ${f.tool ? `<span class="badge badge-violet" style="font-size:0.65rem;">${f.tool}</span>` : ''}
          </div>
        </div>`;
      }).join('');
    }

    document.getElementById('feedback-form').addEventListener('submit', function(e) {
      e.preventDefault();
      const name = document.getElementById('fb-name').value.trim();
      const rating = parseInt(document.getElementById('fb-rating').value);
      const message = document.getElementById('fb-message').value.trim();
      const tool = document.getElementById('fb-tool').value;
      const errBox = document.getElementById('fb-error');
      const sucBox = document.getElementById('fb-success');

      errBox.style.display = 'none';
      if (!rating) { errBox.textContent = '⚠️ Please select a star rating!'; errBox.style.display = 'block'; return; }
      if (message.length < 10) { errBox.textContent = '⚠️ Please write at least 10 characters in your message.'; errBox.style.display = 'block'; return; }

      const feedbacks = JSON.parse(localStorage.getItem('ts-feedback') || '[]');
      feedbacks.push({ id: Date.now(), name, rating, message, tool, date: new Date().toLocaleDateString('en-IN'), approved: true });
      localStorage.setItem('ts-feedback', JSON.stringify(feedbacks));

      sucBox.textContent = '🎉 Thank you, ' + name + '! Your feedback has been submitted successfully.';
      sucBox.style.display = 'block';
      this.reset();
      fbRating = 0;
      document.querySelectorAll('.fb-star').forEach(s => { s.style.filter = 'grayscale(1)'; s.style.transform = 'scale(1)'; });
      document.getElementById('fb-charcount').textContent = '0';

      setTimeout(() => { sucBox.style.display = 'none'; }, 4000);
      renderTestimonials();
    });

    // Load testimonials on page load
    renderTestimonials();
  </script>
"""

with open('d:/Toolsathi/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Insert before closing </body>
content = content.replace('</body>', feedback_js + '</body>', 1)

with open('d:/Toolsathi/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('index.html feedback JS added!')

# 2. Add Feedback nav item to admin sidebar
with open('d:/Toolsathi/admin.html', 'r', encoding='utf-8') as f:
    admin = f.read()

# Add nav item after password nav
admin = admin.replace(
    '<button class="nav-item" data-sec="password">\n      <span class="icon">\U0001f510</span> Password\n    </button>',
    '<button class="nav-item" data-sec="password">\n      <span class="icon">\U0001f510</span> Password\n    </button>\n    <button class="nav-item" data-sec="feedback">\n      <span class="icon">\U0001f4ac</span> Feedback\n    </button>'
)

# Add feedback section before closing </div> of content area
feedback_admin_section = """
    <!-- ─── FEEDBACK ─── -->
    <div id="sec-feedback" class="section">
      <div class="section-head">
        <div>
          <h2>User Feedback 💬</h2>
          <p class="text-muted" style="font-size:0.8rem;">Feedback submitted by users from the homepage</p>
        </div>
        <button class="btn btn-danger btn-sm" onclick="clearAllFeedback()">Clear All</button>
      </div>

      <div id="feedback-stats" style="display:grid; grid-template-columns:repeat(auto-fit,minmax(130px,1fr)); gap:1rem; margin-bottom:1.5rem;"></div>
      <div id="feedback-list"></div>
    </div>

"""

# Find the last section closing and insert before the closing of content div
admin = admin.replace('  </div><!-- /content -->', feedback_admin_section + '  </div><!-- /content -->', 1)

# Add feedback JS to admin
feedback_admin_js = """
  // ── Feedback Admin ──────────────────────────────────────────
  function loadFeedback() {
    const feedbacks = JSON.parse(localStorage.getItem('ts-feedback') || '[]');
    const list = document.getElementById('feedback-list');
    const stats = document.getElementById('feedback-stats');
    if (!list) return;

    // Stats
    const total = feedbacks.length;
    const avg = total ? (feedbacks.reduce((s,f) => s + (f.rating||5), 0) / total).toFixed(1) : 0;
    const approved = feedbacks.filter(f => f.approved !== false).length;
    stats.innerHTML = [
      { emoji: '💬', val: total, label: 'Total', color: 'var(--violet-light)' },
      { emoji: '⭐', val: avg, label: 'Avg Rating', color: 'var(--gold)' },
      { emoji: '✅', val: approved, label: 'Approved', color: 'var(--green)' },
    ].map(s => `<div class="stat"><div class="stat-emoji">${s.emoji}</div><div class="stat-value" style="color:${s.color};">${s.val}</div><div class="stat-label">${s.label}</div></div>`).join('');

    if (!feedbacks.length) {
      list.innerHTML = '<p class="text-muted" style="font-size:0.85rem;">No feedback yet. Share the website with students!</p>';
      return;
    }

    list.innerHTML = [...feedbacks].reverse().map((f, i) => {
      const stars = '⭐'.repeat(f.rating || 5) + '☆'.repeat(5 - (f.rating || 5));
      const ri = feedbacks.length - 1 - i;
      return `<div class="card" style="margin-bottom:0.75rem;">
        <div style="display:flex; align-items:flex-start; justify-content:space-between; gap:1rem; flex-wrap:wrap;">
          <div style="flex:1; min-width:0;">
            <div style="display:flex; align-items:center; gap:0.75rem; flex-wrap:wrap; margin-bottom:0.5rem;">
              <strong style="font-size:0.9rem;">${f.name}</strong>
              <span style="font-size:0.875rem;">${stars}</span>
              ${f.tool ? `<span class="badge badge-violet" style="font-size:0.65rem;">${f.tool}</span>` : ''}
              ${f.approved === false ? '<span class="badge badge-red" style="font-size:0.65rem;">Hidden</span>' : '<span class="badge badge-green" style="font-size:0.65rem;">Visible</span>'}
            </div>
            <p style="font-size:0.85rem; color:var(--t2); line-height:1.6; margin-bottom:0.375rem;">"${f.message}"</p>
            <span style="font-size:0.72rem; color:var(--t3);">${f.date || ''}</span>
          </div>
          <div style="display:flex; gap:0.5rem; flex-shrink:0;">
            <button class="btn btn-xs btn-ghost" onclick="toggleFeedbackApproval(${ri})">${f.approved === false ? '✅ Show' : '🙈 Hide'}</button>
            <button class="btn btn-xs btn-danger" onclick="deleteFeedback(${ri})">🗑️</button>
          </div>
        </div>
      </div>`;
    }).join('');
  }

  function toggleFeedbackApproval(idx) {
    const feedbacks = JSON.parse(localStorage.getItem('ts-feedback') || '[]');
    feedbacks[idx].approved = feedbacks[idx].approved === false ? true : false;
    localStorage.setItem('ts-feedback', JSON.stringify(feedbacks));
    loadFeedback();
    logActivity('Feedback visibility toggled');
  }

  function deleteFeedback(idx) {
    const feedbacks = JSON.parse(localStorage.getItem('ts-feedback') || '[]');
    feedbacks.splice(idx, 1);
    localStorage.setItem('ts-feedback', JSON.stringify(feedbacks));
    loadFeedback();
    logActivity('Feedback deleted');
  }

  function clearAllFeedback() {
    if (!confirm('Clear ALL feedback? This cannot be undone.')) return;
    localStorage.removeItem('ts-feedback');
    loadFeedback();
    logActivity('All feedback cleared');
  }
"""

# Find the showSection function and add loadFeedback call
admin = admin.replace(
    "if (s === 'blog') loadPosts();",
    "if (s === 'blog') loadPosts();\n    if (s === 'feedback') loadFeedback();"
)

# Insert JS before closing </script> of main admin script block
# Find last occurrence of closing script
admin = admin.replace('  // ── end ──', feedback_admin_js + '\n  // ── end ──', 1)

with open('d:/Toolsathi/admin.html', 'w', encoding='utf-8') as f:
    f.write(admin)
print('admin.html Feedback tab added!')
