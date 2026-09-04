import { useState } from 'react'
import { ChevronDown } from 'lucide-react'
import WorkbookCard from './WorkbookCard'
import { useWorkbookSchemas, useWorkbookProgress } from '../hooks/useWorkbook'

const WORKBOOK_COURSES = [
  { label: 'Foundation Workbook', badge: 'FOUNDATION', badgeColor: 'bg-france-blue', range: [1, 7], defaultOpen: false },
  { label: 'Advanced Workbook', badge: 'ADVANCED', badgeColor: 'bg-france-cyan', range: [8, 15], defaultOpen: false },
  { label: 'Service Management Workbook', badge: 'SERVICE MGMT', badgeColor: 'bg-emerald-600', range: [16, 23], defaultOpen: false },
]

function WorkbookCourseSection({ course, entries, progress }) {
  const [open, setOpen] = useState(course.defaultOpen)
  const [min, max] = course.range
  const sectionEntries = entries.filter(e => e.num >= min && e.num <= max)
  const startedCount = sectionEntries.filter(e => progress.completed.includes(e.num)).length

  if (sectionEntries.length === 0) return null

  return (
    <section className="mb-6">
      <button
        onClick={() => setOpen(!open)}
        className="w-full max-w-2xl text-left group"
      >
        <div className="flex items-center gap-3 mb-1">
          <h2 className="text-xl font-bold text-gray-900 group-hover:text-france-blue transition-colors">
            {course.label}
          </h2>
          <span className="text-xs text-gray-400 ml-auto">{startedCount}/{sectionEntries.length} started</span>
          <ChevronDown
            size={18}
            className={`text-gray-400 transition-transform duration-200 ${open ? 'rotate-180' : ''}`}
          />
        </div>
        <div className="flex items-center gap-3 mb-2">
          <span className={`${course.badgeColor} text-white text-[11px] font-bold px-3 py-0.5 rounded-full tracking-wide`}>
            {course.badge}
          </span>
        </div>
      </button>

      {open && (
        <div className="grid grid-cols-1 gap-4 max-w-2xl mt-4 animate-in fade-in duration-200">
          {sectionEntries.map(e => (
            <WorkbookCard
              key={e.num}
              lectureNum={e.num}
              schema={e.schema}
              isComplete={progress.completed.includes(e.num)}
            />
          ))}
        </div>
      )}
    </section>
  )
}

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

      {WORKBOOK_COURSES.map(course => (
        <WorkbookCourseSection
          key={course.label}
          course={course}
          entries={entries}
          progress={progress}
        />
      ))}
    </div>
  )
}
