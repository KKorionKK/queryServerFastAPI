import redis
from api.settings import get_settings

settings = get_settings()

r = redis.asyncio.Redis(
    host=settings.HOST,
    port=settings.PORT,
    password=settings.PASSWORD,
)
