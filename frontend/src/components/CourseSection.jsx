import DemoCard from './DemoCard'

export default function CourseSection({ course, badge, badgeColor }) {
  return (
    <section className="mb-12">
      <div className="flex items-center gap-3 mb-2">
        <h2 className="text-xl font-bold text-gray-900">
          {course.title}
        </h2>
        <span className="text-sm text-gray-500">&mdash; {course.subtitle}</span>
      </div>

      <div className="flex items-center gap-3 mb-6">
        <span className={`${badgeColor} text-white text-[11px] font-bold px-3 py-0.5 rounded-full tracking-wide`}>
          {badge}
        </span>
        <span className="text-sm text-gray-600">{course.description}</span>
      </div>

      <div className="grid grid-cols-1 gap-4 max-w-2xl">
        {course.demos?.map(demo => (
          <DemoCard key={demo.num} demo={demo} />
        ))}
      </div>
    </section>
  )
}
