import { useState } from 'react'
import Header from './components/Header'
import CourseSection from './components/CourseSection'
import WorkbookView from './components/WorkbookView'
import { useDemos } from './hooks/useDemos'

export default function App() {
  const [tab, setTab] = useState('demos')
  const { demos, loading, error, retry } = useDemos()

  if (loading) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-gray-400 text-sm">Loading demos...</div>
      </div>
    )
  }

  if (error || !demos) {
    return (
      <div className="min-h-screen bg-gray-50">
        <Header />
        <div className="flex flex-col items-center justify-center py-20 gap-4">
          <p className="text-gray-500 text-sm">Failed to load demos. Is the backend running on port 18801?</p>
          <button onClick={retry} className="px-4 py-2 bg-france-blue text-white text-sm rounded-lg hover:bg-france-blue-dark">
            Retry
          </button>
        </div>
      </div>
    )
  }

  const foundationReady = demos?.foundation?.demos?.filter(d => d.status === 'ready').length || 0
  const advancedReady = demos?.advanced?.demos?.filter(d => d.status === 'ready').length || 0

  return (
    <div className="min-h-screen bg-gray-50">
      <Header />

      <main className="max-w-6xl mx-auto px-6 py-8">
        {/* Tab navigation */}
        <div className="flex gap-1 mb-8 border-b border-gray-200">
          <button
            onClick={() => setTab('demos')}
            className={`px-5 py-2.5 text-sm font-semibold border-b-2 transition-colors ${
              tab === 'demos'
                ? 'border-france-blue text-france-blue'
                : 'border-transparent text-gray-500 hover:text-gray-700'
            }`}
          >
            Demos
          </button>
          <button
            onClick={() => setTab('workbook')}
            className={`px-5 py-2.5 text-sm font-semibold border-b-2 transition-colors ${
              tab === 'workbook'
                ? 'border-france-blue text-france-blue'
                : 'border-transparent text-gray-500 hover:text-gray-700'
            }`}
          >
            Workbook
          </button>
        </div>

        {tab === 'demos' && (
          <>
            {/* How to use banner */}
            <div className="bg-blue-50 border border-blue-200 rounded-xl p-5 mb-8">
              <h2 className="text-sm font-bold text-blue-900 mb-2">How to Use These Demos</h2>
              <ol className="text-sm text-blue-800 space-y-1.5">
                <li><strong>1. Watch the lecture video first</strong> — don't stop to do the demos, just watch me walk through them.</li>
                <li><strong>2. Come back here</strong> — expand a demo card below.</li>
                <li><strong>3. Open a terminal and type <code className="bg-blue-100 px-1.5 py-0.5 rounded font-mono text-blue-900">claude</code></strong> — that's the only command you'll type.</li>
                <li><strong>4. Copy & paste the prompt</strong> — Claude Code does the rest: navigates, reads files, writes code, runs it.</li>
                <li><strong>5. Keep going</strong> — paste the follow-up prompts to go deeper. Fix errors by talking to CC, not by Googling.</li>
              </ol>
              <p className="text-xs text-blue-600 mt-3">
                All demos require <a href="https://docs.anthropic.com/en/docs/claude-code/overview" target="_blank" rel="noopener noreferrer" className="underline font-medium">Claude Code</a> with a Claude Pro or Max subscription ($20/month). No API key needed. You never leave the CC conversation.
              </p>
            </div>

            {/* Stats */}
            <div className="flex justify-start gap-6 mb-10">
              <div className="bg-white rounded-lg border border-gray-200 px-5 py-3 text-center shadow-sm">
                <div className="text-2xl font-bold text-france-blue">13</div>
                <div className="text-xs text-gray-500">Demos</div>
              </div>
              <div className="bg-white rounded-lg border border-gray-200 px-5 py-3 text-center shadow-sm">
                <div className="text-2xl font-bold text-green-600">{foundationReady + advancedReady}</div>
                <div className="text-xs text-gray-500">Ready</div>
              </div>
              <div className="bg-white rounded-lg border border-gray-200 px-5 py-3 text-center shadow-sm">
                <div className="text-2xl font-bold text-france-cyan">CC</div>
                <div className="text-xs text-gray-500">Powered By</div>
              </div>
            </div>

            {/* Foundation */}
            {demos?.foundation && (
              <CourseSection
                course={demos.foundation}
                badge="FOUNDATION"
                badgeColor="bg-france-blue"
              />
            )}

            {/* Advanced */}
            {demos?.advanced && (
              <CourseSection
                course={demos.advanced}
                badge="ADVANCED"
                badgeColor="bg-france-cyan"
              />
            )}
          </>
        )}

        {tab === 'workbook' && <WorkbookView />}

        {/* Footer */}
        <div className="text-center py-8 border-t border-gray-200 mt-12">
          <p className="text-xs text-gray-400">
            Chris France &middot; All demos built with Claude Code &middot; No third-party code
          </p>
        </div>
      </main>
    </div>
  )
}
