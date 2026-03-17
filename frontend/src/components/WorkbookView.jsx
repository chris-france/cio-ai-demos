import WorkbookCard from './WorkbookCard'
import { useWorkbookSchemas, useWorkbookProgress } from '../hooks/useWorkbook'

export default function WorkbookView() {
  const { schemas, loading } = useWorkbookSchemas()
  const { progress } = useWorkbookProgress()

  if (loading || !schemas) {
    return <div className="text-gray-400 text-sm text-center py-12">Loading workbook...</div>
  }

  const entries = Object.entries(schemas).map(([num, schema]) => ({
    num: parseInt(num),
    schema,
  }))
  const foundation = entries.filter(e => e.num <= 7)
  const advanced = entries.filter(e => e.num > 7)

  const foundationDone = foundation.filter(e => progress.completed.includes(e.num)).length
  const advancedDone = advanced.filter(e => progress.completed.includes(e.num)).length

  return (
    <div>
      {/* Progress bar */}
      <div className="bg-white rounded-xl border border-gray-200 p-5 mb-8 shadow-sm">
        <div className="flex items-center justify-between mb-3">
          <h2 className="text-sm font-bold text-gray-900">Your Progress</h2>
          <span className="text-xs text-gray-500">
            {progress.completed.length} of {progress.total} sections started
          </span>
        </div>
        <div className="flex gap-1">
          {entries.map(e => (
            <div
              key={e.num}
              className={`flex-1 h-2 rounded-full ${
                progress.completed.includes(e.num)
                  ? 'bg-green-400'
                  : 'bg-gray-200'
              }`}
              title={`Lecture ${e.num}: ${e.schema.title}`}
            />
          ))}
        </div>
      </div>

      {/* Customize banner */}
      <div className="bg-blue-50 border border-blue-200 rounded-xl p-5 mb-8">
        <h2 className="text-sm font-bold text-blue-900 mb-1">This Is Your Workbook</h2>
        <p className="text-sm text-blue-800">
          Fill in each section as you complete the lectures. Your data is stored locally on your machine.
          After the course, use Claude Code to customize these forms for your business — the schema file
          is <code className="bg-blue-100 px-1.5 py-0.5 rounded font-mono text-blue-900 text-xs">backend/workbook_schemas.py</code>.
        </p>
      </div>

      {/* Foundation */}
      <section className="mb-12">
        <div className="flex items-center gap-3 mb-2">
          <h2 className="text-xl font-bold text-gray-900">Foundation Workbook</h2>
          <span className="text-sm text-gray-500">&mdash; Lectures 1-7</span>
        </div>
        <div className="flex items-center gap-3 mb-6">
          <span className="bg-france-blue text-white text-[11px] font-bold px-3 py-0.5 rounded-full tracking-wide">
            FOUNDATION
          </span>
          <span className="text-sm text-gray-600">
            {foundationDone} of {foundation.length} started
          </span>
        </div>
        <div className="grid grid-cols-1 gap-4 max-w-2xl">
          {foundation.map(e => (
            <WorkbookCard
              key={e.num}
              lectureNum={e.num}
              schema={e.schema}
              isComplete={progress.completed.includes(e.num)}
            />
          ))}
        </div>
      </section>

      {/* Advanced */}
      <section className="mb-12">
        <div className="flex items-center gap-3 mb-2">
          <h2 className="text-xl font-bold text-gray-900">Advanced Workbook</h2>
          <span className="text-sm text-gray-500">&mdash; Lectures 8-13</span>
        </div>
        <div className="flex items-center gap-3 mb-6">
          <span className="bg-france-cyan text-white text-[11px] font-bold px-3 py-0.5 rounded-full tracking-wide">
            ADVANCED
          </span>
          <span className="text-sm text-gray-600">
            {advancedDone} of {advanced.length} started
          </span>
        </div>
        <div className="grid grid-cols-1 gap-4 max-w-2xl">
          {advanced.map(e => (
            <WorkbookCard
              key={e.num}
              lectureNum={e.num}
              schema={e.schema}
              isComplete={progress.completed.includes(e.num)}
            />
          ))}
        </div>
      </section>
    </div>
  )
}
