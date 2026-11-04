"""DAP AN THAM KHAO - CAU 5, de 11301."""
class DienThoai:
    def __init__(self, MaMay, TenMay, HangSanXuat, DungLuongPin, GiaBan):
        self.MaMay = MaMay
        self.TenMay = TenMay
        self.HangSanXuat = HangSanXuat
        self.DungLuongPin = DungLuongPin
        self.GiaBan = GiaBan
    def thongtindienthoai(self):
        return (
            f"MaMay: {self.MaMay}\n"
            f"TenMay: {self.TenMay}\n"
            f"HangSanXuat: {self.HangSanXuat}\n"
            f"DungLuongPin: {self.DungLuongPin}\n"
            f"GiaBan: {self.GiaBan}"
        )
def main():
    phones = [
        DienThoai("DT01", "iPhone 15 Pro", "Apple", 3274, 28990000),
        DienThoai("DT02", "Galaxy S24 Ultra", "Samsung", 5000, 29990000),
    ]
    for phone in phones:
        print(phone.thongtindienthoai())
if __name__ == "__main__":
    main()
