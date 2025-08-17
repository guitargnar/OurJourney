# OurJourney API Documentation

## Base URL
```
http://localhost:3001/api
```

## Endpoints

### Entries

#### Get All Entries
```
GET /entries
Query params: 
  - type: filter by type (goal, event, memory, ritual, feeling, idea, date)
  - status: filter by status (active, completed, archived, cancelled)
  - category: filter by category
  - limit: max number of results (default: 50)
```

#### Create Entry
```
POST /entries
Body: {
  type, title, content, category, mood, 
  target_date, tags, author
}
```

#### Update Entry
```
PUT /entries/:id
Body: Any fields to update
```

#### Complete Entry
```
POST /entries/:id/complete
Marks entry as completed and sets progress to 100%
```

### Calendar

#### Get Month Events
```
GET /calendar/month/:year/:month
Returns all events for specified month
```

#### Get Day Events
```
GET /calendar/day/:date
Returns events for specific date (format: YYYY-MM-DD)
```

#### Create Calendar Event
```
POST /calendar/event
Body: {
  title, content, target_date, target_time,
  end_date, location, recurrence, reminder_minutes
}
```

### Anticipation

#### Get Next Adventure
```
GET /anticipation/next
Returns the nearest upcoming event with countdown
```

#### Get Upcoming Events
```
GET /anticipation/upcoming
Returns next 5 upcoming events/goals
```

### Rituals

#### Get Current Week Ritual
```
GET /rituals/current
Returns or creates ritual for current week
```

#### Update Ritual
```
PUT /rituals/:id
Body: {
  gratitude, challenges, excitement, 
  mood_score, reflections
}
```

### Insights

#### Get Timeline Data
```
GET /insights/timeline
Returns aggregated timeline entries
```

#### Get Statistics
```
GET /insights/stats
Returns relationship statistics
```

#### Export for AI
```
GET /insights/export
Returns formatted text for ChatGPT/Claude visualization
```

## Data Types

### Entry Types
- `goal` - Trackable goals with progress
- `event` - Future events with countdowns
- `memory` - Past experiences to remember
- `ritual` - Weekly check-ins
- `feeling` - Emotional entries
- `idea` - Thoughts and ideas
- `date` - Calendar-specific events with times

### Status Values
- `active` - Currently active
- `completed` - Successfully completed
- `archived` - Archived for history
- `cancelled` - Cancelled event

### Mood Values
- `excited` - 🤩
- `happy` - 😊
- `neutral` - 😐
- `thoughtful` - 🤔
- `challenging` - 😤

### Recurrence Values
- `none` - One-time event
- `weekly` - Repeats weekly
- `monthly` - Repeats monthly
- `yearly` - Repeats yearly