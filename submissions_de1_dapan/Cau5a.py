"""Dap an tham khao Cau 5a: lop DienThoai."""
class DienThoai:
    def __init__(self, MaMay, TenMay, HangSanXuat, DungLuongPin, GiaBan):
        self.MaMay = MaMay
        self.TenMay = TenMay
        self.HangSanXuat = HangSanXuat
        self.DungLuongPin = DungLuongPin
        self.GiaBan = GiaBan

    def thongtindienthoai(self):
        print("MaMay:", self.MaMay)
        print("TenMay:", self.TenMay)
        print("HangSanXuat:", self.HangSanXuat)
        print("DungLuongPin:", self.DungLuongPin)
        print("GiaBan:", self.GiaBan)

if __name__ == "__main__":
    print("Da dinh nghia lop DienThoai")
