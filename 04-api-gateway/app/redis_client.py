import redis
from app.config import REDIS_HOST, REDIS_PORT, REDIS_PASSWORD

# Tạo một instance của Redis client.
# decode_responses=True giúp chúng ta nhận được dữ liệu dạng string thay vì bytes.
# Thêm password=REDIS_PASSWORD để xác thực với Redis trên Railway.
redis_client = redis.Redis(
    host=REDIS_HOST, 
    port=REDIS_PORT, 
    password=REDIS_PASSWORD,
    db=0, 
    decode_responses=True
)