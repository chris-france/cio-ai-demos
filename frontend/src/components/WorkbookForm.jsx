import WorkbookTable from './WorkbookTable'

export default function WorkbookForm({ section, data, onChange }) {
  const isTable = section.type === 'table'

  if (isTable) {
    return (
      <WorkbookTable
        schema={section}
        data={data || []}
        onChange={onChange}
      />
    )
  }

  // Simple form fields
  const fields = section.fields || []
  const formData = data || section.default_data || {}

  const updateField = (name, value) => {
    onChange({ ...formData, [name]: value })
  }

  return (
    <div className="space-y-4">
      {fields.map(field => (
        <div key={field.name}>
          <label className="block text-sm font-medium text-gray-700 mb-1">
            {field.label}
          </label>
          {field.type === 'textarea' ? (
            <textarea
              value={formData[field.name] || ''}
              onChange={(e) => updateField(field.name, e.target.value)}
              placeholder={field.placeholder || ''}
              rows={3}
              className="w-full text-sm border border-gray-200 rounded-lg px-3 py-2 focus:outline-none focus:ring-1 focus:ring-france-blue/30 focus:border-france-blue resize-none"
            />
          ) : field.type === 'select' ? (
            <select
              value={formData[field.name] || ''}
              onChange={(e) => updateField(field.name, e.target.value)}
              className="w-full text-sm border border-gray-200 rounded-lg px-3 py-2 bg-white focus:outline-none focus:ring-1 focus:ring-france-blue/30 focus:border-france-blue"
            >
              <option value="">Select...</option>
              {field.options?.map(opt => <option key={opt} value={opt}>{opt}</option>)}
            </select>
          ) : (
            <input
              type={field.type === 'number' ? 'number' : 'text'}
              value={formData[field.name] || ''}
              onChange={(e) => updateField(field.name, e.target.value)}
              placeholder={field.placeholder || ''}
              min={field.min}
              max={field.max}
              className="w-full text-sm border border-gray-200 rounded-lg px-3 py-2 focus:outline-none focus:ring-1 focus:ring-france-blue/30 focus:border-france-blue"
            />
          )}
        </div>
      ))}
    </div>
  )
}
