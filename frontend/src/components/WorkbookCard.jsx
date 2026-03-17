import { useState } from 'react'
import { CheckCircle, Circle, ChevronDown, ChevronUp, Save, Loader2 } from 'lucide-react'
import WorkbookForm from './WorkbookForm'
import { useWorkbookData } from '../hooks/useWorkbook'

export default function WorkbookCard({ lectureNum, schema, isComplete }) {
  const [expanded, setExpanded] = useState(false)
  const { data, loading, save, saveStatus } = useWorkbookData(expanded ? lectureNum : null)

  return (
    <div className="bg-white rounded-lg border border-gray-200 shadow-sm hover:shadow-md transition-all">
      <div
        className="p-5 cursor-pointer"
        onClick={() => setExpanded(!expanded)}
      >
        <div className="flex items-start justify-between gap-3">
          <div className="flex-1 min-w-0">
            <div className="text-xs font-bold text-france-blue tracking-wide mb-1">
              LECTURE {lectureNum}
            </div>
            <h3 className="text-base font-semibold text-gray-900 mb-1">
              {schema.title}
            </h3>
            <p className="text-sm text-gray-500">
              {schema.lecture_title}
            </p>
          </div>
          <div className="shrink-0 flex items-center gap-2">
            {isComplete ? (
              <CheckCircle className="w-5 h-5 text-green-500" />
            ) : (
              <Circle className="w-5 h-5 text-gray-300" />
            )}
          </div>
        </div>
        <div className="mt-3 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <span className={`text-xs font-medium ${isComplete ? 'text-green-600' : 'text-gray-400'}`}>
              {isComplete ? 'In Progress' : 'Not Started'}
            </span>
            {saveStatus === 'saving' && (
              <span className="flex items-center gap-1 text-xs text-gray-400">
                <Loader2 size={12} className="animate-spin" /> Saving...
              </span>
            )}
            {saveStatus === 'saved' && (
              <span className="flex items-center gap-1 text-xs text-green-500">
                <Save size={12} /> Saved
              </span>
            )}
            {saveStatus === 'error' && (
              <span className="text-xs text-red-500">Save failed</span>
            )}
          </div>
          <button className="text-gray-400 hover:text-gray-600">
            {expanded ? <ChevronUp size={18} /> : <ChevronDown size={18} />}
          </button>
        </div>
      </div>

      {expanded && (
        <div className="border-t border-gray-100 px-5 pb-5 pt-4">
          {loading ? (
            <div className="text-sm text-gray-400 py-4 text-center">Loading...</div>
          ) : (
            schema.sections?.map(section => (
              <div key={section.key} className="mb-6 last:mb-0">
                <h4 className="text-xs font-bold text-gray-700 uppercase tracking-wide mb-3">
                  {section.title}
                </h4>
                <WorkbookForm
                  section={section}
                  data={data[section.key]}
                  onChange={(sectionData) => save(section.key, sectionData)}
                />
              </div>
            ))
          )}
        </div>
      )}
    </div>
  )
}
