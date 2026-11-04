"""Dap an tham khao Cau 1c."""
def S(n):
    s = 0
    for i in range(1, n + 1):
        s += 1 / (2 * i)
    return s

n = int(input("Nhap n: "))
print("S =", S(n))
