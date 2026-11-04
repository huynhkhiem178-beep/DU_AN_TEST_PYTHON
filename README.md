# Dự án kiểm thử và chấm điểm tự động Python

Dự án chia đề thi thành 13 file theo từng ý nhỏ. Mỗi file chạy độc lập (riêng Câu 5b import lớp từ Câu 5a).

## Cấu trúc
```text
submissions_de1/          # File sinh viên làm: Cau1a.py ... Cau5b.py
submissions_de1_dapan/    # 13 file đáp án mẫu để thử bộ chấm
tests/test_de1_pytest.py  # Kiểm tra đáp án mẫu
test_de1.py               # Dữ liệu kiểm thử input/output
autograde_de1.py          # Chương trình chấm điểm
cham_de_11301.bat
```

Không sử dụng các file gộp Cau1.py, Cau2.py, Cau3.py, Cau4.py, Cau5.py nữa.

## Danh sách file theo đề
| File | Nội dung |
|---|---|
| Cau1a.py | Nhập n, kiểm tra n thuộc [1, 1500] |
| Cau1b.py | Hàm con đếm chữ số lẻ của n |
| Cau1c.py | Hàm con tính S = 1/2 + 1/4 + ... + 1/(2n) |
| Cau2a.py | Đếm ký tự chữ hoa trong chuỗi |
| Cau2b.py | Kiểm tra chuỗi đối xứng |
| Cau2c.py | Tính tổng chữ số trong chuỗi |
| Cau3a.py | Nhập danh sách đến khi gặp 0 và in danh sách |
| Cau3b.py | Tính tổng số dương chẵn trong danh sách |
| Cau3c.py | Đếm số lần xuất hiện của k |
| Cau4a.py | Nhập thông tin sách, lưu vào từ điển |
| Cau4b.py | Tìm mã sách và xóa hoặc thông báo không tìm thấy |
| Cau5a.py | Định nghĩa lớp DienThoai |
| Cau5b.py | Tạo hai đối tượng điện thoại và gọi phương thức |

## Làm bài và chấm
Sinh viên chỉ sửa file trong `submissions_de1/`. Chạy từ thư mục gốc:
```powershell
py autograde_de1.py --student-id SV001
```
Thử bộ chấm bằng đáp án mẫu:
```powershell
py autograde_de1.py --student-id TEST --submissions submissions_de1_dapan
```
Mỗi câu 2 điểm. Câu 1–3 có 3 ý nên mỗi ý 2/3 điểm; Câu 4–5 có 2 ý nên mỗi ý 1 điểm. Tổng 10 điểm.

## Chạy Pytest
```powershell
py -m pip install -r requirements.txt
py -m pytest
```

## Quy ước nhập liệu cho autograder
Đề không mô tả chi tiết thứ tự nhập ở mọi ý, nên bộ chấm cần quy ước: Câu 3b nhập danh sách đến 0; Câu 3c nhập danh sách đến 0 rồi nhập k; Câu 4 nhập số lượng sách trước, sau đó từng trường mã/tên/tác giả/NXB/năm; Câu 5b import lớp từ `Cau5a.py`. Nếu giảng viên quy định định dạng khác, cần chỉnh test và đáp án mẫu theo đúng định dạng đó.
