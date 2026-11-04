"""Dap an tham khao Cau 3b."""
ds = []
while True:
    x = int(input("Nhap so nguyen (0 de dung): "))
    if x == 0:
        break
    ds.append(x)
tong = sum(x for x in ds if x > 0 and x % 2 == 0)
print("Tong cac so duong chan:", tong)
