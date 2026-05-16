"""Redis Connection - UniMatch 2.0"""

import redis
from src.config.redis_config import REDIS_CONFIG


class RedisConnection:

    @staticmethod
    def get_client():
        return redis.Redis(
            host=REDIS_CONFIG["host"],
            port=REDIS_CONFIG["port"],
            db=REDIS_CONFIG["db"],
            password=REDIS_CONFIG["password"],
            decode_responses=True
        )
