# Guide: Adding New Tools with JSON

Welcome to your new **Dynamic AI Tool Builder**! You can now expand your website with hundreds of new tools without writing any HTML or CSS.

## 🚀 How to Add a New Tool (Step-by-Step)

### 1. Open the Data File
Go to the folder `data/` and open the file named `tools.json`.

### 2. Add a New Tool Object
Paste a new tool entry at the end of the JSON array. Follow this template:

```json
{
  "id": "my-new-tool",
  "icon": "⚡",
  "name": "Quick Fact Checker",
  "description": "Checks any fact using AI prompt logic.",
  "tag": "Verification",
  "color": "#10B981",
  "isStatic": false,
  "inputs": [
    { "id": "claim", "label": "The Claim", "placeholder": "Enter a fact here..." }
  ],
  "promptTemplate": "Decide if this claim is likely true or false and explain why: {claim}"
}
```

### 3. Save and Refresh
Save the file. Your new tool will **automatically** appear on:
- The **Homepage** as a premium card.
- The **Admin Panel** in the Tools Management tab.

---

## 🛠️ How the System Works

1.  **Data Storage**: Everything starts in `data/tools.json`. This file acts as the "Brain" of the site.
2.  **Homepage Loader**: When a student visits the homepage, a script fetches `tools.json`, reads all the tools, and builds the cards on the fly.
3.  **The Universal Viewer**: When a tool is clicked, it opens `dynamic-tool.html?id=ytt`. This page is a master template. It reads the `id` from the URL, finds the tool in your JSON, and builds the exact input boxes you defined.
4.  **Instant Logic**: When the "Generate" button is clicked, the script takes the user's input and "plugs" it into your `promptTemplate` by replacing the `{placeholder}` text.
5.  **Admin Integration**: Your Admin Dashboard is now also dynamic! It reads the same JSON file, allowing you to turn these newly added tools ON or OFF with a single toggle.

---

## 💡 Pro Tips
- **Colors**: Use Hex codes like `#A78BFA` to match your site's purple theme.
- **Input Types**: You can use `"type": "textarea"` for large text boxes or leave it out for a standard single-line box.
- **Placeholders**: Ensure your `{topic}` in the `promptTemplate` exactly matches the `id` in your `inputs` list.
