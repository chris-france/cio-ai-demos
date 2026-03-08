import { useState } from 'react'
import { CheckCircle, Clock, ChevronDown, ChevronUp, Copy, Check, FolderOpen, ExternalLink } from 'lucide-react'

function CopyButton({ text, label = 'Copy' }) {
  const [copied, setCopied] = useState(false)
  const copy = async (e) => {
    e.stopPropagation()
    await navigator.clipboard.writeText(text)
    setCopied(true)
    setTimeout(() => setCopied(false), 2000)
  }
  return (
    <button
      onClick={copy}
      className="flex items-center gap-1 text-xs text-gray-400 hover:text-france-blue transition-colors"
    >
      {copied ? <Check size={12} /> : <Copy size={12} />}
      {copied ? 'Copied!' : label}
    </button>
  )
}

export default function DemoCard({ demo }) {
  const [expanded, setExpanded] = useState(false)
  const isReady = demo.status === 'ready'

  return (
    <div className="bg-white rounded-lg border border-gray-200 shadow-sm hover:shadow-md transition-all">
      {/* Card header */}
      <div
        className="p-5 cursor-pointer"
        onClick={() => isReady && setExpanded(!expanded)}
      >
        <div className="flex items-start justify-between gap-3">
          <div className="flex-1 min-w-0">
            <div className="text-xs font-bold text-france-blue tracking-wide mb-1">
              LECTURE {demo.num}
            </div>
            <h3 className="text-base font-semibold text-gray-900 mb-1">
              {demo.title}
            </h3>
            <p className="text-sm text-gray-500 leading-relaxed">
              {demo.subtitle}
            </p>
          </div>
          <div className="shrink-0 flex items-center gap-2">
            {isReady ? (
              <CheckCircle className="w-5 h-5 text-green-500" />
            ) : (
              <Clock className="w-5 h-5 text-gray-300" />
            )}
          </div>
        </div>

        {/* Demo summary */}
        {isReady && (
          <div className="mt-3 flex items-center justify-between">
            <div className="flex items-center gap-3">
              <span className="text-xs font-medium text-green-600">Ready</span>
              <span className="text-xs text-gray-400">{demo.time}</span>
              {demo.tool && (
                <span className="text-xs bg-blue-50 text-blue-700 px-2 py-0.5 rounded-full font-medium">
                  {demo.tool}
                </span>
              )}
            </div>
            {isReady && (
              <button className="text-gray-400 hover:text-gray-600">
                {expanded ? <ChevronUp size={18} /> : <ChevronDown size={18} />}
              </button>
            )}
          </div>
        )}
        {!isReady && (
          <div className="mt-3">
            <span className="text-xs font-medium text-gray-400">Coming Soon</span>
          </div>
        )}
      </div>

      {/* Expanded detail */}
      {expanded && isReady && (
        <div className="border-t border-gray-100 px-5 pb-5">
          {/* Demo description */}
          <div className="mt-4">
            <h4 className="text-xs font-bold text-gray-700 uppercase tracking-wide mb-2">What You'll Do</h4>
            <p className="text-sm text-gray-600 leading-relaxed">{demo.description}</p>
          </div>

          {/* Prerequisites */}
          {demo.prerequisites && (
            <div className="mt-4">
              <h4 className="text-xs font-bold text-gray-700 uppercase tracking-wide mb-2">Prerequisites</h4>
              <ul className="text-sm text-gray-600 space-y-1">
                {demo.prerequisites.map((p, i) => (
                  <li key={i} className="flex items-start gap-2">
                    <span className="text-france-blue mt-0.5">-</span>
                    <span>{p}</span>
                  </li>
                ))}
              </ul>
            </div>
          )}

          {/* Steps */}
          {demo.steps && (
            <div className="mt-4">
              <h4 className="text-xs font-bold text-gray-700 uppercase tracking-wide mb-2">Steps</h4>
              <ol className="text-sm text-gray-600 space-y-2">
                {demo.steps.map((step, i) => (
                  <li key={i} className="flex items-start gap-2">
                    <span className="text-france-blue font-bold shrink-0">{i + 1}.</span>
                    <span>{step}</span>
                  </li>
                ))}
              </ol>
            </div>
          )}

          {/* CC Prompt */}
          {demo.cc_prompt && (
            <div className="mt-4">
              <div className="flex items-center justify-between mb-2">
                <h4 className="text-xs font-bold text-gray-700 uppercase tracking-wide">Paste This Prompt</h4>
                <CopyButton text={demo.cc_prompt} />
              </div>
              <div className="bg-gray-900 text-green-400 rounded-lg p-4 text-sm font-mono leading-relaxed whitespace-pre-wrap">
                {demo.cc_prompt}
              </div>
            </div>
          )}

          {/* Follow-up prompts */}
          {demo.followups && demo.followups.length > 0 && (
            <div className="mt-4">
              <h4 className="text-xs font-bold text-gray-700 uppercase tracking-wide mb-2">Keep Going — Paste These Next</h4>
              <div className="space-y-2">
                {demo.followups.map((followup, i) => (
                  <div key={i} className="flex items-start gap-2 bg-gray-50 rounded-lg p-3 group">
                    <span className="text-france-cyan font-bold text-sm shrink-0">{i + 1}.</span>
                    <p className="text-sm text-gray-700 flex-1 font-mono">{followup}</p>
                    <CopyButton text={followup} label="" />
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* CIO Takeaway */}
          {demo.takeaway && (
            <div className="mt-4 bg-amber-50 border border-amber-200 rounded-lg p-3">
              <h4 className="text-xs font-bold text-amber-800 uppercase tracking-wide mb-1">CIO Takeaway</h4>
              <p className="text-sm text-amber-900 italic">"{demo.takeaway}"</p>
            </div>
          )}

          {/* Folder reference */}
          <div className="mt-4 flex items-center gap-3">
            {demo.folder && (
              <span className="flex items-center gap-1.5 text-xs text-gray-500">
                <FolderOpen size={14} />
                <code className="bg-gray-100 px-2 py-0.5 rounded">{demo.folder}</code>
              </span>
            )}
            {demo.link && (
              <a
                href={demo.link}
                target="_blank"
                rel="noopener noreferrer"
                className="flex items-center gap-1.5 text-xs text-france-blue hover:underline"
                onClick={(e) => e.stopPropagation()}
              >
                <ExternalLink size={12} />
                Open Demo App
              </a>
            )}
          </div>
        </div>
      )}
    </div>
  )
}
