"""Dap an tham khao Cau 4a."""
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
print("Tu dien sach:", sach)
