# ARCHITECTURE

## Overview
Client-server architecture with separate frontend and backend.

## Frontend
- Technologies: HTML5, CSS3, Vanilla JavaScript
- Hosting: GitHub Pages
- Responsibilities: UI rendering, navigation, beat catalog display, YouTube Embedded Player
- Communicates with backend via HTTP requests (fetch API)

## Backend
- Language: Python 3.13
- Framework: Flask 3.1.3
- Hosting: TBD
- Responsibilities: YouTube Data API v3 communication, data processing, REST API
- In-memory cache to reduce API quota usage
- CORS configured for GitHub Pages domain

## External API
- Service: YouTube Data API v3
- Data retrieved: video ID, title, thumbnail, publish date, view count, video URL
- Strategy: paginate full uploads playlist, batch video stats in groups of 50

## Endpoints
- GET /api/health — backend availability check
- GET /api/beats — latest 24 beats ordered by publish date
- GET /api/beats/popular — top 5 beats by view count across full catalog

## Response Format
JSON for all endpoints.

## Data Flow
1. User opens the page
2. Frontend requests catalog from backend
3. Backend checks in-memory cache
4. If cache miss: backend queries YouTube Data API v3
5. Backend processes and returns JSON
6. Frontend renders beat cards
7. User selects a beat
8. YouTube Embedded Player loads the selected video

## Security
- YouTube API Key stored in environment variable (never in frontend)
- HTTPS required in production
- CORS restricted to GitHub Pages domain
- No sensitive data exposed in API responses

## Caching Strategy
- In-memory cache with configurable TTL
- Avoids redundant YouTube API calls
- Cache resets on backend restart
