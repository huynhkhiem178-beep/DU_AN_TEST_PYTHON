# Dự án kiểm thử và chấm điểm tự động Python

Dự án có hai cách kiểm thử bài Python:

- **Pytest:** chạy kiểm thử tự động cho các bài và chức năng.
- **Autograder dạng chạy file:** chạy từng file bài làm bằng Python, truyền dữ liệu vào `input()`, lấy nội dung `print()` để so sánh với kết quả mong đợi và tính điểm.

## 1. Cấu trúc chính

```text
DU_AN_TEST_PYTHON/
├── submissions_de1/
│   ├── Cau1.py
│   ├── Cau2.py
│   ├── Cau3.py
│   ├── Cau4.py
│   └── Cau5.py
├── tests/
│   ├── test_question_1_numbers.py
│   ├── test_question_2_strings.py
│   ├── test_question_3_lists.py
│   ├── test_question_4_dictionary.py
│   ├── test_question_5_oop.py
│   ├── test_autograder.py
│   └── test_de1_pytest.py
├── autograder/
│   ├── test_cases_de1.py
│   └── grade.py
├── src/
│   └── exam_tasks.py
├── test_de1.py
├── autograde_de1.py
├── cham_de_11301.bat
├── pytest.ini
└── requirements.txt
```

## 2. Đề 11301

Các file `submissions_de1/Cau1.py` đến `Cau5.py` là bài làm mẫu theo từng câu. Bộ test chạy file nằm trong `test_de1.py`.

| File | Nội dung |
|---|---|
| `Cau1.py` | Kiểm tra n, đếm chữ số lẻ và tính tổng phân số |
| `Cau2.py` | Xử lý chuỗi: đếm chữ hoa, kiểm tra đối xứng, tính tổng chữ số |
| `Cau3.py` | Danh sách số nguyên, dừng khi gặp 0, tính tổng và đếm phần tử |
| `Cau4.py` | Quản lý sách bằng từ điển, thêm và xóa sách |
| `Cau5.py` | Lập trình hướng đối tượng với lớp `DienThoai` |

**Lưu ý về dữ liệu đề:** PDF đã tải lên ở cuộc trò chuyện này không hiển thị được nội dung câu hỏi đủ rõ để đối chiếu. Vì vậy, các bài mẫu và test 11301 hiện tại được giữ theo bộ nội dung đã có trong dự án; riêng cách nhập dữ liệu cho câu 4 được quy ước trong phần chú thích của `test_de1.py`. Cần kiểm tra lại với đề gốc/giảng viên trước khi xem đây là bộ test chính thức.

## 3. Chạy chấm tự động theo kiểu file input/output

Mỗi câu là một file Python độc lập. Bộ chấm gọi file bằng chính Python đang cài trên máy, gửi dữ liệu qua stdin và kiểm tra stdout.

Từ thư mục gốc dự án, chạy:

```powershell
py autograde_de1.py --student-id SV001
```

Hoặc nhấp đúp file:

```text
cham_de_11301.bat
```

Muốn chấm bài khác, thay các file trong `submissions_de1/` bằng bài làm tương ứng và giữ nguyên tên `Cau1.py` ... `Cau5.py`.

## 4. Chạy Pytest

Cài thư viện:

```powershell
py -m pip install -r requirements.txt
```

Chạy toàn bộ test:

```powershell
py -m pytest
```

Chạy riêng bộ test dạng chạy file:

```powershell
py -m pytest tests/test_de1_pytest.py
```

## 5. Bộ chấm hoạt động như thế nào?

1. Đọc danh sách test trong `test_de1.py`.
2. Tìm file bài làm tương ứng trong `submissions_de1/`.
3. Chạy file bằng subprocess và truyền dữ liệu đầu vào.
4. So sánh các nội dung mong đợi với kết quả in ra.
5. Tính điểm từng câu tối đa 2 điểm, tổng tối đa 10 điểm.

Bộ chấm có giới hạn thời gian chạy cho mỗi test để tránh chương trình bị treo.

## 6. Cấu trúc cũ

Các thư mục `src/`, `autograder/` và những test cũ vẫn được giữ lại để không làm mất phần kiểm thử theo hàm/lớp đã xây dựng trước đó. Hai cách chấm có mục đích khác nhau:

- `py autograde_de1.py`: chấm chương trình tương tác qua input/output.
- `py -m autograder.grade submissions/de1/bai_lam.py --student-id SV001`: chấm trực tiếp hàm/lớp theo bộ test cũ.

## 7. Thêm đề mới

Khi có đề mới, tạo bộ dữ liệu test riêng, các file bài làm tương ứng và một script chấm riêng. Chỉ đưa test vào sử dụng khi đã đối chiếu nội dung đề và xác định rõ dữ liệu đầu vào/đầu ra mong đợi.
