with open('d:/Toolsathi/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

feedback_section = """
    <!-- FEEDBACK SECTION -->
    <section style="padding: 5rem 0; position: relative; z-index: 10;" id="feedback-section">
      <div style="max-width: 72rem; margin: 0 auto; padding: 0 1.5rem;">

        <!-- Testimonials grid (shown after submissions) -->
        <div id="testimonials-wrap" style="margin-bottom: 4rem; display: none;">
          <div style="text-align: center; margin-bottom: 2rem;">
            <span class="badge badge-green" style="display:inline-flex; margin-bottom: 1rem;"><span style="margin-right: 0.375rem;">&#x1F4AC;</span> What Students Say</span>
            <h2 class="font-display font-semibold" style="font-size: clamp(1.5rem,4vw,2.25rem); color: var(--text-primary);">Real <span class="gradient-text-violet italic">Feedback</span></h2>
          </div>
          <div id="testimonials-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem;"></div>
        </div>

        <!-- Feedback Form -->
        <div class="glass-card reveal-hidden" style="border-radius: 1.5rem; padding: 3rem; background: linear-gradient(135deg, rgba(124,58,237,0.06), rgba(16,185,129,0.04)); border: 1px solid rgba(124,58,237,0.15); max-width: 640px; margin: 0 auto; position: relative; overflow: hidden;">
          <div class="ambient-orb" style="width: 200px; height: 200px; background: radial-gradient(circle, rgba(124,58,237,0.12) 0%, transparent 70%); top: -2rem; right: -2rem;"></div>

          <div style="text-align: center; margin-bottom: 2rem; position: relative; z-index: 1;">
            <span class="badge badge-violet" style="display:inline-flex; margin-bottom: 1rem;"><span style="margin-right:0.375rem;">&#x2B50;</span> Share Your Experience</span>
            <h2 class="font-display font-semibold" style="font-size: clamp(1.5rem,4vw,2rem); color: var(--text-primary); margin-bottom: 0.5rem;">Your <span class="gradient-text-mixed italic">Feedback</span> Matters</h2>
            <p style="font-size: 0.9375rem; color: var(--text-secondary); font-weight: 300;">Tell us how Toolsathi helped you &mdash; it takes just 30 seconds! &#x1F680;</p>
          </div>

          <form id="feedback-form" style="display: flex; flex-direction: column; gap: 1.25rem; position: relative; z-index: 1;">
            <div>
              <label style="display:block; font-size:0.875rem; font-weight:600; margin-bottom:0.5rem; color:var(--text-secondary);">Your Name</label>
              <input type="text" id="fb-name" class="tool-input" placeholder="e.g. Rahul Kumar" maxlength="60" required>
            </div>

            <div>
              <label style="display:block; font-size:0.875rem; font-weight:600; margin-bottom:0.625rem; color:var(--text-secondary);">Rating</label>
              <div id="star-rating" style="display:flex; gap:0.5rem;">
                <span class="fb-star" data-val="1" onclick="setRating(1)" style="font-size:2rem; cursor:pointer; transition:transform 0.15s; filter:grayscale(1); user-select:none;">&#x2B50;</span>
                <span class="fb-star" data-val="2" onclick="setRating(2)" style="font-size:2rem; cursor:pointer; transition:transform 0.15s; filter:grayscale(1); user-select:none;">&#x2B50;</span>
                <span class="fb-star" data-val="3" onclick="setRating(3)" style="font-size:2rem; cursor:pointer; transition:transform 0.15s; filter:grayscale(1); user-select:none;">&#x2B50;</span>
                <span class="fb-star" data-val="4" onclick="setRating(4)" style="font-size:2rem; cursor:pointer; transition:transform 0.15s; filter:grayscale(1); user-select:none;">&#x2B50;</span>
                <span class="fb-star" data-val="5" onclick="setRating(5)" style="font-size:2rem; cursor:pointer; transition:transform 0.15s; filter:grayscale(1); user-select:none;">&#x2B50;</span>
              </div>
              <input type="hidden" id="fb-rating" value="0">
            </div>

            <div>
              <label style="display:block; font-size:0.875rem; font-weight:600; margin-bottom:0.5rem; color:var(--text-secondary);">Your Message</label>
              <textarea id="fb-message" class="tool-input" placeholder="What did you like? Which tool helped you the most?" rows="4" maxlength="300" required style="resize:vertical;" oninput="document.getElementById('fb-charcount').textContent=this.value.length"></textarea>
              <div style="text-align:right; font-size:0.75rem; color:var(--text-muted); margin-top:0.25rem;"><span id="fb-charcount">0</span>/300</div>
            </div>

            <div>
              <label style="display:block; font-size:0.875rem; font-weight:600; margin-bottom:0.5rem; color:var(--text-secondary);">Tool Used <span style="font-weight:400; opacity:0.6;">(Optional)</span></label>
              <select id="fb-tool" class="tool-input" style="cursor:pointer;">
                <option value="">-- Select a tool --</option>
                <option value="CGPA Calculator">&#x1F393; CGPA Calculator</option>
                <option value="EMI Calculator">&#x1F4B0; EMI Calculator</option>
                <option value="Age Calculator">&#x1F382; Age Calculator</option>
                <option value="BMI Calculator">&#x2696;&#xFE0F; BMI Calculator</option>
                <option value="Percentage Calculator">&#x1F4CA; Percentage Calculator</option>
                <option value="Discount Calculator">&#x1F3F7;&#xFE0F; Discount Calculator</option>
                <option value="AI Tools">&#x26A1; AI Tools</option>
                <option value="All Tools">&#x1F31F; All Tools</option>
              </select>
            </div>

            <div id="fb-error" style="display:none; padding:0.75rem; border-radius:0.75rem; font-size:0.875rem; background:rgba(239,68,68,0.1); border:1px solid rgba(239,68,68,0.2); color:#F87171;"></div>
            <div id="fb-success" style="display:none; padding:0.75rem; border-radius:0.75rem; font-size:0.875rem; background:rgba(16,185,129,0.1); border:1px solid rgba(16,185,129,0.2); color:#34D399; text-align:center;"></div>

            <button type="submit" class="btn-primary" style="width:100%;">Submit Feedback &#x2728;</button>
          </form>
        </div>
      </div>
    </section>

"""

# Insert before </main>
content = content.replace('  </main>', feedback_section + '  </main>', 1)

with open('d:/Toolsathi/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done!')
