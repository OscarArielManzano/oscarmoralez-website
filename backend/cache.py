import time

DEFAULT_TTL_SECONDS = 30 * 60


class MemoryCache:
    def __init__(self, ttl_seconds=DEFAULT_TTL_SECONDS):
        self.ttl_seconds = ttl_seconds
        self._value = None
        self._expires_at = 0.0

    def get(self):
        if self._value is None or time.time() >= self._expires_at:
            return None
        return self._value

    def set(self, value):
        self._value = value
        self._expires_at = time.time() + self.ttl_seconds


catalog_cache = MemoryCache()