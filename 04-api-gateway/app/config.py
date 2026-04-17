# -*- coding: utf-8 -*-
"""
File cấu hình tập trung cho toàn bộ ứng dụng.
"""
import os
from dotenv import load_dotenv

# Tải các biến môi trường từ file .env
load_dotenv()

# === API Key Settings ===
# Lấy API key từ biến môi trường
AGENT_API_KEY = os.getenv("AGENT_API_KEY")

# === Rate Limiting Settings ===
# Giới hạn 10 request mỗi 60 giây
RATE_LIMIT_REQUESTS = 10
RATE_LIMIT_PERIOD_SECONDS = 60

# === Cost Guard Settings ===
# Ngân sách tối đa là $10
BUDGET = 10.0

# === Redis Settings ===
# Đọc các biến môi trường từ Railway, nếu không có thì dùng giá trị mặc định cho docker-compose
REDIS_HOST = os.getenv("REDISHOST", "redis")
REDIS_PORT = int(os.getenv("REDISPORT", 6379))
REDIS_PASSWORD = os.getenv("REDISPASSWORD", None)

# === Caching Settings ===
# Thời gian cache là 1 giờ (3600 giây)
CACHE_EXPIRATION_SECONDS = 3600