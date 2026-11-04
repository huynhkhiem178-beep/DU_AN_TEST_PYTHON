"""Cau 4 - De thi Python 11301.
Quy uoc dau vao de cham tu dong: nhap so luong sach, thong tin tung sach,
sau do nhap ma sach can xoa.
"""
def main():
    books = {}
    count = int(input("Nhap so luong sach: "))
    for _ in range(count):
        ma_so = input("Ma so sach: ")
        ten_sach = input("Ten sach: ")
        tac_gia = input("Ten tac gia: ")
        nha_xuat_ban = input("Nha xuat ban: ")
        nam_xuat_ban = int(input("Nam xuat ban: "))
        books[ma_so] = {
            "TenSach": ten_sach,
            "TenTacGia": tac_gia,
            "NhaXuatBan": nha_xuat_ban,
            "NamXuatBan": nam_xuat_ban,
        }

    print("Tu dien sach:", books)
    ma_can_xoa = input("Nhap ma sach can xoa: ")
    if ma_can_xoa in books:
        del books[ma_can_xoa]
        print("Da xoa sach:", ma_can_xoa)
    else:
        print("Khong tim thay cuon sach can xoa.")
    print("Tu dien sau khi xu ly:", books)

if __name__ == "__main__":
    main()
