import { Terminal } from 'lucide-react'

export default function Header() {
  return (
    <header>
      <div className="bg-gradient-to-r from-france-blue to-france-cyan text-white">
        <div className="max-w-6xl mx-auto px-6 py-3 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <Terminal className="w-7 h-7" />
            <div>
              <h1 className="text-lg font-bold leading-tight">CIO AI Demos</h1>
              <p className="text-white/80 text-xs">Hands-On Lab Menu</p>
            </div>
          </div>
          <span className="text-white/60 text-xs font-mono">:18802</span>
        </div>
      </div>
      <div className="bg-france-blue-dark/90 text-white/70 text-xs px-6 py-1 flex justify-between max-w-full">
        <span>Chris France</span>
        <span>CIO in the AI World — Udemy Course</span>
      </div>
    </header>
  )
}
