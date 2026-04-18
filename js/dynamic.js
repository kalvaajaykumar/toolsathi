/**
 * Toolsathi Dynamic Tool Engine
 * Handles AI Tools, Prompt Generation, and Content Injection
 */

document.addEventListener('DOMContentLoaded', async () => {
    const urlParams = new URLSearchParams(window.location.search);
    const toolId = urlParams.get('id');
    const toolContent = document.getElementById('tool-content');

    if (!toolId) {
        window.location.href = 'index.html';
        return;
    }

    try {
        // Fetch All Tools
        const response = await fetch('data/tools.json?v=' + Date.now());
        const jsonTools = await response.json();
        const customTools = JSON.parse(localStorage.getItem('ts-custom-tools') || '[]');
        const deletedIds = JSON.parse(localStorage.getItem('ts-deleted-tools') || '[]');
        
        // Merge and Filter (to respect admin deletions/hides)
        const allTools = [...jsonTools.filter(t => !deletedIds.includes(t.id)), ...customTools];
        const tool = allTools.find(t => t.id === toolId);

        if (!tool) {
            showError("Tool Not Found", "This dynamic tool does not exist or has been removed.");
            return;
        }

        // Set SEO Title
        document.title = `${tool.name} — Toolsathi AI`;

        // Fill UI Header
        document.getElementById('tool-name').textContent = tool.name;
        document.getElementById('tool-icon').textContent = tool.icon;
        document.getElementById('tool-tag').textContent = tool.tag;
        document.getElementById('tool-desc').textContent = tool.description;
        
        if (tool.color) {
            document.getElementById('tool-tag').style.color = tool.color;
            document.getElementById('tool-icon').style.background = `${tool.color}15`;
        }

        // Build Input Fields
        const container = document.getElementById('inputs-container');
        if (tool.inputs && tool.inputs.length > 0) {
            tool.inputs.forEach(input => {
                const group = document.createElement('div');
                group.className = 'input-group';
                
                const label = document.createElement('label');
                label.textContent = input.label;
                group.appendChild(label);

                let field;
                if (input.type === 'textarea') {
                    field = document.createElement('textarea');
                } else {
                    field = document.createElement('input');
                    field.type = input.type || 'text';
                }
                field.className = 'input-field';
                field.placeholder = input.placeholder;
                field.id = `input-${input.id}`;
                group.appendChild(field);
                
                container.appendChild(group);
            });
        }

        // Action Logic: Generate Result or Prompt
        const generateBtn = document.getElementById('generate-btn');
        const resultArea = document.getElementById('result-area');
        const output = document.getElementById('prompt-output');
        const resultHeader = document.querySelector('#result-area h2');
        const tipText = document.querySelector('#result-area p.text-muted');

        if (tool.isDirect) {
            generateBtn.innerHTML = 'Generate Result ⚡';
            if (resultHeader) resultHeader.textContent = 'Generated Result';
            if (tipText) tipText.innerHTML = '✅ This is your final result. You can copy it directly! 🚀';
        }

        generateBtn.addEventListener('click', () => {
            let finalOutput = "";

            if (tool.isDirect) {
                // RUN DIRECT LOGIC
                const vals = {};
                (tool.inputs || []).forEach(input => {
                    const el = document.getElementById(`input-${input.id}`);
                    vals[input.id] = el ? el.value.trim() : '';
                });

                if (tool.id === 'ytt') {
                    const templates = [
                        `How to Master ${vals.topic || 'Topic'} for ${vals.audience || 'Audience'} (Step-by-Step)`,
                        `5 Secret ${vals.topic || 'Topic'} Tips Every ${vals.audience || 'Audience'} Must Know!`,
                        `${vals.topic || 'Topic'} Explained for ${vals.audience || 'Audience'} in 10 Minutes`,
                        `Why Most ${vals.audience || 'Audience'} Fail at ${vals.topic || 'Topic'} (and How to Fix It)`,
                        `The Ultimate ${vals.topic || 'Topic'} Guide for ${vals.audience || 'Audience'} in 2024`,
                        `Best way to learn ${vals.topic || 'Topic'} for ${vals.audience || 'Audience'}`
                    ];
                    finalOutput = templates.sort(() => 0.5 - Math.random()).slice(0, 5).map((t, i) => `${i+1}. ${t}`).join('\n');
                } 
                else if (tool.id === 'res') {
                    const name = vals.name || 'Name';
                    const degree = vals.degree || 'B.Tech';
                    const skills = vals.skills || 'Python, Java';
                    const goal = vals.goal || 'Software Developer';
                    const summaries = [
                        `Highly motivated ${degree} graduate with core expertise in ${skills}. Passionate about leveraging my technical foundation to excel as a ${goal} in a high-growth environment.`,
                        `Aspiring ${goal} with a strong background in ${degree}. Proficient in ${skills}, with a dedicated focus on building scalable solutions and impactful experiences.`
                    ];
                    finalOutput = summaries[Math.floor(Math.random() * summaries.length)];
                }
                else if (tool.id === 'study') {
                    const days = parseInt(vals.days) || 30;
                    finalOutput = `📅 ${days}-Day Study Plan for ${vals.subject || 'Subject'} (${vals.level || 'Beginner'})\n──────────────────────────────\n`;
                    const weeks = Math.ceil(days / 7);
                    for (let w = 1; w <= weeks; w++) {
                        finalOutput += `Week ${w}: ${w === 1 ? 'Foundations' : w === weeks ? 'Final Revision' : 'Main Content'}\n`;
                    }
                    finalOutput += `\nDaily Commitment: 3-5 Hours.`;
                }
            } else {
                // DEFAULT PROMPT GENERATION
                let prompt = tool.promptTemplate || tool.prompt;
                if (!prompt) {
                    alert("No prompt template defined for this tool.");
                    return;
                }
                (tool.inputs || []).forEach(input => {
                    const el = document.getElementById(`input-${input.id}`);
                    const val = el ? el.value.trim() : '';
                    const regex = new RegExp(`\\{${input.id}\\}`, 'gi');
                    prompt = prompt.replace(regex, val || `[${input.label}]`);
                });
                finalOutput = prompt;
            }

            // Display Result
            output.textContent = finalOutput;
            resultArea.style.display = 'block';
            resultArea.scrollIntoView({ behavior: 'smooth', block: 'center' });
            
            // Log analytics
            const an = JSON.parse(localStorage.getItem('ts-analytics') || '{}');
            an.calcs = (an.calcs || 0) + 1;
            localStorage.setItem('ts-analytics', JSON.stringify(an));
        });

        // Copy Feature
        document.getElementById('copy-btn').addEventListener('click', function() {
            navigator.clipboard.writeText(output.textContent);
            const originalHTML = this.innerHTML;
            this.textContent = "✅ Copied!";
            setTimeout(() => { this.innerHTML = originalHTML; }, 2000);
        });

        // Reveal page
        toolContent.classList.add('revealed');

    } catch (error) {
        console.error("Engine Error:", error);
        showError("Loading Error", "Something went wrong while preparing the tool logic.");
    }
});

function showError(title, msg) {
    document.getElementById('tool-name').textContent = title;
    document.getElementById('tool-desc').textContent = msg;
    document.getElementById('inputs-container').innerHTML = '';
    document.getElementById('generate-btn').style.display = 'none';
}
