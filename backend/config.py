import os

# La API Key se lee desde variable de entorno, nunca se escribe en el código.
YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", "")

# Origen del frontend permitido por CORS.
# Desarrollo: servidor local. Producción: dominio de GitHub Pages (se completará en T17).
ALLOWED_ORIGINS = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]