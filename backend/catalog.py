LATEST_LIMIT = 24
POPULAR_LIMIT = 5


def get_latest_beats(videos):
    ordered = sorted(videos, key=lambda v: v["publishedAt"], reverse=True)
    return ordered[:LATEST_LIMIT]


def get_popular_beats(videos):
    ordered = sorted(videos, key=lambda v: v["viewCount"], reverse=True)
    return ordered[:POPULAR_LIMIT]