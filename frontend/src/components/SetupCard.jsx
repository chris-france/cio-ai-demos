import { useState } from 'react'
import { Rocket, Copy, Check, ChevronDown, ChevronUp } from 'lucide-react'

const SETUP_PROMPT = `I'm taking the "CIO in the AI World" Udemy course by Chris France and I need you to set up all the hands-on demos on my machine. Do everything automatically — install whatever is missing, don't stop to ask me.

IMPORTANT: If any install command fails due to permissions (no admin/sudo access), fall back to user-profile installs instead. Everything can be installed without admin access.

Here's what I need:

1. Check if Python 3.10+ is installed. If not, install it:
   - Mac: use Homebrew (install Homebrew first if needed). If no admin, download the installer from python.org
   - Windows: use winget (winget install Python.Python.3.12). If no admin, download from python.org and install for current user only
   - Linux: use apt/dnf. If no sudo, install pyenv into ~/.pyenv and use it to install Python

2. Check if Node.js 18+ is installed. If not, install it:
   - Mac: use Homebrew (brew install node). If no admin, install nvm into ~/.nvm and use it to install Node
   - Windows: use winget (winget install OpenJS.NodeJS.LTS). If no admin, install nvm-windows into the user profile
   - Linux: use apt/dnf. If no sudo, install nvm into ~/.nvm and use it to install Node

3. Check if git is installed. If not, install it:
   - Mac: use Homebrew (brew install git) or run xcode-select --install
   - Windows: use winget (winget install Git.Git). If no admin, download Git portable from git-scm.com
   - Linux: use apt/dnf. If no sudo, download a portable git binary

4. Clone the demo repository into my home directory:
   - git clone https://github.com/chris-france/cio-ai-demos.git ~/cio-ai-demos

5. Clone the full public prototypes repo (includes the Inference Cost Calculator for Lecture 2):
   - git clone https://github.com/chris-france/AI_Public_Prototypes.git ~/AI_Public_Prototypes

6. Set up the demo menu app:
   - Create a Python virtual environment in ~/cio-ai-demos/backend/venv
   - Install the backend requirements (fastapi, uvicorn)
   - Install the frontend npm dependencies in ~/cio-ai-demos/frontend/

7. Pre-generate the sample data for Lecture 4 (Shadow IT demo):
   - Install openpyxl in the backend venv
   - Run ~/cio-ai-demos/foundation/lecture-04-shadow-it/generate-workbook.py

8. Install the Python dependencies for Lecture 5 (Offshore demo):
   - Install flask and pytest in the backend venv

9. Make the demo launcher executable and create a global "ciodemos" command:
   - chmod +x ~/cio-ai-demos/run.sh
   - On Mac/Linux: create ~/.local/bin/ if it doesn't exist, then ln -sf ~/cio-ai-demos/run.sh ~/.local/bin/ciodemos. Make sure ~/.local/bin is in the user's PATH (add to ~/.zshrc or ~/.bashrc if needed)
   - On Windows: create a ciodemos.cmd batch file in %USERPROFILE%\\.local\\bin\\ and add that to the user's PATH if needed

10. Launch the demo menu and open it in my browser.

After everything is done, give me a summary of what was installed and confirm all 7 foundation demos are ready. Remind the user they can now type "ciodemos" from any terminal to launch the demos in the future.`

const MAC_INSTALL = 'curl -fsSL https://claude.ai/install.sh | bash'
const WIN_INSTALL = 'irm https://claude.ai/install.ps1 | iex'

function CopyButton({ text }) {
  const [copied, setCopied] = useState(false)
  const handleCopy = async (e) => {
    e.stopPropagation()
    await navigator.clipboard.writeText(text)
    setCopied(true)
    setTimeout(() => setCopied(false), 2000)
  }
  return (
    <button
      onClick={handleCopy}
      className="flex items-center gap-1 text-xs text-green-600 hover:text-green-800 transition-colors shrink-0"
    >
      {copied ? <Check size={12} /> : <Copy size={12} />}
      {copied ? 'Copied!' : 'Copy'}
    </button>
  )
}

function Step({ number, title, children }) {
  return (
    <div className="mt-4 flex gap-3">
      <div className="flex-shrink-0 w-7 h-7 rounded-full bg-green-600 text-white flex items-center justify-center text-sm font-bold">{number}</div>
      <div className="flex-1 min-w-0">
        <h3 className="text-sm font-bold text-green-900">{title}</h3>
        {children}
      </div>
    </div>
  )
}

function CommandBlock({ command, label }) {
  return (
    <div className="mt-1">
      {label && <p className="text-xs text-green-600 mb-0.5">{label}</p>}
      <div className="flex items-center gap-2 bg-gray-900 rounded-lg px-3 py-2">
        <code className="text-green-400 text-sm font-mono flex-1 min-w-0 break-all">{command}</code>
        <CopyButton text={command} />
      </div>
    </div>
  )
}

export default function SetupCard() {
  const [expanded, setExpanded] = useState(false)

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
              <h2 className="text-base font-bold text-green-900">First Time? Set Up Everything in 4 Steps</h2>
              <p className="text-sm text-green-700 mt-0.5">
                Subscribe, install one thing, then paste one prompt. Takes about 5 minutes.
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

          <Step number={1} title="Get a Claude Pro or Max subscription">
            <p className="text-sm text-green-700 mt-0.5">
              Go to{' '}
              <a href="https://claude.ai" target="_blank" rel="noopener noreferrer" className="underline font-medium">claude.ai</a>,
              {' '}create an account, and subscribe to Pro ($20/month) or Max.
            </p>
          </Step>

          <Step number={2} title="Install Claude Code">
            <p className="text-sm text-green-700 mt-0.5">
              Open <strong>Terminal</strong> (Mac/Linux) or <strong>PowerShell</strong> (Windows) and copy-paste the command for your system:
            </p>
            <CommandBlock command={MAC_INSTALL} label="Mac / Linux:" />
            <CommandBlock command={WIN_INSTALL} label="Windows PowerShell:" />
          </Step>

          <Step number={3} title="Launch Claude Code">
            <p className="text-sm text-green-700 mt-0.5">
              In the same terminal, type:
            </p>
            <CommandBlock command="claude" />
            <p className="text-xs text-green-600 mt-1">
              First time? It will open your browser to log in with your Anthropic account. Follow the prompts, then come back to the terminal.
            </p>
            <p className="text-xs mt-1.5 bg-yellow-50 border border-yellow-200 text-yellow-800 rounded px-2 py-1">
              Do NOT paste the prompt into claude.ai (the website). Claude Code runs in your terminal — that's where you paste it.
            </p>
          </Step>

          <Step number={4} title="Paste the setup prompt into Claude Code">
            <p className="text-sm text-green-700 mt-0.5">
              Copy the prompt below and paste it into the Claude Code terminal. Hit Enter and let it run.
            </p>
            <div className="mt-2">
              <div className="flex items-center justify-end mb-1">
                <CopyButton text={SETUP_PROMPT} />
              </div>
              <div className="bg-gray-900 text-green-400 rounded-lg p-4 text-sm font-mono leading-relaxed whitespace-pre-wrap max-h-80 overflow-y-auto">
                {SETUP_PROMPT}
              </div>
            </div>
          </Step>

          <div className="mt-4 bg-green-100 rounded-lg p-3">
            <h3 className="text-xs font-bold text-green-800 uppercase tracking-wide mb-1">What happens next</h3>
            <ul className="text-sm text-green-700 space-y-1">
              <li>- Claude Code checks your system and installs anything missing (Python, Node.js, git)</li>
              <li>- It clones the demo repo and all dependencies</li>
              <li>- It pre-generates sample data files</li>
              <li>- It creates a global <code className="bg-green-200 px-1 rounded font-mono text-xs">ciodemos</code> command you can use anytime</li>
              <li>- It launches the demo menu at <strong>localhost:18802</strong></li>
              <li>- It will ask your permission before running commands — just approve them</li>
            </ul>
          </div>

          <p className="mt-3 text-xs text-green-600 italic">
            You only do this once. After setup, just type <code className="bg-green-100 px-1 rounded font-mono">ciodemos</code> in any terminal to launch the demos.
          </p>
        </div>
      )}
    </div>
  )
}
