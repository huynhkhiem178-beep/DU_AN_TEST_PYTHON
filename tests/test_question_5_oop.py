from src.exam_tasks import DienThoai

def test_create_iphone_object_and_attributes():
    phone = DienThoai("DT01", "iPhone 15 Pro", "Apple", 3274, 28990000)
    assert phone.MaMay == "DT01"
    assert phone.TenMay == "iPhone 15 Pro"
    assert phone.HangSanXuat == "Apple"
    assert phone.DungLuongPin == 3274
    assert phone.GiaBan == 28990000

def test_create_samsung_object():
    phone = DienThoai("DT02", "Galaxy S24 Ultra", "Samsung", 5000, 29990000)
    assert phone.TenMay == "Galaxy S24 Ultra"
    assert phone.GiaBan == 29990000

def test_thongtindienthoai_contains_all_fields():
    phone = DienThoai("DT01", "iPhone 15 Pro", "Apple", 3274, 28990000)
    output = phone.thongtindienthoai()
    for value in ["DT01", "iPhone 15 Pro", "Apple", "3274", "28990000"]:
        assert value in output
