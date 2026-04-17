# -*- coding: utf-8 -*-
"""
Agent đơn giản để demo Dockerfile cơ bản.
"""
import os
import time

from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from utils.mock_llm import ask
from fastapi.responses import JSONResponse

app = FastAPI(title="Agent Basic Docker")
START_TIME = time.time()


# 1. Define the request body model using Pydantic
class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def root():
    return {"message": "Agent is running in a Docker container!"}


# 2. Update the endpoint to use the Pydantic model
@app.post("/ask")
async def ask_agent(request: QuestionRequest):
    answer = ask(request.question)
    return JSONResponse(content={"answer": answer}, media_type="application/json; charset=utf-8")


@app.get("/health")# ============================================================
# Dockerfile ở thư mục gốc - Tương thích với Railway
# ============================================================

# Bước 1: Chọn base image
FROM python:3.11

# Install locale support and configure UTF-8
RUN apt-get update && apt-get install -y locales && \
    sed -i '/vi_VN.UTF-8/s/^# //g' /etc/locale.gen && \
    locale-gen vi_VN.UTF-8

# Bước 2: Đặt working directory trong container
WORKDIR /app

# Set UTF-8 environment để tránh lỗi font tiếng Việt
ENV PYTHONIOENCODING=utf-8
ENV LANG=vi_VN.UTF-8
ENV LC_ALL=vi_VN.UTF-8
ENV PYTHONUTF8=1

# Bước 3: Copy requirements TRƯỚC (từ thư mục con)
COPY 02-docker/develop/requirements.txt .

# Bước 4: Cài dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Bước 5: Copy code vào container
# Copy app.py và thư mục utils
COPY 02-docker/develop/app.py .
COPY utils ./utils

# Bước 6: Expose port
EXPOSE 8000

# Bước 7: Command mặc định khi container start
# Chạy app.py từ thư mục /app
CMD ["python", "app.py"]

def health():
    return {
        "status": "ok",
        "uptime_seconds": round(time.time() - START_TIME, 1),
        "container": True,
    }


if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app="app:app", host="0.0.0.0", port=port)