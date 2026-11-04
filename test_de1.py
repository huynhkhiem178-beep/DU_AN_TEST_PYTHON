"""Du lieu test cho de thi Python ma 11301.

Moi cau 2 diem. Moi test case co stdin va cac chuoi can tim trong stdout.
Voi cau 4, quy uoc dau vao la: so luong sach -> thong tin tung sach
(ma, ten, tac gia, nha xuat ban, nam) -> ma sach can xoa.
"""
tests = {
    "Cau1": [
        {"input": "635\n", "expected": ["So luong chu so le:", "2", "Tong S:"]},
        {"input": "468\n", "expected": ["So luong chu so le:", "0", "Tong S:"]},
        {"input": "0\n1501\n12\n", "expected": ["Nhap lai!", "So luong chu so le:", "1"]},
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
