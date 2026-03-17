# CIO in the AI World — Hands-On Demos

Free, hands-on demo projects for the **[CIO in the AI World](https://www.udemy.com/course/cio-in-the-ai-world/?referralCode=PLACEHOLDER)** Udemy course by Chris France.

Every demo was built entirely with **Claude Code** — no third-party code, no copy-paste from other repos. 100% original.

## Quick Start — One Prompt Installs Everything

1. Get a [Claude Pro or Max subscription](https://claude.ai) ($20/month)
2. Install [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview)
3. Open any terminal, type `claude`, paste this:

```
I'm taking the "CIO in the AI World" Udemy course by Chris France and I need you to set up all the hands-on demos on my machine. Here's what I need:

1. Check if Python 3.10+ is installed. If not, tell me how to install it for my operating system and wait for me to confirm.
2. Check if Node.js 18+ is installed. If not, tell me how to install it for my operating system and wait for me to confirm.
3. Check if git is installed. If not, tell me how to install it and wait for me to confirm.
4. Clone the demo repository: git clone https://github.com/chris-france/cio-ai-demos.git ~/cio-ai-demos
5. Clone the public prototypes repo (includes the Inference Cost Calculator for Lecture 2): git clone https://github.com/chris-france/AI_Public_Prototypes.git ~/AI_Public_Prototypes
6. Set up the demo menu app: create a Python venv in ~/cio-ai-demos/backend/venv, install the backend requirements, install the frontend npm dependencies.
7. Pre-generate sample data for Lecture 4: install openpyxl, run ~/cio-ai-demos/foundation/lecture-04-shadow-it/generate-workbook.py
8. Install Python dependencies for Lecture 5: flask and pytest
9. Make the launcher executable: chmod +x ~/cio-ai-demos/run.sh
10. Launch the demo menu and open it in my browser.

After everything is done, give me a summary of what was installed and confirm all 7 foundation demos are ready.
```

That's it. CC checks your system, installs what's missing, clones the repos, sets up everything, and opens the demo menu at [http://localhost:18802](http://localhost:18802).

## How to Use

1. **Watch the lecture video first** — don't stop to do the demos. Watch me walk through them to understand the concept.
2. **Come back here** — open the demo menu, expand a demo card.
3. **Open any terminal and type `claude`** — that's the only command you will ever type.
4. **Copy & paste the prompt** — Claude Code finds the repo on your machine, navigates to the files, reads them, writes code, installs packages, runs everything. You never leave the conversation.
5. **Keep going** — paste the follow-up prompts to go deeper. If something breaks, tell CC. Don't Google it — CC fixes its own work.

## Foundation Course (Lectures 1-7)

| # | Lecture | Demo | What Happens |
|---|---------|------|--------------|
| 1 | The AI Inflection Point | CSV → chart | CC writes & runs a complete data analysis from one sentence |
| 2 | LLMs Demystified | Ollama model comparison | CC installs Ollama, pulls 2 models, compares speed/quality/cost |
| 3 | Finding Your $250K Moment | [Inference Cost Calculator](https://github.com/chris-france/AI_Public_Prototypes/tree/main/ai-inference-cost-calculator) | CC launches CF's own AI-built cost tool + adds a feature |
| 4 | Legacy Code is Not a Dead End | COBOL → Python | CC converts a 1985 accounting system to a modern web service |
| 5 | The Shadow IT Time Bomb | Excel risk scanner | CC audits a complex spreadsheet and generates a risk report |
| 6 | The Death of Offshore Labor Arbitrage | Sprint ticket | CC implements a feature request in 90 seconds |
| 7 | Renegotiating Your SaaS Stack | SaaS audit tool | CC builds a complete spend analysis dashboard from a CSV |

## Advanced Course (Lectures 8-13) — Coming Soon

Advanced demos add local models (Ollama), UI-based tools, and self-hosted infrastructure.

## About

These demos accompany the **[CIO in the AI World: A Practical Playbook for Modern Technology Leadership](https://www.udemy.com/course/cio-in-the-ai-world/?referralCode=PLACEHOLDER)** course on Udemy.

The course teaches business leaders who just became CIO how to lead technology in the AI era — no deep technical background required.

- **Course:** [Udemy](https://www.udemy.com/course/cio-in-the-ai-world/?referralCode=PLACEHOLDER)
- **Author:** [Chris France](https://chrisfrance.ai)
- **LinkedIn:** [christopherfrance](https://linkedin.com/in/christopherfrance)
- **GitHub:** [chris-france](https://github.com/chris-france)
