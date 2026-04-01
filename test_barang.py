import unittest
from makanan import Makanan

class TestBarang(unittest.TestCase):

    def setUp(self):
        self.barang = Makanan("Roti", 10000, 8000, 10, "2026-12-01")

    #  Test getter stok
    def test_get_stok(self):
        self.assertEqual(self.barang.stok, 10)

    #  Test setter stok valid
    def test_set_stok_valid(self):
        self.barang.stok = 5
        self.assertEqual(self.barang.stok, 5)

    #  Test stok tidak boleh negatif
    def test_set_stok_negatif(self):
        with self.assertRaises(ValueError):
            self.barang.stok = -1

    #  Test akses langsung private (enkapsulasi)
    def test_private_stok(self):
        with self.assertRaises(AttributeError):
            _ = self.barang.__stok  # harus error

    #  Test harga modal tidak bisa diakses langsung
    def test_private_harga_modal(self):
        with self.assertRaises(AttributeError):
            _ = self.barang.__harga_modal

if __name__ == "__main__":
    unittest.main()