from flask import Flask, jsonify
from flask_cors import CORS

from catalog import get_latest_beats, get_popular_beats
from config import ALLOWED_ORIGINS
from youtube_client import (
    YouTubeAPIError,
    get_all_video_ids,
    get_uploads_playlist_id,
    get_videos_stats,
)

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": ALLOWED_ORIGINS}})


def load_catalog():
    playlist_id = get_uploads_playlist_id()
    video_ids = get_all_video_ids(playlist_id)
    return get_videos_stats(video_ids)


@app.errorhandler(YouTubeAPIError)
def handle_youtube_error(error):
    return jsonify({"error": str(error)}), 502


@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


@app.route("/api/beats", methods=["GET"])
def beats():
    return jsonify(get_latest_beats(load_catalog())), 200


@app.route("/api/beats/popular", methods=["GET"])
def popular_beats():
    return jsonify(get_popular_beats(load_catalog())), 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)