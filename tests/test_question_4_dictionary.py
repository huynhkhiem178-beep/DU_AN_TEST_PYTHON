from datetime import date
import pytest
from src.exam_tasks import add_book, delete_book

def test_add_book_stores_all_information():
    books = {}
    add_book(books, "S01", "Dế Mèn Phiêu Lưu Ký", "Tô Hoài", "Kim Đồng", 1941)
    assert books["S01"] == {
        "ten_sach": "Dế Mèn Phiêu Lưu Ký",
        "ten_tac_gia": "Tô Hoài",
        "nha_xuat_ban": "Kim Đồng",
        "nam_xuat_ban": 1941,
    }

def test_add_book_updates_existing_code():
    books = {"S01": {"ten_sach": "Cũ"}}
    add_book(books, "S01", "Mới", "Tác giả", "NXB", 2020)
    assert books["S01"]["ten_sach"] == "Mới"
    assert len(books) == 1

def test_add_book_rejects_empty_code():
    with pytest.raises(ValueError):
        add_book({}, "", "Tên", "Tác giả", "NXB", 2020)

@pytest.mark.parametrize("year", [0, date.today().year + 1])
def test_add_book_rejects_invalid_year(year):
    with pytest.raises(ValueError):
        add_book({}, "S02", "Tên", "Tác giả", "NXB", year)

def test_add_book_rejects_non_integer_year():
    with pytest.raises(TypeError):
        add_book({}, "S02", "Tên", "Tác giả", "NXB", "2020")

def test_delete_existing_book():
    books = {"S01": {"ten_sach": "Python"}}
    assert delete_book(books, "S01") is True
    assert "S01" not in books

def test_delete_missing_book_keeps_dictionary_unchanged():
    books = {"S01": {"ten_sach": "Python"}}
    assert delete_book(books, "S99") is False
    assert "S01" in books
