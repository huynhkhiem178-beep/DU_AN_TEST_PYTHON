"""DAP AN THAM KHAO - CAU 3, de 11301."""
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
