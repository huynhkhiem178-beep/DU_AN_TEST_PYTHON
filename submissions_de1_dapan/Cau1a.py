"""Dap an tham khao Cau 1a."""
n = int(input("Nhap gia tri 1<=n<=1500: "))
while n < 1 or n > 1500:
    print("Gia tri khong hop le, nhap lai!")
    n = int(input("Nhap gia tri 1<=n<=1500: "))
print("n hop le:", n)
