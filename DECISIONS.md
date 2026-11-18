# DECISIONS

## Confirmed Decisions

### Repository
- Name: oscarmoralez-website
- Platform: GitHub
- Frontend deployment: GitHub Pages

### Frontend
- Vanilla HTML5, CSS3, JavaScript — no frameworks
- Single-page portfolio website
- Fetch API for backend communication
- YouTube Embedded Player via iframe

### Backend
- Python 3.13 + Flask 3.1.3
- No database — in-memory cache only
- REST API with JSON responses
- CORS configured for GitHub Pages domain
- Dependencies: flask, requests, flask-cors

### YouTube Integration
- YouTube Data API v3 for metadata
- Full catalog pagination via playlistItems.list
- Batch stats retrieval via videos.list (max 50 IDs per request)
- Latest 24 beats ordered by publish date
- Top 5 beats ordered by view count across full catalog
- YouTube Embedded Player for playback — no audio file hosting

### Content
- One featured collaboration: Oscar Moralez x AP Wizard
- Featured video: https://youtu.be/CCFZr7MRrYU
- Contact via Instagram DM only

### Security
- API Key stored in environment variable
- API Key never exposed in frontend files
- HTTPS required in production

### Exclusions (MVP)
- No user authentication
- No database
- No admin panel
- No payment system
- No beat store
- No audio file hosting or downloads
- No contact forms with storage

## Pending Decisions
- Backend hosting service
