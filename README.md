# Dự án kiểm thử và chấm điểm tự động Python

Dự án có hai phần:
- **Pytest:** kiểm thử các hàm Python theo từng câu của đề.
- **Autograder:** chạy bộ test đã định nghĩa, đối chiếu kết quả và tính điểm trên thang 10.

Bộ câu hỏi hiện có được xây dựng theo nội dung đề mã **11301** đã dùng trong dự án. Mỗi câu tối đa 2 điểm.

## 1. Cấu trúc thư mục

```text
DU_AN_TEST_PYTHON/
├── src/
│   ├── __init__.py
│   └── exam_tasks.py
├── tests/
│   ├── test_question_1_numbers.py
│   ├── test_question_2_strings.py
│   ├── test_question_3_lists.py
│   ├── test_question_4_dictionary.py
│   ├── test_question_5_oop.py
│   └── test_autograder.py
├── autograder/
│   ├── __init__.py
│   ├── test_cases_de1.py
│   └── grade.py
├── submissions/
│   ├── de1/
│   └── de2/
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

## 2. Nội dung đề 11301

| Câu | Nội dung |
|---|---|
| 1 | Kiểm tra số nguyên, đếm chữ số lẻ, tính tổng phân số |
| 2 | Xử lý chuỗi: đếm chữ hoa, kiểm tra đối xứng, tính tổng chữ số |
| 3 | Xử lý danh sách: dừng khi gặp 0, tổng số dương chẵn, đếm phần tử |
| 4 | Quản lý sách bằng từ điển, thêm và xóa theo mã |
| 5 | Lập trình hướng đối tượng với lớp `DienThoai` |

## 3. Cài đặt trên Windows

Mở PowerShell tại thư mục dự án:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Không bắt buộc phải kích hoạt môi trường ảo.

## 4. Chạy Pytest

Chạy toàn bộ kiểm thử:

```powershell
.\.venv\Scripts\python.exe -m pytest -v
```

Chạy riêng một câu:

```powershell
.\.venv\Scripts\python.exe -m pytest tests/test_question_1_numbers.py
```

## 5. Chấm tự động bài làm

1. Đặt file bài làm của sinh viên trong thư mục tương ứng, ví dụ `submissions/de1/bai_lam.py`.
2. File bài làm cần định nghĩa các hàm/lớp có tên, tham số và kiểu kết quả tương ứng với các mục trong `src/exam_tasks.py`.
3. Chạy lệnh từ thư mục gốc:

```powershell
.\.venv\Scripts\python.exe -m autograder.grade submissions/de1/bai_lam.py --student-id SV001
```

Chương trình sẽ:
- Chạy từng test case trong bộ dữ liệu đề 01.
- Hiển thị PASS hoặc FAIL cho từng test.
- Tính điểm từng câu theo tỉ lệ test đúng.
- Cộng điểm 5 câu, tối đa 10 điểm.

**Lưu ý:** Bộ chấm hiện tại gọi trực tiếp hàm/lớp trong file bài làm và kiểm tra giá trị trả về. Nó chưa mô phỏng nhập liệu từ bàn phím hoặc chấm nội dung in ra màn hình như script mẫu dạng `subprocess`.

## 6. Thêm đề mới

- Tạo file dữ liệu kiểm thử riêng trong thư mục `autograder/`.
- Mỗi test case cần có tên hàm, tham số đầu vào và kết quả mong đợi.
- Chỉ thêm đáp án khi có nội dung đề và đáp án đáng tin cậy. Thư mục `submissions/de2/` hiện là nơi đặt bài làm; chưa có bộ test đề 02 được xác nhận.

## 7. Ghi chú

Công thức câu 1c đang được hiểu là `1/2 + 1/4 + ... + 1/(2n)` theo cách diễn giải đã dùng khi xây dựng phiên bản trước. Cần đối chiếu lại với đề/đáp án gốc nếu giảng viên yêu cầu chính xác tuyệt đối.
