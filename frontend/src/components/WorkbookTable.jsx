import { Plus, Trash2 } from 'lucide-react'

export default function WorkbookTable({ schema, data = [], onChange }) {
  const columns = schema.columns || []
  const rows = data.length > 0 ? data : (schema.default_data || Array.from({ length: schema.initial_rows || 5 }, () => ({})))

  const updateCell = (rowIdx, colName, value) => {
    const updated = rows.map((row, i) => i === rowIdx ? { ...row, [colName]: value } : row)
    onChange(updated)
  }

  const addRow = () => {
    onChange([...rows, {}])
  }

  const deleteRow = (rowIdx) => {
    if (rows.length <= 1) return
    onChange(rows.filter((_, i) => i !== rowIdx))
  }

  return (
    <div className="overflow-x-auto">
      <table className="w-full text-sm border-collapse">
        <thead>
          <tr>
            <th className="text-left text-xs font-semibold text-gray-500 uppercase tracking-wide px-2 py-2 border-b border-gray-200 w-8">#</th>
            {columns.map(col => (
              <th key={col.name} className="text-left text-xs font-semibold text-gray-500 uppercase tracking-wide px-2 py-2 border-b border-gray-200">
                {col.label}
              </th>
            ))}
            <th className="w-8 border-b border-gray-200" />
          </tr>
        </thead>
        <tbody>
          {rows.map((row, rowIdx) => (
            <tr key={rowIdx} className="group hover:bg-gray-50">
              <td className="text-xs text-gray-400 px-2 py-1.5 border-b border-gray-100">{rowIdx + 1}</td>
              {columns.map(col => (
                <td key={col.name} className="px-1 py-1 border-b border-gray-100">
                  {col.type === 'select' ? (
                    <select
                      value={row[col.name] || ''}
                      onChange={(e) => updateCell(rowIdx, col.name, e.target.value)}
                      className="w-full text-sm border border-gray-200 rounded px-2 py-1.5 bg-white focus:outline-none focus:ring-1 focus:ring-france-blue/30 focus:border-france-blue"
                    >
                      <option value="">—</option>
                      {col.options?.map(opt => <option key={opt} value={opt}>{opt}</option>)}
                    </select>
                  ) : (
                    <input
                      type={col.type === 'number' ? 'number' : 'text'}
                      value={row[col.name] || ''}
                      onChange={(e) => updateCell(rowIdx, col.name, e.target.value)}
                      placeholder={col.placeholder || ''}
                      className="w-full text-sm border border-gray-200 rounded px-2 py-1.5 focus:outline-none focus:ring-1 focus:ring-france-blue/30 focus:border-france-blue"
                    />
                  )}
                </td>
              ))}
              <td className="px-1 py-1 border-b border-gray-100">
                <button
                  onClick={() => deleteRow(rowIdx)}
                  className="opacity-0 group-hover:opacity-100 text-gray-300 hover:text-red-400 transition-all p-1"
                  title="Delete row"
                >
                  <Trash2 size={14} />
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
      <button
        onClick={addRow}
        className="mt-2 flex items-center gap-1 text-xs text-france-blue hover:text-france-blue-dark transition-colors px-2 py-1"
      >
        <Plus size={14} />
        Add Row
      </button>
    </div>
  )
}
