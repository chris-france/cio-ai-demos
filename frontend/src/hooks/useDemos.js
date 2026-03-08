import { useState, useEffect, useCallback } from 'react'

export function useDemos() {
  const [demos, setDemos] = useState(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  const fetchDemos = useCallback(async () => {
    try {
      const res = await fetch('/api/demos')
      if (!res.ok) throw new Error(`HTTP ${res.status}`)
      const data = await res.json()
      setDemos(data)
      setError(null)
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }, [])

  useEffect(() => {
    fetchDemos()
  }, [fetchDemos])

  return { demos, loading, error, retry: fetchDemos }
}
