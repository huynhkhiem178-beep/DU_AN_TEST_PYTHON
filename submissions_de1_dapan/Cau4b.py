"""Dap an tham khao Cau 4b."""
sach = {}
n = int(input("Nhap so luong sach: "))
for _ in range(n):
    ma = input("Ma so sach: ")
    ten = input("Ten sach: ")
    tac_gia = input("Ten tac gia: ")
    nxb = input("Nha xuat ban: ")
    nam = input("Nam xuat ban: ")
    sach[ma] = {
        "TenSach": ten,
        "TenTacGia": tac_gia,
        "NhaXuatBan": nxb,
        "NamXuatBan": nam,
    }
ma_can_xoa = input("Nhap ma sach can xoa: ")
if ma_can_xoa in sach:
    del sach[ma_can_xoa]
    print("Da xoa cuon sach:", ma_can_xoa)
else:
    print("Khong tim thay cuon sach can xoa")
print("Tu dien sau khi xu ly:", sach)
