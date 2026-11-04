"""Dap an tham khao Cau 2c."""
s = input("Nhap chuoi s: ")
tong = sum(int(ky_tu) for ky_tu in s if ky_tu.isdigit())
print("Tong cac chu so:", tong)
