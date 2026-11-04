"""Test input/output cho de 11301.
Cau 1 duoc tach thanh 1a, 1b, 1c. Tong diem Cau 1 la 2 diem,
chia deu cho ba y. Moi cau 2-5 toi da 2 diem.
"""
tests = {
    "Cau1a": [
        {"input": "635\n", "expected": ["n hop le:", "635"]},
        {"input": "0\n1501\n12\n", "expected": ["nhap lai!", "n hop le:", "12"]},
    ],
    "Cau1b": [
        {"input": "635\n", "expected": ["so luong chu so le la:", "2"]},
        {"input": "468\n", "expected": ["so luong chu so le la:", "0"]},
    ],
    "Cau1c": [
        {"input": "1\n", "expected": ["s =", "0.5"]},
        {"input": "2\n", "expected": ["s =", "0.75"]},
    ],
    "Cau2": [
        {"input": "Abc123\n", "expected": ["So ky tu chu hoa:", "1", "Chuoi doi xung:", "False", "Tong cac chu so:", "6"]},
        {"input": "madam\n", "expected": ["So ky tu chu hoa:", "0", "Chuoi doi xung:", "True", "Tong cac chu so:", "0"]},
        {"input": "A1B2\n", "expected": ["So ky tu chu hoa:", "2", "Tong cac chu so:", "3"]},
    ],
    "Cau3": [
        {"input": "2\n-3\n4\n0\n2\n", "expected": ["Danh sach:", "[2, -3, 4]", "Tong so duong chan:", "6", "So lan xuat hien cua k:", "1"]},
        {"input": "0\n5\n", "expected": ["Danh sach:", "[]", "Tong so duong chan:", "0", "So lan xuat hien cua k:", "0"]},
    ],
    "Cau4": [
        {"input": "2\nS01\nDe Men Phieu Luu Ky\nTo Hoai\nKim Dong\n1941\nS02\nPython Co Ban\nNguyen Van A\nNXB Tre\n2020\nS01\n", "expected": ["Tu dien sach:", "S01", "S02", "Da xoa sach:", "Tu dien sau khi xu ly:", "S02"]},
        {"input": "1\nS01\nSach mau\nTac gia mau\nNXB Tre\n2020\nS99\n", "expected": ["Khong tim thay cuon sach can xoa.", "S01"]},
    ],
    "Cau5": [
        {"input": "", "expected": ["DT01", "iPhone 15 Pro", "Apple", "3274", "28990000", "DT02", "Galaxy S24 Ultra", "Samsung", "5000", "29990000"]},
    ],
}
