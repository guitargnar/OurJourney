import { useState, useEffect } from 'react'
import axios from 'axios'
import { format, formatDistanceToNow } from 'date-fns'
import { Heart, Plus, Target, Sparkles, Trophy, Star, ChevronRight, Calendar as CalendarIcon } from 'lucide-react'
import { styles } from './styles'
import Calendar from './Calendar'

const API_URL = 'http://localhost:3001/api'

const MOODS = {
  excited: '🤩',
  happy: '😊',
  neutral: '😐',
  thoughtful: '🤔',
  challenging: '😤'
}

function AppSimple() {
  const [entries, setEntries] = useState([])
  const [nextAdventure, setNextAdventure] = useState(null)
  const [stats, setStats] = useState(null)
  const [quickInput, setQuickInput] = useState('')
  const [activeView, setActiveView] = useState('dashboard')

  useEffect(() => {
    loadDashboard()
    const interval = setInterval(loadDashboard, 30000)
    return () => clearInterval(interval)
  }, [])

  const loadDashboard = async () => {
    try {
      const [entriesRes, adventureRes, statsRes] = await Promise.all([
        axios.get(`${API_URL}/entries?limit=20`),
        axios.get(`${API_URL}/anticipation/next`),
        axios.get(`${API_URL}/insights/stats`)
      ])
      
      setEntries(entriesRes.data || [])
      setNextAdventure(adventureRes.data)
      setStats(statsRes.data || {})
    } catch (error) {
      console.error('Error loading dashboard:', error)
    }
  }

  const handleQuickCapture = async (e) => {
    e.preventDefault()
    if (!quickInput.trim()) return

    try {
      const input = quickInput.toLowerCase()
      const originalInput = quickInput
      let type = 'idea'
      let targetDate = null
      let targetTime = null
      let location = null
      
      // Enhanced calendar detection patterns
      const calendarPatterns = [
        /date|dinner|lunch|breakfast|movie|concert|show|tickets?/i,
        /tomorrow|tonight|weekend|next \w+day|this \w+day/i,
        /at \d{1,2}(:\d{2})?\s?(am|pm)?/i,
        /(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)\w*\s+\d{1,2}/i,
        /\d{1,2}\/\d{1,2}/i
      ]
      
      const isCalendarEvent = calendarPatterns.some(pattern => pattern.test(originalInput))
      
      // Parse dates from natural language
      const parseDate = (text) => {
        const today = new Date()
        
        if (/tomorrow/i.test(text)) {
          const tomorrow = new Date(today)
          tomorrow.setDate(today.getDate() + 1)
          return tomorrow.toISOString().split('T')[0]
        }
        
        if (/tonight/i.test(text)) {
          return today.toISOString().split('T')[0]
        }
        
        if (/this weekend|saturday|sunday/i.test(text)) {
          const daysUntilSaturday = (6 - today.getDay() + 7) % 7 || 7
          const weekend = new Date(today)
          weekend.setDate(today.getDate() + daysUntilSaturday)
          if (/sunday/i.test(text)) {
            weekend.setDate(weekend.getDate() + 1)
          }
          return weekend.toISOString().split('T')[0]
        }
        
        // Try to extract MM/DD format
        const dateMatch = text.match(/(\d{1,2})\/(\d{1,2})/)
        if (dateMatch) {
          const month = parseInt(dateMatch[1])
          const day = parseInt(dateMatch[2])
          const year = today.getFullYear()
          const date = new Date(year, month - 1, day)
          if (date < today) {
            date.setFullYear(year + 1)
          }
          return date.toISOString().split('T')[0]
        }
        
        return null
      }
      
      // Parse time from natural language
      const parseTime = (text) => {
        const timeMatch = text.match(/at (\d{1,2})(:(\d{2}))?\s?(am|pm)?/i)
        if (timeMatch) {
          let hours = parseInt(timeMatch[1])
          const minutes = timeMatch[3] || '00'
          const period = timeMatch[4]
          
          if (period) {
            if (period.toLowerCase() === 'pm' && hours < 12) {
              hours += 12
            } else if (period.toLowerCase() === 'am' && hours === 12) {
              hours = 0
            }
          }
          
          return `${String(hours).padStart(2, '0')}:${minutes}`
        }
        
        // Common meal times
        if (/breakfast/i.test(text)) return '09:00'
        if (/lunch/i.test(text)) return '12:00'
        if (/dinner/i.test(text)) return '19:00'
        
        return null
      }
      
      // Parse location
      const parseLocation = (text) => {
        const locationMatch = text.match(/at ([^0-9][^,]+?)(?:\s+at\s+|\s+on\s+|$)/i)
        if (locationMatch && !/(\d{1,2}(:\d{2})?\s?(am|pm)?)/i.test(locationMatch[1])) {
          return locationMatch[1].trim()
        }
        return null
      }
      
      // Determine type and extract data
      if (input.includes('goal') || input.includes('want to') || input.includes('save for')) {
        type = 'goal'
      } else if (isCalendarEvent) {
        type = 'date'
        targetDate = parseDate(originalInput)
        targetTime = parseTime(originalInput)
        location = parseLocation(originalInput)
      } else if (input.includes('plan') || input.includes('going to')) {
        type = 'event'
        targetDate = parseDate(originalInput)
      } else if (input.includes('remember') || input.includes('today we') || input.includes('just')) {
        type = 'memory'
      } else if (input.includes('feeling') || input.includes('grateful') || input.includes('happy')) {
        type = 'feeling'
      }
      
      // Clean up title (remove parsed date/time/location for calendar events)
      let title = originalInput
      if (type === 'date' && targetTime) {
        title = title.replace(/at \d{1,2}(:\d{2})?\s?(am|pm)?/i, '').trim()
      }
      
      const entryData = {
        type,
        title,
        content: '',
        category: 'General',
        mood: 'neutral'
      }
      
      if (targetDate) entryData.target_date = targetDate
      if (targetTime) entryData.target_time = targetTime
      if (location) entryData.location = location

      await axios.post(`${API_URL}/entries`, entryData)
      
      setQuickInput('')
      loadDashboard()
      
      // If calendar event was created, switch to calendar view
      if (type === 'date') {
        setActiveView('calendar')
      }
    } catch (error) {
      console.error('Error creating entry:', error)
    }
  }

  const updateProgress = async (id, progress) => {
    try {
      await axios.put(`${API_URL}/entries/${id}`, { progress })
      loadDashboard()
    } catch (error) {
      console.error('Error updating progress:', error)
    }
  }

  const goals = entries.filter(e => e.type === 'goal' && e.status === 'active')
  const memories = entries.filter(e => e.type === 'memory')

  return (
    <div style={styles.container}>
      {/* Header */}
      <header style={styles.header}>
        <div style={styles.headerContent}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
            <Heart size={32} color="#f43f5e" />
            <div>
              <h1 style={{ fontSize: '24px', fontWeight: 'bold', margin: 0 }}>OurJourney</h1>
              <p style={{ fontSize: '14px', color: '#6b7280', margin: 0 }}>Building our story together</p>
            </div>
          </div>
          
          <nav style={styles.nav}>
            <button
              onClick={() => setActiveView('dashboard')}
              style={{
                ...styles.navButton,
                ...(activeView === 'dashboard' ? styles.navButtonActive : {})
              }}
            >
              Dashboard
            </button>
            <button
              onClick={() => setActiveView('timeline')}
              style={{
                ...styles.navButton,
                ...(activeView === 'timeline' ? styles.navButtonActive : {})
              }}
            >
              Timeline
            </button>
            <button
              onClick={() => setActiveView('calendar')}
              style={{
                ...styles.navButton,
                ...(activeView === 'calendar' ? styles.navButtonActive : {})
              }}
            >
              Calendar
            </button>
          </nav>

          {stats && (
            <div style={{ display: 'flex', gap: '1rem', fontSize: '14px' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '4px' }}>
                <Trophy size={16} color="#eab308" />
                <span>{stats.goals_completed || 0} completed</span>
              </div>
              <div style={{ display: 'flex', alignItems: 'center', gap: '4px' }}>
                <Star size={16} color="#3b82f6" />
                <span>{stats.memories_created || 0} memories</span>
              </div>
            </div>
          )}
        </div>
      </header>

      {/* Quick Capture */}
      <div style={styles.quickCapture}>
        <div style={styles.quickCaptureContent}>
          <form onSubmit={handleQuickCapture} style={styles.quickCaptureForm}>
            <input
              type="text"
              value={quickInput}
              onChange={(e) => setQuickInput(e.target.value)}
              placeholder="Try: 'Dinner tomorrow at 7pm' or 'Concert tickets for 11/12' or 'Goal: Save $5000'"
              style={styles.quickCaptureInput}
            />
            <button type="submit" style={styles.quickCaptureButton}>
              <Plus size={16} />
              Add
            </button>
          </form>
        </div>
      </div>

      {/* Main Content */}
      <main style={styles.main}>
        {activeView === 'dashboard' && (
          <div>
            {/* Next Adventure */}
            {nextAdventure && (
              <div style={styles.anticipationCard}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                  <div>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '8px' }}>
                      <Sparkles size={20} />
                      <span style={{ fontSize: '14px', fontWeight: '500' }}>Next Adventure</span>
                    </div>
                    <h2 style={{ fontSize: '28px', fontWeight: 'bold', margin: '0 0 8px 0' }}>
                      {nextAdventure.title}
                    </h2>
                    <p style={{ opacity: 0.9 }}>{nextAdventure.content}</p>
                  </div>
                  <div style={{ textAlign: 'center' }}>
                    <div style={{ fontSize: '48px', fontWeight: 'bold' }}>
                      {nextAdventure.days_until}
                    </div>
                    <div style={{ fontSize: '14px' }}>days to go!</div>
                  </div>
                </div>
              </div>
            )}

            {/* Active Goals */}
            <div style={styles.card}>
              <h3 style={{ fontSize: '20px', fontWeight: '600', marginBottom: '1rem', display: 'flex', alignItems: 'center', gap: '8px' }}>
                <Target size={20} color="#10b981" />
                Active Goals
              </h3>
              <div>
                {goals.slice(0, 3).map(goal => (
                  <div key={goal.id} style={styles.goalCard}>
                    <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '8px' }}>
                      <h4 style={{ fontWeight: '500', margin: 0 }}>{goal.title}</h4>
                      <span style={{ fontSize: '14px', color: '#6b7280' }}>{goal.progress}%</span>
                    </div>
                    <div style={styles.progressBar}>
                      <div 
                        style={{
                          ...styles.progressBarFill,
                          width: `${goal.progress}%`
                        }}
                      />
                    </div>
                    <button
                      onClick={() => updateProgress(goal.id, Math.min(100, goal.progress + 10))}
                      style={{
                        marginTop: '8px',
                        padding: '4px 8px',
                        fontSize: '14px',
                        backgroundColor: '#dbeafe',
                        color: '#1e40af',
                        border: 'none',
                        borderRadius: '4px',
                        cursor: 'pointer'
                      }}
                    >
                      +10%
                    </button>
                  </div>
                ))}
              </div>
            </div>

            {/* Recent Memories */}
            <div style={styles.card}>
              <h3 style={{ fontSize: '20px', fontWeight: '600', marginBottom: '1rem', display: 'flex', alignItems: 'center', gap: '8px' }}>
                <Heart size={20} color="#f43f5e" />
                Recent Memories
              </h3>
              <div>
                {memories.slice(0, 4).map(memory => (
                  <div key={memory.id} style={styles.memoryCard}>
                    <div style={{ display: 'flex', justifyContent: 'space-between' }}>
                      <div>
                        <h4 style={{ fontWeight: '500', margin: '0 0 4px 0' }}>{memory.title}</h4>
                        {memory.content && (
                          <p style={{ fontSize: '14px', color: '#6b7280', margin: 0 }}>{memory.content}</p>
                        )}
                      </div>
                      {memory.mood && (
                        <span style={{ fontSize: '24px' }}>{MOODS[memory.mood]}</span>
                      )}
                    </div>
                    <div style={{ fontSize: '12px', color: '#9ca3af', marginTop: '8px' }}>
                      {formatDistanceToNow(new Date(memory.created_at), { addSuffix: true })}
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        )}

        {activeView === 'calendar' && (
          <Calendar />
        )}

        {activeView === 'timeline' && (
          <div style={styles.card}>
            <h2 style={{ fontSize: '24px', fontWeight: 'bold', marginBottom: '1.5rem' }}>
              Our Journey Timeline
            </h2>
            <div>
              {entries.map((entry, index) => (
                <div key={entry.id} style={{ display: 'flex', gap: '1rem', marginBottom: '1.5rem' }}>
                  <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
                    <div style={{
                      ...styles.timelineDot,
                      backgroundColor: entry.type === 'goal' ? '#10b981' :
                                     entry.type === 'event' ? '#3b82f6' :
                                     entry.type === 'memory' ? '#f43f5e' : '#9ca3af'
                    }} />
                    {index < entries.length - 1 && (
                      <div style={styles.timelineLine} />
                    )}
                  </div>
                  <div style={{ flex: 1, paddingBottom: '1rem' }}>
                    <div style={{ fontSize: '14px', color: '#6b7280', marginBottom: '4px' }}>
                      {format(new Date(entry.created_at), 'MMM d, yyyy')}
                    </div>
                    <h3 style={{ fontWeight: '500', margin: '0 0 4px 0' }}>{entry.title}</h3>
                    {entry.content && (
                      <p style={{ fontSize: '14px', color: '#6b7280', margin: 0 }}>{entry.content}</p>
                    )}
                    <div style={{ display: 'flex', gap: '8px', marginTop: '8px' }}>
                      <span style={{
                        fontSize: '12px',
                        padding: '2px 8px',
                        backgroundColor: '#f3f4f6',
                        borderRadius: '4px'
                      }}>
                        {entry.type}
                      </span>
                      {entry.mood && (
                        <span>{MOODS[entry.mood]}</span>
                      )}
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}
      </main>
    </div>
  )
}

export default AppSimple