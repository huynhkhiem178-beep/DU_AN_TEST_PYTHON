# Dự án kiểm thử Python bằng Pytest

Dự án xây dựng bộ kiểm thử tự động cho **đề thi kết thúc môn Lập trình Python – mã đề 11301**. Nội dung được chia thành 5 nhóm tương ứng 5 câu trong đề.

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
│   └── test_question_5_oop.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

## 2. Nội dung kiểm thử

| File kiểm thử | Nội dung đề thi |
|---|---|
| `test_question_1_numbers.py` | Kiểm tra n trong [1, 1500], đếm chữ số lẻ, tính S = 1/2 + 1/4 + ... + 1/(2n) |
| `test_question_2_strings.py` | Đếm chữ hoa, kiểm tra chuỗi đối xứng, tính tổng chữ số trong chuỗi |
| `test_question_3_lists.py` | Nhập danh sách đến số 0, tổng số dương chẵn, đếm số lần xuất hiện |
| `test_question_4_dictionary.py` | Thêm thông tin sách, kiểm tra năm xuất bản, xóa sách theo mã |
| `test_question_5_oop.py` | Khởi tạo đối tượng `DienThoai`, kiểm tra thuộc tính và nội dung hiển thị |

## 3. Cài đặt trên Windows

Mở Terminal tại thư mục dự án và chạy:

```bash
py -m venv .venv
.venv\\Scripts\\activate
py -m pip install -r requirements.txt
```

## 4. Chạy kiểm thử

Chạy toàn bộ bài kiểm thử:

```bash
py -m pytest
```

Chạy riêng một câu, ví dụ câu 1:

```bash
py -m pytest tests/test_question_1_numbers.py
```

Chạy và xem kết quả ngắn gọn:

```bash
py -m pytest -q
```

## 5. Ý nghĩa kết quả

- `PASSED`: hàm đáp ứng trường hợp kiểm thử.
- `FAILED`: kết quả thực tế khác kết quả mong đợi hoặc phát sinh lỗi không mong muốn.
- `ERROR`: lỗi trong quá trình thiết lập/chạy kiểm thử.
- `skipped`: trường hợp được chủ động bỏ qua.

## 6. Ghi chú về đề

Câu 1c trong đáp án đính kèm được hiểu là tổng `1/(2*i)` với `i` chạy từ 1 đến `n`. Chuỗi đối xứng được kiểm tra đúng theo phép so sánh chuỗi gốc với chuỗi đảo ngược (phân biệt chữ hoa/chữ thường). Các hàm được tách riêng để dễ kiểm thử; phần nhập/xuất bàn phím có thể xây dựng thành giao diện riêng sau này.
