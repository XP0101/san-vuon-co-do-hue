# Sân Vườn Cố Đô

Website tiếng Việt gồm 15 trang HTML độc lập, CSS/JavaScript/ảnh SVG được nhúng vào từng trang. Không cần npm hay framework để chạy bản xuất.

## Xem website

Mở `dist/index.html` trực tiếp hoặc chạy từ thư mục này:

```sh
python3 -m http.server 4173 --directory dist
```

Sau đó truy cập http://localhost:4173.

## Chỉnh sửa và tạo lại bản xuất

- `build.py`: nội dung, dữ liệu, mẫu HTML, ảnh minh họa SVG và SEO.
- `src/style.css`: hệ thống thiết kế và bố cục responsive.
- `src/app.js`: menu, bộ lọc, carousel, gallery và form.
- `dist/`: 15 HTML, sitemap.xml, robots.txt; đây là thư mục để triển khai.

```sh
python3 build.py
python3 check.py
node --check src/app.js
```

Các thay đổi trực tiếp trong `dist/` sẽ bị ghi đè khi tạo lại bản xuất.

## Tính năng

- Trang chủ, dịch vụ, danh sách dự án, 5 hồ sơ dự án, giới thiệu, liên hệ.
- 3 bài viết, chính sách bảo mật và điều khoản sử dụng.
- 12 thẻ dự án: 5 hồ sơ và 7 ý tưởng mẫu; lọc danh mục kết hợp tải thêm.
- Gallery 6 ảnh mỗi hồ sơ, đóng bằng Escape, điều hướng bằng phím mũi tên, hoàn trả focus.
- Carousel điều khiển bằng vuốt hoặc chấm điều hướng, không tự chuyển và không có nút pause.
- Form kiểm tra dữ liệu, yêu cầu đồng ý và soạn email với nội dung đã mã hóa.
- SEO tiếng Việt, canonical, Open Graph, JSON-LD, sitemap và robots.
- Menu di động, điều hướng bàn phím, skip link, Zalo và gọi điện.

## Các cấu hình cần xác nhận khi vận hành thật

1. **Tiếp nhận tư vấn:** hiện là website tĩnh. Form không lưu hoặc tự gửi dữ liệu tới máy chủ; khách cần mở email rồi nhấn gửi. Không có thông báo giả “đã gửi thành công”. Muốn nhận tự động cần tích hợp endpoint có xác thực dữ liệu, chống thư rác và chính sách lưu trữ thích hợp.
2. **Tên miền và email:** bản yêu cầu chứa ký tự `о` Cyrillic ở cuối `sanvuoncodо.vn`. Đã chuẩn hóa thành ASCII `sanvuoncodo.vn` để tránh địa chỉ nhìn giống nhưng khác tên miền. Chưa xác minh quyền sở hữu tên miền hoặc hộp thư. Thay `DOMAIN` trong `build.py` và địa chỉ email trong nguồn nếu cần.
3. **Dữ liệu mẫu:** số liệu và đánh giá lấy từ yêu cầu; thông số mở rộng của dự án là minh họa. Các trang dự án và đánh giá có ghi chú mẫu. Xác nhận nội dung trước khi dùng để quảng bá thực tế.
4. **Ảnh:** SVG gradient được nhúng, không có tài nguyên ảnh bị thiếu. Để dùng ảnh thực, thêm tệp vào `dist/images` sau khi build, đặt `data-src` thành đường dẫn tương ứng hoặc chỉnh hàm `img()` trước khi build. `data-image-path` ghi đường dẫn dự kiến. Ảnh lỗi sẽ giữ minh họa hiện tại.
5. **Mạng xã hội:** Zalo sử dụng số điện thoại trong yêu cầu. Facebook và YouTube chưa có URL chính thức nên hiện thông báo cập nhật thay vì dẫn tới tài khoản không xác định.
6. **Phông chữ:** tải Google Fonts khi có mạng; có phông hệ thống dự phòng khi ngoại tuyến.
7. **Triển khai:** cấu hình Sites nằm trong `.openai/hosting.json`, bản đăng riêng tư chỉ chủ sở hữu truy cập. Canonical/sitemap vẫn dùng tên miền doanh nghiệp dự kiến, chưa có kết nối tên miền riêng.

## Kiểm tra đã thực hiện

- 15 trang có đúng 1 H1, không trùng ID, JSON-LD hợp lệ, ảnh có alt.
- 518 liên kết nội bộ và neo trang không bị thiếu đích.
- JavaScript qua kiểm tra cú pháp Node.
- Trình duyệt: bộ lọc Hồ cá 2/2, tải thêm 12/12, gallery chuyển ảnh và Escape, lỗi form bắt buộc, soạn email hợp lệ, menu di động.
- Kiểm tra tràn ngang tại 1440px và 390px; chưa thực hiện kiểm toán WCAG đầy đủ hoặc kiểm tra trên thiết bị iOS/Android thật.

## Nhận diện và khả năng đọc

- Logo gốc ở `src/assets/logo.jpeg`, được nhúng vào HTML để từng trang vẫn mở độc lập.
- Bảng màu mới: xanh đậm `#1C4332`, xanh chủ đạo `#28513D`, ô-liu `#7F965C`, màu nút sáng `#B5C78E`, nền `#F8F9F3`.
- Nội dung chính 18px, nút 17px, thông tin phụ thường 16px; khoảng cách dòng 1.8–1.9.
- Điện thoại dùng một cột cho dịch vụ/dự án; lời giới thiệu được rút gọn và nút đầu trang gọi trực tiếp.
- Kiểm tra trình duyệt ở 390px và 1440px: không tràn ngang, logo tải đúng, điều hướng không chồng nhau. Khối bài viết chứa đủ nội dung và cách phần liên hệ 64px trên điện thoại.


## Ảnh thật ở phần mở đầu

- Ảnh nền lối dạo nhiệt đới: GH Ang, Unsplash, https://unsplash.com/photos/-xk0f3eLStA
- Ảnh trong khung vòm: Annie Spratt, Unsplash, https://unsplash.com/photos/ezmI-TtoQbc
- Hai ảnh miễn phí theo Unsplash License, dùng làm ảnh truyền cảm hứng cho giao diện, không phải ảnh công trình của công ty. Bản tải được lưu trong `src/assets/` và nhúng vào trang chủ; không phụ thuộc hotlink.


### Thay ảnh bìa sáng hơn

- Nền toàn cảnh hồ và đồi cỏ: Arinal Izzah, https://unsplash.com/photos/00DjNGJqkVk
- Khung vòm hồ thủy sinh, thác nước và cầu đá: Sascha Braun, https://unsplash.com/photos/6Clxp6DDXXo
- Ảnh dùng theo Unsplash License. Bản hiện tại dùng hai ảnh này thay cho hai ảnh ở mục trước. Lớp phủ bên phải giảm còn 4–15%, phần chữ bên trái 51–72% để giữ độ tương phản.


### Ảnh khung vòm mang nét Huế

Khung vòm hiện dùng ảnh chụp tại Huế của Florian Delée: https://unsplash.com/photos/bSErx3YI4Rc (Unsplash License). Ảnh ở `src/assets/vuon-hue.jpg`, gồm cây cảnh, non bộ, cầu cong và kiến trúc mái ngói. Đây là ảnh tạo cảm hứng, không được giới thiệu là công trình của công ty. Nền toàn cảnh hồ sáng giữ nguyên.


### Ảnh khung vòm hiện tại: hồ sen Huế

Ảnh hồ sen trước kiến trúc truyền thống tại Huế của Florian Delée: https://unsplash.com/photos/a2e4rXtXDGI, dùng theo Unsplash License. Tệp `src/assets/ho-sen-hue.jpg` thay cho ảnh vườn trước đó; dùng làm ảnh truyền cảm hứng.
