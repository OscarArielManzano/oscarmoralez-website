# ARCHITECTURE

## Overview
Client-server architecture with separate frontend and backend.

## Frontend
- Technologies: HTML5, CSS3, Vanilla JavaScript
- Hosting: GitHub Pages
- Responsibilities: UI rendering, navigation, beat catalog display, YouTube Embedded Player

## Backend
- Language: Python
- Framework: Flask
- Hosting: TBD
- Responsibilities: YouTube Data API v3 communication, data processing, REST API

## External API
- Service: YouTube Data API v3
- Data retrieved: video ID, title, thumbnail, publish date, view count, video URL

## Endpoints
- GET /api/beats — latest 24 beats
- GET /api/beats/popular — top 5 beats by view count
- GET /api/health — backend availability check

## Data Flow
1. User opens the page
2. Frontend requests catalog from backend
3. Backend queries YouTube Data API
4. Backend processes and returns JSON
5. Frontend renders beat cards
6. User selects a beat
7. YouTube Embedded Player loads
