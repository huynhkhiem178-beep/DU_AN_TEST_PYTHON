"""Dap an tham khao Cau 3c."""
ds = []
while True:
    x = int(input("Nhap so nguyen (0 de dung): "))
    if x == 0:
        break
    ds.append(x)
k = int(input("Nhap k: "))
print("So lan xuat hien cua k:", ds.count(k))
