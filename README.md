# Giá vàng hôm nay

Trang giá vàng/bạc thế giới quy đổi VNĐ cho hoc3giay.com, chạy trên GitHub Pages.

- `index.html`: trang hiển thị (bảng giá, biểu đồ, máy tính quy đổi, lãi/lỗ, tỷ giá).
- `data/history.json`: lịch sử giá, do GitHub Actions cập nhật 30 phút/lần.
- `scripts/update.py`: script lấy giá và thêm 1 điểm vào lịch sử.
- `.github/workflows/update.yml`: lịch chạy tự động.
- `nhung-vao-wordpress.html`: đoạn mã dán vào khối "HTML tùy chỉnh" của WordPress.

Nguồn dữ liệu: gold-api.com (giá kim loại), ExchangeRate-API (tỷ giá).
Giá là giá thế giới quy đổi, chỉ để tham khảo, không phải lời khuyên đầu tư.
