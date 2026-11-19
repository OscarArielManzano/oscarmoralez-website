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

def get_all_video_ids(playlist_id):
    video_ids = []
    page_token = None

    while True:
        params = {
            "part": "contentDetails",
            "playlistId": playlist_id,
            "maxResults": 50,
        }
        if page_token:
            params["pageToken"] = page_token

        data = _get("playlistItems", params)

        for item in data.get("items", []):
            video_id = item.get("contentDetails", {}).get("videoId")
            if video_id:
                video_ids.append(video_id)

        page_token = data.get("nextPageToken")
        if not page_token:
            break

    return video_ids


def get_videos_stats(video_ids):
    videos = []

    for start in range(0, len(video_ids), 50):
        batch = video_ids[start:start + 50]
        data = _get(
            "videos",
            {
                "part": "snippet,statistics",
                "id": ",".join(batch),
                "maxResults": 50,
            },
        )

        for item in data.get("items", []):
            snippet = item.get("snippet", {})
            statistics = item.get("statistics", {})
            video_id = item["id"]
            thumbnails = snippet.get("thumbnails", {})
            thumbnail = (
                thumbnails.get("high")
                or thumbnails.get("medium")
                or thumbnails.get("default")
                or {}
            ).get("url")

            videos.append({
                "id": video_id,
                "title": snippet.get("title", ""),
                "thumbnail": thumbnail,
                "publishedAt": snippet.get("publishedAt"),
                "viewCount": int(statistics.get("viewCount", 0)),
                "url": f"https://youtu.be/{video_id}",
            })

    return videos