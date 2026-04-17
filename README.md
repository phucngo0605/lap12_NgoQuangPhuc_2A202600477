# Lab 12: API Gateway - Production Readiness

Dự án này triển khai một API Gateway hoàn chỉnh, sẵn sàng cho môi trường production, đóng vai trò là cổng vào cho một dịch vụ AI.

## Các tính năng chính

- **Xác thực qua API Key**: Bảo vệ endpoint, chỉ những ai có key hợp lệ mới được truy cập.
- **Giám sát chi phí (Cost Guard)**: Theo dõi và giới hạn chi phí sử dụng dịch vụ AI, tránh vượt ngân sách.
- **Giới hạn tần suất (Rate Limiting)**: Chống lạm dụng API và tấn công DoS.
- **Bộ nhớ đệm (Caching)**: Giảm chi phí và cải thiện tốc độ phản hồi cho các câu hỏi lặp lại.
- **Kiểm tra "sức khỏe" (Health Check)**: Cung cấp endpoint `/health` để các hệ thống giám sát có thể kiểm tra trạng thái dịch vụ.
- **Kiến trúc Stateless**: Sử dụng Redis làm nơi lưu trữ trạng thái chung, cho phép mở rộng theo chiều ngang (horizontal scaling) một cách dễ dàng.
- **Container hóa**: Toàn bộ ứng dụng được đóng gói bằng Docker và Docker Compose để triển khai đồng nhất và dễ dàng.

## Công nghệ sử dụng

- **FastAPI**: Framework web hiệu năng cao của Python.
- **Redis**: Datastore trong bộ nhớ, được sử dụng cho Caching, Rate Limiting, và Cost Guard.
- **Docker & Docker Compose**: Dành cho việc container hóa và điều phối các dịch vụ.
- **Gunicorn**: Production-grade WSGI server để chạy ứng dụng FastAPI.

## Hướng dẫn cài đặt và chạy dự án

### Yêu cầu

- Đã cài đặt Docker
- Đã cài đặt Docker Compose

### Các bước thực hiện

1.  **Tải mã nguồn về:**
    ```bash
    git clone <repository-url>
    cd <repository-folder>
    ```

2.  **Tạo file biến môi trường:**
    - Sao chép file `.env.example` thành một file mới tên là `.env`.
      ```bash
      # Trên Windows (Command Prompt)
      copy .env.example .env
      ```
    - Mở file `.env` và điền các giá trị API key thật của bạn:
      ```ini
      # API Gateway Security Key
      API_KEY="your-strong-api-key"

      # OpenAI API Key
      OPENAI_API_KEY="sk-your-openai-key"
      ```

3.  **Khởi chạy ứng dụng:**
    - Sử dụng Docker Compose để build và chạy các dịch vụ ở chế độ nền.
      ```bash
      docker-compose up --build -d
      ```
    - API Gateway sẽ chạy và có thể truy cập tại `http://localhost:8001`.

4.  **Kiểm tra các dịch vụ:**
    - Kiểm tra xem các container đã chạy thành công hay chưa:
      ```bash
      docker-compose ps
      ```
    - Bạn sẽ thấy 2 dịch vụ là `api-gateway` và `redis` đều đang ở trạng thái `running`.

## Cách sử dụng

Gửi một request POST đến endpoint `/ask` với API key và câu hỏi của bạn.

```bash
curl -X POST "http://localhost:8001/ask" \
-H "Content-Type: application/json" \
-H "X-API-Key: your-strong-api-key" \
-d '{"question": "What is Docker?"}'
```

## Dừng ứng dụng

Để dừng tất cả các dịch vụ, chạy lệnh:
```bash
docker-compose down
```
````

Sau khi bạn tạo xong 2 file này, chúng ta chỉ còn một file cuối cùng là `DEPLOYMENT.md`