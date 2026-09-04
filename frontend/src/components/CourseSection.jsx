import { useState } from 'react'
import { ChevronDown } from 'lucide-react'
import DemoCard from './DemoCard'

export default function CourseSection({ course, badge, badgeColor, defaultOpen = false }) {
  const [open, setOpen] = useState(defaultOpen)
  const readyCount = course.demos?.filter(d => d.status === 'ready').length || 0
  const totalCount = course.demos?.length || 0

  return (
    <section className="mb-6">
      <button
        onClick={() => setOpen(!open)}
        className="w-full max-w-2xl text-left group"
      >
        <div className="flex items-center gap-3 mb-1">
          <h2 className="text-xl font-bold text-gray-900 group-hover:text-france-blue transition-colors">
            {course.title}
          </h2>
          <span className="text-sm text-gray-500">&mdash; {course.subtitle}</span>
          <span className="text-xs text-gray-400 ml-auto">{readyCount}/{totalCount} ready</span>
          <ChevronDown
            size={18}
            className={`text-gray-400 transition-transform duration-200 ${open ? 'rotate-180' : ''}`}
          />
        </div>

        <div className="flex items-center gap-3 mb-2">
          <span className={`${badgeColor} text-white text-[11px] font-bold px-3 py-0.5 rounded-full tracking-wide`}>
            {badge}
          </span>
          <span className="text-sm text-gray-600">{course.description}</span>
        </div>
      </button>

      {open && (
        <div className="grid grid-cols-1 gap-4 max-w-2xl mt-4 animate-in fade-in duration-200">
          {course.demos?.map(demo => (
            <DemoCard key={demo.num} demo={demo} />
          ))}
        </div>
      )}
    </section>
  )
}
