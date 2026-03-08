# Lecture 3 Demo — Legacy Code is Not a Dead End

**Time:** ~8 minutes | **Tool:** Claude Code

## What This Proves

A COBOL accounting system from 1985 becomes a modern Python web service in minutes. No COBOL expertise required.

## Run the Demo

Open any terminal. Type `claude`. Paste this:

> Find the cio-ai-demos repo on my machine. Inside it, go to foundation/lecture-03-legacy-code and read accounting.cob. This is a COBOL accounting system from 1985 with view balance, credit, and debit operations. Convert it to modern Python in that same folder with:
> 1. A clean Account class with type hints
> 2. All original functionality preserved (balance check, credit, debit, transaction limits, account status enforcement)
> 3. Unit tests in test_accounting.py that verify each operation
> 4. A simple Flask REST API in api.py with endpoints for /balance, /credit, /debit
> Install any packages you need. Run the tests and tell me the results.

## Keep Going — Paste These Next

1. "Add a /transactions endpoint that returns the last 10 transactions for an account"
2. "Add JWT authentication to the API"
3. "Generate Swagger API documentation and open it in my browser"

## CIO Takeaway

> "Code nobody has touched for 40 years just became a modern web service in 5 minutes."
