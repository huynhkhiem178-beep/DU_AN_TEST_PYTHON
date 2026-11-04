"""Dap an tham khao Cau 2a."""
s = input("Nhap chuoi s: ")
dem = sum(1 for ky_tu in s if ky_tu.isupper())
print("So ky tu chu hoa:", dem)
