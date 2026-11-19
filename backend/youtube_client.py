import requests

from config import YOUTUBE_API_KEY

YOUTUBE_API_BASE = "https://www.googleapis.com/youtube/v3"
CHANNEL_HANDLE = "@oscarmoralezz"


class YouTubeAPIError(Exception):
    pass


def _get(endpoint, params):
    if not YOUTUBE_API_KEY:
        raise YouTubeAPIError("YOUTUBE_API_KEY no está configurada en backend/.env.")

    try:
        response = requests.get(
            f"{YOUTUBE_API_BASE}/{endpoint}",
            params={**params, "key": YOUTUBE_API_KEY},
            timeout=10,
        )
    except requests.RequestException as exc:
        raise YouTubeAPIError(f"Error de red: {exc}") from exc

    if response.status_code != 200:
        raise YouTubeAPIError(
            f"YouTube respondió {response.status_code}: {response.text[:200]}"
        )

    return response.json()


def get_uploads_playlist_id():
    data = _get(
        "channels",
        {"part": "contentDetails", "forHandle": CHANNEL_HANDLE},
    )

    items = data.get("items", [])
    if not items:
        raise YouTubeAPIError(f"No se encontró el canal {CHANNEL_HANDLE}.")

    return items[0]["contentDetails"]["relatedPlaylists"]["uploads"]
