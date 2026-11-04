"""Cau 3 - De thi Python 11301.
Nhap danh sach so nguyen, dung khi nhap 0.
"""
def main():
    numbers = []
    while True:
        try:
            value = int(input("Nhap phan tu (0 de dung): "))
        except ValueError:
            print("Vui long nhap so nguyen!")
            continue
        if value == 0:
            break
        numbers.append(value)

    print("Danh sach:", numbers)
    print("Tong so duong chan:", sum(x for x in numbers if x > 0 and x % 2 == 0))
    k = int(input("Nhap k can dem: "))
    print("So lan xuat hien cua k:", numbers.count(k))

if __name__ == "__main__":
    main()
