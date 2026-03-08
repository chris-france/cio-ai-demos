import { useState } from 'react'
import { Rocket, Copy, Check, ChevronDown, ChevronUp } from 'lucide-react'

const SETUP_PROMPT = `I'm taking the "CIO in the AI World" Udemy course by Chris France and I need you to set up all the hands-on demos on my machine. Here's what I need:

1. Check if Python 3.10+ is installed. If not, tell me how to install it for my operating system and wait for me to confirm.

2. Check if Node.js 18+ is installed. If not, tell me how to install it for my operating system and wait for me to confirm.

3. Check if git is installed. If not, tell me how to install it and wait for me to confirm.

4. Clone the demo repository into my home directory:
   git clone https://github.com/chris-france/cio-ai-demos.git ~/cio-ai-demos

5. Clone the full public prototypes repo (includes the Inference Cost Calculator for Lecture 2):
   git clone https://github.com/chris-france/AI_Public_Prototypes.git ~/AI_Public_Prototypes

6. Set up the demo menu app:
   - Create a Python virtual environment in ~/cio-ai-demos/backend/venv
   - Install the backend requirements (fastapi, uvicorn)
   - Install the frontend npm dependencies in ~/cio-ai-demos/frontend/

7. Pre-generate the sample data for Lecture 4 (Shadow IT demo):
   - Install openpyxl in the backend venv
   - Run ~/cio-ai-demos/foundation/lecture-04-shadow-it/generate-workbook.py

8. Install the Python dependencies for Lecture 5 (Offshore demo):
   - Install flask and pytest in the backend venv

9. Make the demo launcher executable:
   - chmod +x ~/cio-ai-demos/run.sh

10. Launch the demo menu and open it in my browser.

After everything is done, give me a summary of what was installed and confirm all 7 foundation demos are ready.`

export default function SetupCard() {
  const [expanded, setExpanded] = useState(false)
  const [copied, setCopied] = useState(false)

  const copyPrompt = async (e) => {
    e.stopPropagation()
    await navigator.clipboard.writeText(SETUP_PROMPT)
    setCopied(true)
    setTimeout(() => setCopied(false), 2000)
  }

  return (
    <div className="bg-gradient-to-r from-green-50 to-emerald-50 border-2 border-green-300 rounded-xl mb-8 shadow-sm">
      <div
        className="p-5 cursor-pointer"
        onClick={() => setExpanded(!expanded)}
      >
        <div className="flex items-start justify-between gap-3">
          <div className="flex items-center gap-3">
            <div className="bg-green-600 text-white p-2 rounded-lg">
              <Rocket size={20} />
            </div>
            <div>
              <h2 className="text-base font-bold text-green-900">First Time? One Prompt Sets Up Everything</h2>
              <p className="text-sm text-green-700 mt-0.5">
                Open a terminal, type <code className="bg-green-100 px-1.5 py-0.5 rounded font-mono text-green-900 text-xs">claude</code>, paste one prompt. CC clones the repo, installs all dependencies, and launches the demo menu.
              </p>
            </div>
          </div>
          <button className="text-green-600 hover:text-green-800 shrink-0 mt-1">
            {expanded ? <ChevronUp size={20} /> : <ChevronDown size={20} />}
          </button>
        </div>
      </div>

      {expanded && (
        <div className="border-t border-green-200 px-5 pb-5">
          <div className="mt-4">
            <h3 className="text-xs font-bold text-green-800 uppercase tracking-wide mb-1">Before You Start</h3>
            <p className="text-sm text-green-700">
              You need a <strong>Claude Pro or Max subscription</strong> ($20/month) with Claude Code installed.
              If you haven't done that yet, go to{' '}
              <a href="https://docs.anthropic.com/en/docs/claude-code/overview" target="_blank" rel="noopener noreferrer" className="underline font-medium">
                docs.anthropic.com/en/docs/claude-code
              </a>{' '}
              and follow the install instructions first.
            </p>
          </div>

          <div className="mt-4">
            <div className="flex items-center justify-between mb-2">
              <h3 className="text-xs font-bold text-green-800 uppercase tracking-wide">The Master Setup Prompt</h3>
              <button
                onClick={copyPrompt}
                className="flex items-center gap-1 text-xs text-green-600 hover:text-green-800 transition-colors"
              >
                {copied ? <Check size={12} /> : <Copy size={12} />}
                {copied ? 'Copied!' : 'Copy'}
              </button>
            </div>
            <div className="bg-gray-900 text-green-400 rounded-lg p-4 text-sm font-mono leading-relaxed whitespace-pre-wrap max-h-80 overflow-y-auto">
              {SETUP_PROMPT}
            </div>
          </div>

          <div className="mt-4 bg-green-100 rounded-lg p-3">
            <h3 className="text-xs font-bold text-green-800 uppercase tracking-wide mb-1">What CC Will Do</h3>
            <ul className="text-sm text-green-700 space-y-1">
              <li>- Check Python, Node.js, and git are installed (helps you install if not)</li>
              <li>- Clone the demo repo and the public prototypes repo</li>
              <li>- Install all Python and Node.js dependencies</li>
              <li>- Pre-generate sample data files</li>
              <li>- Launch the demo menu at <strong>localhost:8802</strong></li>
              <li>- Report a summary when done</li>
            </ul>
          </div>

          <p className="mt-3 text-xs text-green-600 italic">
            This takes 2-3 minutes depending on your internet speed. You only do this once.
          </p>
        </div>
      )}
    </div>
  )
}
