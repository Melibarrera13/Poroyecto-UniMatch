"""Redis Configuration - UniMatch 2.0

Redis se utiliza para sesiones, caché y ranking.
Requiere: redis-py
"""

REDIS_CONFIG = {
    "host": "localhost",
    "port": 6379,
    "db": 0,
    "password": None
}

SESSION_TTL_SECONDS = 3600
CACHE_TTL_SECONDS = 600
TOKEN_TTL_SECONDS = 900
