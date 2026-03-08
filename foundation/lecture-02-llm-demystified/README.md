# Lecture 2 Demo — LLMs Demystified

**Time:** ~10 minutes | **Tool:** Claude Code + Ollama

## What This Proves

When a vendor says "70 billion parameters," you'll know exactly what that means for your budget, your hardware, and your data security. You'll see the tradeoff between small and large models with your own eyes.

## Run the Demo

Open any terminal. Type `claude`. Paste this:

> I want to understand LLMs hands-on. Here's what I need:
>
> 1. Check if Ollama is installed on my machine. If not, install it.
> 2. Pull two models: a small one (llama3.2:1b — 1 billion parameters) and a medium one (llama3.2:3b — 3 billion parameters).
> 3. Run the exact same prompt on both models: "Explain cloud computing to a CEO in 3 sentences."
> 4. Show me the results side by side — the actual response text, how long each took, and tokens per second.
> 5. Show me how much memory/disk each model uses.
> 6. Now run a harder prompt on both: "Write a 90-day IT modernization plan for a mid-size company. Include milestones, risks, and budget considerations."
> 7. Compare the quality of both responses and explain the tradeoff between model size, speed, cost, and quality in plain CIO language — no data science jargon.

That's it. CC installs Ollama, pulls the models, runs the comparisons, and explains everything.

## What You'll See

- **Small model (1B params):** Fast, cheap to run, fits on any laptop. Good for simple tasks. Struggles with complex reasoning.
- **Medium model (3B params):** Slower, needs more RAM. Noticeably better quality on hard tasks.
- **The tradeoff is real:** Every CIO decision about AI comes down to this — capability vs. cost vs. speed vs. where the data lives.

## Keep Going — Paste These Next

1. "Now pull a larger model like llama3.1:8b and run the same hard prompt. Show me how quality improves with size."
2. "Explain the difference between training and inference. What does each cost? Which one am I paying for when I use Claude or ChatGPT?"
3. "If I wanted to run AI locally so no data leaves my building, what hardware would I need? Give me a budget for small, medium, and enterprise setups."

## Key Vocabulary for CIOs

- **Parameters** — the "knowledge" baked into a model. More = smarter but heavier.
- **Inference** — asking a model a question. This is what you pay for daily.
- **Training** — teaching a model from scratch. Costs millions. You're not doing this.
- **Tokens** — the units models read and write. ~4 characters per token. Pricing is per token.
- **Local vs Cloud** — local means data stays in your building. Cloud means it doesn't.

## CIO Takeaway

> "You don't need to be a data scientist. But you need to know enough to call BS when a vendor says their model is 'enterprise-grade.' After this demo, you can."
