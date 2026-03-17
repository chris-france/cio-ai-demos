import { useState, useEffect, useCallback, useRef } from 'react'

export function useWorkbookSchemas() {
  const [schemas, setSchemas] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetch('/api/workbook/schemas')
      .then(r => r.json())
      .then(setSchemas)
      .catch(() => {})
      .finally(() => setLoading(false))
  }, [])

  return { schemas, loading }
}

export function useWorkbookProgress() {
  const [progress, setProgress] = useState({ completed: [], total: 0 })

  const refresh = useCallback(() => {
    fetch('/api/workbook/progress')
      .then(r => r.json())
      .then(setProgress)
      .catch(() => {})
  }, [])

  useEffect(() => { refresh() }, [refresh])

  return { progress, refresh }
}

export function useWorkbookData(lectureNum) {
  const [data, setData] = useState({})
  const [loading, setLoading] = useState(true)
  const [saveStatus, setSaveStatus] = useState(null) // null | 'saving' | 'saved' | 'error'
  const timerRef = useRef(null)

  useEffect(() => {
    if (!lectureNum) return
    fetch(`/api/workbook/${lectureNum}`)
      .then(r => r.json())
      .then(d => {
        const result = {}
        for (const [key, val] of Object.entries(d)) {
          result[key] = val.data
        }
        setData(result)
      })
      .catch(() => {})
      .finally(() => setLoading(false))
  }, [lectureNum])

  const save = useCallback((sectionKey, sectionData) => {
    setData(prev => ({ ...prev, [sectionKey]: sectionData }))

    if (timerRef.current) clearTimeout(timerRef.current)
    setSaveStatus('saving')

    timerRef.current = setTimeout(() => {
      fetch(`/api/workbook/${lectureNum}/${sectionKey}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ data: sectionData }),
      })
        .then(r => {
          if (!r.ok) throw new Error()
          setSaveStatus('saved')
          setTimeout(() => setSaveStatus(null), 1500)
        })
        .catch(() => {
          setSaveStatus('error')
          setTimeout(() => setSaveStatus(null), 2000)
        })
    }, 800)
  }, [lectureNum])

  return { data, loading, save, saveStatus }
}
