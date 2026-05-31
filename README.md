# Recipe Idea Generator

A Python console app that turns whatever ingredients you have at home into a
personalised recipe suggestion, powered by Claude AI.

Built as a final project for **Code in Place 2026** by Stanford University.

---

## What It Does

1. You enter the ingredients you have, one at a time
2. You select a dietary preference (none, vegetarian, vegan, or gluten-free)
3. Claude suggests a complete recipe with ingredients and step-by-step instructions

---

## Demo

```
========================================
       RECIPE IDEA GENERATOR
   Powered by Claude (Max Plan)
========================================

Enter your ingredients one at a time.
Press ENTER with no input when you are done.

Ingredient: eggs
Ingredient: spinach
Ingredient: garlic
Ingredient:

--- Your Ingredients ---
  1. eggs
  2. spinach
  3. garlic
------------------------

Select a dietary preference:
  1. no restrictions
  2. vegetarian
  3. vegan
  4. gluten-free

Enter 1, 2, 3 or 4: 2

Asking Claude for a recipe idea...

========================================
           YOUR RECIPE SUGGESTION
========================================
Garlic Spinach Scrambled Eggs

Ingredients:
- 3 eggs
- 2 cups fresh spinach
- 2 cloves garlic, minced
- Salt, pepper, olive oil

Steps:
1. Heat olive oil in a pan over medium heat.
2. Add garlic and cook for 1 minute until fragrant.
3. Add spinach and stir until wilted, about 2 minutes.
4. Whisk eggs, pour into pan, and scramble gently until just set.
5. Season with salt and pepper and serve immediately.
========================================

Try with different ingredients? (yes / no):
```

---

## Python Concepts Used

This project was built using only concepts taught in Code in Place 2026:

| Concept | Where Used |
|---|---|
| Variables | Storing ingredients, preferences, recipe text |
| Lists | Collecting ingredients with `append()` |
| Dictionaries | Storing dietary options and session data |
| While loops | Collecting ingredients until blank input |
| For loops | Displaying ingredients and options |
| Conditionals | Validating input, checking Claude's response |
| Functions | Five separate functions, each doing one job |
| User input | `input()` throughout |
| String operations | `join()`, `strip()`, `lower()`, f-strings |

Claude is integrated via the **Claude Agent SDK**, authenticated through a
Claude Max subscription — no separate API key or billing required.

---

## Requirements

- Python 3.10 or later
- Node.js (to install Claude Code)
- A Claude Pro or Max subscription

---

## Setup (One Time Only)

**1. Install Claude Code**
```bash
sudo npm install -g @anthropic-ai/claude-code
```

**2. Log in with your Claude subscription**
```bash
claude login
```
Select option 1 (Claude account with subscription) and follow the browser prompt.

**3. Install the Agent SDK**
```bash
pip install claude-agent-sdk
```

**4. Clear any existing API key**
```bash
unset ANTHROPIC_API_KEY
```

---

## How to Run

```bash
python3 recipe_generator.py
```

---

## Project Structure

```
recipe-idea-generator/
├── recipe_generator.py    # Main program
└── README.md              # This file
```

---

## How Claude Is Used

The `call_claude()` function sends your ingredient list and dietary preference
as a plain-text prompt to Claude via the Agent SDK. Claude returns a single
recipe suggestion with ingredients and steps. The Agent SDK streams the
response back as a series of messages — the program captures the final result
message and displays it in the terminal.

---

*Code in Place 2026 — Stanford University*
