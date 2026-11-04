"""Cau 2 - De thi Python 11301.
Nhap chuoi, dem chu hoa, kiem tra doi xung va tinh tong chu so.
"""
def main():
    s = input("Nhap chuoi s: ")
    uppercase_count = sum(1 for ch in s if ch.isupper())
    digit_sum = sum(int(ch) for ch in s if ch.isdigit())
    print("So ky tu chu hoa:", uppercase_count)
    print("Chuoi doi xung:", s == s[::-1])
    print("Tong cac chu so:", digit_sum)

if __name__ == "__main__":
    main()
