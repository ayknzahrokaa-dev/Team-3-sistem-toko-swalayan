import unittest
from makanan import Makanan

class TestValidation(unittest.TestCase):

    #  Nama kosong
    def test_nama_kosong(self):
        with self.assertRaises(ValueError):
            Makanan("", 10000, 8000, 10, "2026-12-01")

    #  Harga negatif
    def test_harga_negatif(self):
        with self.assertRaises(ValueError):
            Makanan("Roti", -10000, 8000, 10, "2026-12-01")

    #  Stok negatif
    def test_stok_negatif(self):
        with self.assertRaises(ValueError):
            Makanan("Roti", 10000, 8000, -5, "2026-12-01")

    #  Data valid
    def test_data_valid(self):
        barang = Makanan("Roti", 10000, 8000, 10, "2026-12-01")
        self.assertEqual(barang.nama, "Roti")

if __name__ == "__main__":
    unittest.main()