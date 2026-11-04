"""Test input/output cho tung y nho trong de thi."""
tests = {
    "Cau1a": [
        {
            "input": "635\n",
            "expected": [
                "n hop le:",
                "635"
            ]
        },
        {
            "input": "0\n1501\n12\n",
            "expected": [
                "nhap lai",
                "n hop le:",
                "12"
            ]
        }
    ],
    "Cau1b": [
        {
            "input": "635\n",
            "expected": [
                "so luong chu so le la:",
                "2"
            ]
        },
        {
            "input": "468\n",
            "expected": [
                "so luong chu so le la:",
                "0"
            ]
        }
    ],
    "Cau1c": [
        {
            "input": "1\n",
            "expected": [
                "s =",
                "0.5"
            ]
        },
        {
            "input": "2\n",
            "expected": [
                "s =",
                "0.75"
            ]
        }
    ],
    "Cau2a": [
        {
            "input": "AbCxyz\n",
            "expected": [
                "so ky tu chu hoa:",
                "2"
            ]
        },
        {
            "input": "python\n",
            "expected": [
                "so ky tu chu hoa:",
                "0"
            ]
        }
    ],
    "Cau2b": [
        {
            "input": "madam\n",
            "expected": [
                "chuoi doi xung:",
                "true"
            ]
        },
        {
            "input": "python\n",
            "expected": [
                "chuoi doi xung:",
                "false"
            ]
        }
    ],
    "Cau2c": [
        {
            "input": "a1b2c3\n",
            "expected": [
                "tong cac chu so:",
                "6"
            ]
        },
        {
            "input": "khong co so\n",
            "expected": [
                "tong cac chu so:",
                "0"
            ]
        }
    ],
    "Cau3a": [
        {
            "input": "2\n-3\n4\n0\n",
            "expected": [
                "danh sach:",
                "[2, -3, 4]"
            ]
        },
        {
            "input": "0\n",
            "expected": [
                "danh sach:",
                "[]"
            ]
        }
    ],
    "Cau3b": [
        {
            "input": "2\n-3\n4\n0\n",
            "expected": [
                "tong cac so duong chan:",
                "6"
            ]
        },
        {
            "input": "-2\n3\n0\n",
            "expected": [
                "tong cac so duong chan:",
                "0"
            ]
        }
    ],
    "Cau3c": [
        {
            "input": "2\n3\n2\n0\n2\n",
            "expected": [
                "so lan xuat hien cua k:",
                "2"
            ]
        },
        {
            "input": "5\n0\n8\n",
            "expected": [
                "so lan xuat hien cua k:",
                "0"
            ]
        }
    ],
    "Cau4a": [
        {
            "input": "1\nS01\nDe Men Phieu Luu Ky\nTo Hoai\nKim Dong\n1941\n",
            "expected": [
                "tu dien sach:",
                "S01",
                "De Men Phieu Luu Ky",
                "To Hoai",
                "Kim Dong",
                "1941"
            ]
        }
    ],
    "Cau4b": [
        {
            "input": "1\nS01\nSach mau\nTac gia\nNXB Tre\n2020\nS01\n",
            "expected": [
                "da xoa cuon sach:",
                "S01"
            ]
        },
        {
            "input": "1\nS01\nSach mau\nTac gia\nNXB Tre\n2020\nS99\n",
            "expected": [
                "khong tim thay cuon sach can xoa"
            ]
        }
    ],
    "Cau5a": [
        {
            "input": "",
            "expected": [
                "da dinh nghia lop dienthoai"
            ]
        }
    ],
    "Cau5b": [
        {
            "input": "",
            "expected": [
                "dt01",
                "iphone 15 pro",
                "apple",
                "3274",
                "28990000",
                "dt02",
                "galaxy s24 ultra",
                "samsung",
                "5000",
                "29990000"
            ]
        }
    ]
}
