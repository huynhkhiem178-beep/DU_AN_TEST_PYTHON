"""Cau 1 - De thi Python 11301.
Nhap so nguyen duong n trong [1, 1500], dem chu so le va tinh S.
"""
def main():
    while True:
        try:
            n = int(input("Nhap n (1..1500): "))
            if 1 <= n <= 1500:
                break
            print("n phai nam trong doan [1, 1500]. Nhap lai!")
        except ValueError:
            print("Vui long nhap so nguyen!")

    count_odd = sum(1 for ch in str(n) if int(ch) % 2 == 1)
    total = sum(1 / (2 * i) for i in range(1, n + 1))
    print("So luong chu so le:", count_odd)
    print("Tong S:", total)

if __name__ == "__main__":
    main()
