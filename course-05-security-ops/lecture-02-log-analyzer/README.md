# Lecture 2 Demo — AI Threat Detection

**Time:** ~8 minutes | **Tool:** Claude Code

## What This Proves

AI can analyze 1,000 log entries from multiple sources (firewall, authentication, application) in seconds, classify each as normal/suspicious/malicious, and identify the 3 actual threats hiding in the noise — something a human analyst would need hours to accomplish.

## Run the Demo

Open any terminal. Type `claude`. Paste this:

> Find the cio-ai-demos repo on my machine. Inside it, go to course-05-security-ops/lecture-02-log-analyzer. Build an AI Log Analyzer that processes 1,000 simulated log entries from firewall, auth, and application logs. Classify each entry as normal, suspicious, or malicious. Identify distinct threat patterns. Create index.html with a streaming log display, threat timeline chart, and detailed threat cards for each identified attack. Open in browser.

## Keep Going — Paste These Next

1. "Correlate the brute force and lateral movement events — could they be the same attacker?"
2. "Generate SIEM alert rules (Wazuh or Splunk format) for each threat pattern detected"
3. "Create a threat intelligence report linking the source IPs to known threat actors"

## CIO Takeaway

> "Your logs already contain the evidence of the breach happening right now. AI reads what nobody has time to read — and finds the 3 events that matter in a million lines of noise."
