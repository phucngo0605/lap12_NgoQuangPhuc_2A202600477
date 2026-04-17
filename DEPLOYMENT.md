# Thông tin Triển khai trên Railway

Dự án này đã được triển khai thành công lên nền tảng Railway.

## URL của Dịch vụ

- **API Gateway**: [https://lap12-production.up.railway.app](https://lap12-production.up.railway.app)

## Thông tin Dịch vụ

- **Nền tảng**: Railway
- **Phương thức triển khai**: Kết nối với kho chứa GitHub và tự động triển khai khi có commit mới vào nhánh `main`.
- **Dockerfile sử dụng**: `04-api-gateway/Dockerfile.prod`
- **Cổng dịch vụ**: Ứng dụng chạy trên cổng `8000` bên trong container và Railway tự động expose ra ngoài qua cổng `443` (HTTPS).

## Biến môi trường

Các biến môi trường sau đã được cấu hình trên dịch vụ của Railway:

- `API_KEY`: API key để xác thực với Gateway.
- `OPENAI_API_KEY`: API key của dịch vụ OpenAI.
- `REDIS_HOST`: Tên dịch vụ Redis do Railway cung cấp.
- `REDIS_PORT`: Cổng của dịch vụ Redis.
- `REDIS_PASSWORD`: Mật khẩu của dịch vụ Redis.

## Kiểm tra "sức khỏe"

Có thể kiểm tra trạng thái của dịch vụ bằng cách truy cập vào endpoint `/health`.

- **URL Health Check**: [https://lap12-production.up.railway.app/health](https://lap12-production.up.railway.app/health)

Nếu kết quả trả về là `{"status": "ok"}`, dịch vụ đang hoạt động bình thường.