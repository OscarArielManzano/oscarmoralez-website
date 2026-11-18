# DECISIONS

## Confirmed Decisions

### Frontend
- Vanilla HTML5, CSS3, JavaScript — no frameworks
- Single-page portfolio website
- GitHub Pages for hosting

### Backend
- Python + Flask
- No database — in-memory cache only
- REST API with JSON responses
- CORS configured for GitHub Pages domain

### Music
- YouTube Data API v3 for metadata
- YouTube Embedded Player for playback
- No audio file hosting or downloads

### Content
- Latest 24 beats from channel
- Top 5 beats by view count (full catalog pagination)
- One featured collaboration: Oscar Moralez x AP Wizard

### Security
- API Key stored in environment variable
- API Key never exposed in frontend files
- HTTPS required in production

## Pending Decisions
- Backend hosting service
- Repository name: oscarmoralez-website (confirmed by user)
